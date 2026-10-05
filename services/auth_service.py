from services.db_connection import DBConnection
import hashlib
import os
import hmac


# =========================================================
# PASSWORD HASHING
# =========================================================

def hash_password(password):
    """
    Generates a random salt for the password
    and hashes it using PBKDF2-HMAC-SHA256.
    """

    salt = os.urandom(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )

    return salt.hex(), password_hash.hex()


def verify_password(password, salt_hex, stored_hash):
    """
    Verifies the password during login.
    """

    salt = bytes.fromhex(salt_hex)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100_000
    )

    return hmac.compare_digest(
        password_hash.hex(),
        stored_hash
    )


# =========================================================
# USER SEARCH
# =========================================================

def find_user_by_username(username):
    """
    Searches for a user in the database by username.
    """

    db = DBConnection()

    try:
        return db.fetch_user_by_username(username)

    finally:
        db.close()


# =========================================================
# REGISTER
# =========================================================

def create_user(
    username,
    password,
    role="user"
):
    """
    Creates a new system user.
    """

    username = username.strip()

    # Username validation
    if not username:
        return False, "Username is required."

    if len(username) < 3:
        return False, "Username must be at least 3 characters."

    # Password validation
    if not password:
        return False, "Password is required."

    if len(password) < 3:
        return False, "Password must be at least 3 characters."


    db = DBConnection()

    try:

        # -------------------------------------------------
        # Check username
        # -------------------------------------------------

        existing_user = db.fetch_user_by_username(username)

        if existing_user:
            return False, "Username already exists."


        # -------------------------------------------------
        # Password hash
        # -------------------------------------------------

        salt, password_hash = hash_password(password)

        # Storing salt + hash together split by a colon
        stored_password = f"{salt}:{password_hash}"


        # -------------------------------------------------
        # Create user
        # -------------------------------------------------

        user_id = db.add_user(
            username,
            stored_password,
            role,
            True
        )


        return True, user_id

    finally:

        db.close()


# =========================================================
# LOGIN
# =========================================================

def authenticate_user(
    username,
    password
):
    """
    Authenticates username and verifies password.
    """

    username = username.strip()

    db = DBConnection()

    try:

        user = db.fetch_user_by_username(username)

        # User not found
        if not user:
            return None


        # -------------------------------------------------
        # Database result mapping
        #
        # (
        #   id,
        #   username,
        #   password_hash,
        #   role,
        #   status
        # )
        # -------------------------------------------------

        user_id = user[0]
        db_username = user[1]
        stored_password = user[2]
        role = user[3]
        status = user[4]


        # Inactive user
        if not status:
            return None


        # -------------------------------------------------
        # Separate salt + password hash
        # -------------------------------------------------

        if ":" not in stored_password:
            return None

        salt_hex, password_hash = stored_password.split(
            ":",
            1
        )


        # -------------------------------------------------
        # Password verification
        # -------------------------------------------------

        if not verify_password(
            password,
            salt_hex,
            password_hash
        ):
            return None


        # -------------------------------------------------
        # Authenticated user
        # -------------------------------------------------

        return {
            "id": user_id,
            "username": db_username,
            "role": role,
            "status": status
        }

    finally:

        db.close()

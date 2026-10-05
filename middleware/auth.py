# middleware/auth.py

import secrets


# Server-side session storage
SESSIONS = {}


PUBLIC_ROUTES = {
    "/login",
    "/register"
}


def create_session(user):

    session_id = secrets.token_urlsafe(32)

    SESSIONS[session_id] = {
        "user_id": user["id"],
        "username": user["username"]
    }

    return session_id


def get_session(session_id):

    if not session_id:
        return None

    return SESSIONS.get(session_id)


def destroy_session(session_id):

    if session_id in SESSIONS:
        del SESSIONS[session_id]


def is_public_route(path):

    return path in PUBLIC_ROUTES


def is_authenticated(session_id):

    return get_session(session_id) is not None


def get_session_id_from_cookie(handler):

    cookie_header = handler.headers.get("Cookie")

    if not cookie_header:
        return None

    cookies = {}

    for item in cookie_header.split(";"):

        if "=" not in item:
            continue

        key, value = item.strip().split("=", 1)

        cookies[key] = value

    return cookies.get("session_id")


def require_authentication(handler):

    path = handler.path.split("?")[0]

    # Login/Register not protected
    if is_public_route(path):
        return True

    session_id = get_session_id_from_cookie(handler)

    if not is_authenticated(session_id):

        handler.send_response(303)
        handler.send_header("Location", "/login")
        handler.end_headers()

        return False

    return True


def get_current_user(handler):

    session_id = get_session_id_from_cookie(handler)

    if not session_id:
        return None

    return get_session(session_id)
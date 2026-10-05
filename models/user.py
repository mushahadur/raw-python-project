
class User:

    def __init__(
        self,
        user_id,
        username,
        password_hash,
        role,
        status
    ):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.role = role
        self.status = status

    def show_info(self):
        print(
            f"ID: {self.user_id}, "
            f"Username: {self.username}, "
            f"Role: {self.role}, "
            f"Status: {self.status}"
        )


from . import cursor
from werkzeug.security import check_password_hash

class Admin:
    def __init__(self, username: str = None, password: str = None, password2: str = None) -> None:
        self.username = username
        self.password = password
        self.password2 = password2

    @staticmethod
    def get_user_by_username(username):
        query = "SELECT username, password FROM admin WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result:
            return {"username": result[0], "password": result[1]}
        return None

    @staticmethod
    def validate(username, password):
        user = Admin.get_user_by_username(username)
        if not user:
            return False
        return check_password_hash(user["password"], password)

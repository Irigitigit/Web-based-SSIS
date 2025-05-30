from . import cursor
from werkzeug.security import check_password_hash

class Admin():
    def __init__(self, username: str = None, password: str = None, password2: str = None) -> None:
        self.username = username
        self.password = password
        self.password2 = password2

    @staticmethod
    def validate(username: str, password: str) -> bool:
        query = f'''
            SELECT username, password 
            FROM admin
            WHERE username = %s;
        '''
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if not result:
            return False

        stored_username, hashed_password = result
        return check_password_hash(hashed_password, password)


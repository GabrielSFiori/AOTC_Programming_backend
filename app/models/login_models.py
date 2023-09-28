from ..database import DatabaseConnection


class Login:

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.users = kwargs.get('users')
        self.email = kwargs.get('email')
        self.passwords = kwargs.get('passwords')
        self.birthday_date = kwargs.get('birthday_date')

    @classmethod
    def is_registered(cls, user):
        query = """SELECT user_id FROM app_coding.users 
        WHERE email = %(email)s and passwords = %(passwords)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False

    @classmethod
    def get(cls, user):
        query = """SELECT * FROM app_coding.users 
        WHERE email = %(email)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                user_id=result[0],
                first_name=result[1],
                last_name=result[2],
                users=result[3],
                email=result[4],
                passwords=result[5],
                birthday_date=result[6]
            )
        return None

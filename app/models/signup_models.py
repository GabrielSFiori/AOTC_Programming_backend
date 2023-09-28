"""from ..database import DatabaseConnection

from flask import jsonify, session


class SignUp:
    def init(self, **kwargs):
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.users = kwargs.get('users', None)
        self.email = kwargs.get('email', None)
        self.passwords = kwargs.get('passwords', None)
        self.birthday_date = kwargs.get('birthday_date', None)
        self.route_img = kwargs.get('route_img', None)

    @classmethod
    def signup(cls, user):
        query = """  # INSERT INTO app_coding.users (first_name, last_name, users, email, passwords, birthday_date) VALUES (%(first_name)s, %(last_name)s, %(users)s, %(email)s, %(passwords)s, %(birthday_date)s"""
"""        params = user.__dict__
        response = DatabaseConnection.execute_query(query, params=params)

        if response is not None:
            return True
        return None"""
""

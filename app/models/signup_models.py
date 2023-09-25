from ..database import DatabaseConnection

from flask import jsonify, session


class SignUp:
    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.user_name = kwargs.get('user_name', None)
        self.email = kwargs.get('email', None)
        self.password = kwargs.get('password', None)
        self.birthday_date = kwargs.get('birthday_date', None)
        self.route_img = kwargs.get('route_img', None)

    @classmethod
    def signup(cls, user):
        query = """INSERT INTO app_coding.users (first_name, last_name, users, email, passwords, birthday_date, route_img) VALUES (%(name)s, %(lastname)s, %(username)s, %(email)s, %(password)s, %(birthday_date)s, %(route_img)s);"""
        params = user.__dict__
        response = DatabaseConnection.execute_query(query, params=params)

        if response is not None:
            return True
        return None

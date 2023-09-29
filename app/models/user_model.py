from ..database import DatabaseConnection


class User:
    def __init__(self, user_id: str = None, users: str = None, passwords: str = None,
                 email: str = None, first_name: str = None,
                 last_name: str = None, birthday_date: str = None):
        self.user_id = user_id
        self.users = users
        self.passwords = passwords
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.birthday_date = birthday_date

# Serializa el objeto Usuario en un diccionario

    def serialize(self):
        method_serialize = {
            "user_id": self.user_id,
            "users": self.users,
            "passwords": self.passwords,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday_date": self.birthday_date
        }
        return method_serialize

# Creacion de un nuevo Usuario                                                                                                                                                                                               io

    @classmethod
    def create_user(cls, user):
        query = "INSERT INTO app_coding.users (users, passwords, email, first_name, last_name, birthday_date) values (%s, %s, %s, %s, %s, %s)"
        params = (
            user.users,
            user.passwords,
            user.email,
            user.first_name,
            user.last_name,
            user.birthday_date)
        DatabaseConnection.execute_query_pr(query, params)

# Obtener un Usuario
    @classmethod
    def get_all(cls):
        consulta = """SELECT * FROM app_coding.users"""
        results = DatabaseConnection.get_all(
            consulta=consulta, diccionario=True)
        users = list(results)
        return users

# Obtener un Usuario por ID
    @classmethod
    def get(cls, user):
        """Get users for id
        Returns:
            - list: List of Film objects
        """
        query = """SELECT user_id, users, passwords, email, first_name, last_name, birthday_date
                FROM app_coding.users
                WHERE user_id = %s"""
        params = (user.user_id,)
        results = DatabaseConnection.fetch_one(query, params=params)

        if results is not None:
            return cls(*results)
        return None

# Actualizar un Usuario
    @classmethod
    def update_user_pr(cls, user):
        query = """UPDATE app_coding.users as u SET
        u.first_name = %s,
        u.last_name = %s,
        u.users = %s,
        u.email = %s,
        u.passwords = %s,
        u.birthday_date = %s
        WHERE u.user_id = %s"""
        params = (user.first_name,
                  user.last_name,
                  user.users,
                  user.email,
                  user.passwords,
                  user.birthday_date,
                  user.user_id)
        DatabaseConnection.execute_query_pr(
            query=query, params=params)

# Eliminar un usuario

    @classmethod
    def delete(cls, user_id: int):
        """Delete a user
        Args:
            - film (Film): Film object with the id attribute
        """
        query = "DELETE FROM app_coding.users WHERE user_id = %s"
        params = (user_id,)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def user_exist(cls, user_id):
        consulta = """SELECT u.user_id FROM app_coding.users as u WHERE u.user_id = %s"""
        response = DatabaseConnection.fetch_one(
            consulta=consulta, parametros=user_id)
        return response != None

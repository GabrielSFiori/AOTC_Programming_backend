from ..database import DatabaseConnection


class User:
    def __init__(self, user_id: str = None, users: str = None,
                 email: str = None, first_name: str = None,
                 last_name: str = None, birthday_date: str = None):
        self.user_id = user_id
        self.users = users
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.birthday_date = birthday_date


# Serializa el objeto Usuario en un diccionario

    def serialize(self):
        method_serialize = {
            "user_id": self.user_id,
            "users": self.users,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday_date": self.birthday_date
        }
        return method_serialize

# Creacion de un nuevo Usuario

    @classmethod
    def crear_usuario(cls, user):
        insert_query = "INSERT INTO users (users, passwords, email, first_name, last_name, birthday_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            user.username, user.passwords, user.email,
            user.first_name, user.last_name, user.date_of_birth,
            user.creation_date, user.last_login, user.status_id,
            user.avatar_url
        )
        DatabaseConnection.execute_query(insert_query, values)

# Obtener un Usuario

    @classmethod
    def get_all(cls):
        """Get all users
        Returns:
            - list: List of User objects
        """
        query = """SELECT * FROM app_coding.users"""

        results = DatabaseConnection.fetch_all(query=query)
        usuarios = list(results)
        return usuarios

# Obtener un Usuario por ID
    @classmethod
    def get(cls, user):
        """Get users for id
        Returns:
            - list: List of Film objects
        """
        query = """SELECT user_id, users, email, first_name, last_name, birthday_date
                FROM app_coding.users
                WHERE user_id = %s"""
        params = (user.user_id,)
        results = DatabaseConnection.fetch_one(query, params=params)

        if results is not None:
            return cls(*results)
        return None

# Actualizar un Usuario
    @classmethod
    def actualizar_usuario(cls, user_id, new_date):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        update_query = "UPDATE users SET users=%s, password=%s, email=%s, first_name=%s, last_name=%s, date_of_birth=%s, creation_date=%s, last_login=%s, status_id=%s, avatar_url=%s WHERE user_id=%s"
        values = (
            new_date['users'], new_date['password'],
            new_date['email'], new_date['first_name'],
            new_date['last_name'], new_date['birthday_date'],
            new_date['creation_date'], new_date['last_login'],
            new_date['status_id'], new_date['avatar_url'], user_id
        )

        cursor.execute(update_query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return True
# Eliminar un usuario

    @classmethod
    def eliminar_usuario(cls, user_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        delete_query = "DELETE FROM users WHERE user_id=%s"
        cursor.execute(delete_query, (user_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return True

    @classmethod
    def user_exist(cls, user_id):
        consulta = """SELECT u.user_id FROM app_coding.users as u WHERE u.user_id = %s"""
        response = DatabaseConnection.fetch_one(
            consulta=consulta, parametros=user_id)
        return response != None

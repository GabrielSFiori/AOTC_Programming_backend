from database import DatabaseConnection


class User:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.username = kwargs.get('users')
        self.password = kwargs.get('password')
        self.email = kwargs.get('email')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.birthday_date = kwargs.get('birthday_date')
        self.creation_date = kwargs.get('creation_date')
        self.last_login = kwargs.get('last_login')
        self.status_id = kwargs.get('status_id')
        self.avatar_url = kwargs.get('avatar_url', None)

# Serializa el objeto Usuario en un diccionario
    def serialize(self):
        user_dict = {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday_date': self.birthday_date,
            'creation_date': self.creation_date,
            'last_login': self.last_login,
            'status_id': self.status_id,
            'avatar_url': self.avatar_url
        }
        return user_dict


# Creacion de un nuevo Usuario

    @classmethod
    def crear_usuario(cls, user):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        insert_query = "INSERT INTO users (users, password, email, first_name, last_name, birthday_date, creation_date, last_login, status_id, avatar_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            user.username, user.password, user.email,
            user.first_name, user.last_name, user.date_of_birth,
            user.creation_date, user.last_login, user.status_id,
            user.avatar_url
        )

        cursor.execute(insert_query, values)
        conn.commit()

        user_id = cursor.lastrowid
        cursor.close()
        conn.close()

        return user_id
# Obtener un Usuario

    @classmethod
    def obtener_usuarios(cls):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        usuarios = cursor.fetchall()

        cursor.close()
        conn.close()

        return [cls(**usuario) for usuario in usuarios]

# Obtener un Usuario por ID
    @classmethod
    def obtener_usuario_por_id(cls, user_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(select_query, (user_id,))
        usuario = cursor.fetchone()

        cursor.close()
        conn.close()

        return usuario
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

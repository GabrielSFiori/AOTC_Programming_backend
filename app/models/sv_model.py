from ..database import DatabaseConnection


class Server:
    def __init__(self, **kwargs):
        self.server_id = kwargs.get('server_id')
        self.name_server = kwargs.get('name_server')
        self.description_server = kwargs.get('description_server', '')
        # ID del usuario que creó el servidor
        self.property_id = kwargs.get('property_id')
        self.members = []  # Lista de usuarios miembros del servidor
        self.channels = []  # Lista de canales en el servidor

    def serialize(self):
        # Método para serializar el objeto del servidor a un diccionario
        server_dict = {
            'server_id': self.server_id,
            'name_server': self.name_server,
            'description_server': self.description_server,
            'property_id': self.property_id,
            # Serializar usuarios miembros
            'members': [member.serialize() for member in self.members],
            # Serializar canales
            'channels': [channel.serialize() for channel in self.channels],
        }
        return server_dict

# Logica de Servidor
# Creacion de un nuevo Servidor
    @classmethod
    def create_server(cls, server):

        query = "INSERT INTO app_coding.servers (name_server, description_server) VALUES (%s, %s)"
        params = (server.name_server, server.description_server)
        DatabaseConnection.execute_query_pr(query, params)

# Obtener un Servidor
    @classmethod
    def get_all_servers(cls):
        consulta = """SELECT * FROM app_coding.servers"""
        results = DatabaseConnection.get_all(
            consulta=consulta, diccionario=True)
        users = list(results)
        return users

# Actualizar un Servidor

    @classmethod
    def update_server(cls, server_id, new_data):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        update_query = "UPDATE servers SET name_server=%s, description_server=%s WHERE server_id=%s"
        values = (new_data['name'], new_data['description'], server_id)

        cursor.execute(update_query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return True
# Borrar un Servidor

    @classmethod
    def delete_server(cls, server_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor()

        delete_query = "DELETE FROM servers WHERE server_id=%s"
        cursor.execute(delete_query, (server_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return True

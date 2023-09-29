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

        query = "INSERT INTO app_coding.servers (name_server, description_server, property_id) VALUES (%s, %s, %s)"
        params = (server.name_server,
                  server.description_server, server.property_id)
        DatabaseConnection.execute_query_pr(query, params)

# Obtener todos los servidores
    @classmethod
    def get_all_servers(cls):
        consulta = """SELECT * FROM app_coding.servers"""
        results = DatabaseConnection.get_all(
            consulta=consulta, diccionario=True)
        users = list(results)
        return users

    @classmethod
    def get_server(cls, server_id):
        """Get Server"""
        query = """
            SELECT server_id, name_server, description_server, property_id
            FROM servers
            WHERE server_id = %s
        """
        server_data = DatabaseConnection.fetch_one(query, (server_id,))
        if server_data is not None:
            server = Server(
                server_id=server_data[0],
                server_name=server_data[1],
                server_description=server_data[2],
                owner_id=server_data[3],
            )
            return server

        return None


# Actualizar un Servidor

    @classmethod
    def update_user_pr(cls, server):
        query = """UPDATE app_coding.servers as u SET
        u.name_server = %s,
        u.description_server = %s,
        WHERE u.server_id = %s"""
        params = (server.name_server,
                  server.description_server,
                  server.server_id)
        DatabaseConnection.execute_query_pr(
            query=query, params=params)

# Borrar un Servidor

    @classmethod
    def delete_server(cls, server_id: int):
        """Delete a user
        Args:
            - film (Film): Film object with the id attribute
        """
        query = "DELETE FROM app_coding.users WHERE user_id = %s"
        params = (server_id,)
        DatabaseConnection.execute_query(query, params=params)

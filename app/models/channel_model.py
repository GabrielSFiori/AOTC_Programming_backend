from ..database import DatabaseConnection


class ChannelModel:
    def __init__(self, **kwargs):
        self.channel_id = kwargs.get('channel_id')
        self.server_id = kwargs.get('server_id')
        self.name = kwargs.get('name')

    def serialize(self):
        # Método para serializar el objeto del canal a un diccionario
        channel_dict = {
            'channel_id': self.channel_id,
            'server_id': self.server_id,
            'name': self.name,
        }
        return channel_dict
# Creacion de un nuevo Canal

    @classmethod
    def create_channel(cls, channel):
        query = "INSERT INTO app_coding.channels (server_id, name, description) values (%s, %s, %s)"
        params = (
            channel.server_id,
            channel.name,
            channel.description
        )
        DatabaseConnection.execute_query_pr(query, params)

# Obtener Canales de un Servidor

    @classmethod
    def get_channels_by_server(cls, channels):
        consulta = """SELECT * FROM app_coding.servers WHERE server_id = %s"""
        results = DatabaseConnection.get_all(
            consulta=consulta, diccionario=True)
        channels = list(results)
        return [cls(**channel) for channel in channels]
# Obtener Canal por su ID

    @classmethod
    def get_channel_by_id(cls, channel_id):
        conn = DatabaseConnection.connect()
        cursor = conn.cursor(dictionary=True)

        select_query = "SELECT * FROM channels WHERE channel_id = %s"
        cursor.execute(select_query, (channel_id,))
        channel = cursor.fetchone()

        cursor.close()
        conn.close()

        return cls(**channel) if channel else None
# Actualizar un Canal

    @classmethod
    def update_channel(cls, channel_id, new_data):
        query = "UPDATE channels SET name = %s WHERE channel_id = %s"
        params = (new_data['name'], channel_id)

        DatabaseConnection.execute_query_pr(
            query=query, params=params)

        return True
# Borrar un Canal

    @classmethod
    def delete_channel(cls, channel_id):
        """Delete a user
        Args:
            - film (Film): Film object with the id attribute
        """
        query = "DELETE FROM app_coding.channel WHERE channel_id = %s"
        params = (channel_id,)
        DatabaseConnection.execute_query(query, params=params)

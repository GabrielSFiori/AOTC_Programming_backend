from ..database import DatabaseConnection
from ..models.exception import BadRequest


class Message:
    def __init__(self, **kwargs) -> None:
        self.id_msg = kwargs.get('id_msg', None)
        self.id_user = kwargs.get('id_user', None)
        self.content = kwargs.get('content', None)
        self.date_day = kwargs.get('date_day', None)
        self.date_time = kwargs.get('date_time', None)
        self.id_channel = kwargs.get('id_channel', None)

    @classmethod
    def get_message(cls, id_msg):
        query = "SELECT * FROM messages WHERE message_id = %s"
        msg = DatabaseConnection.fetch_one(query, (id_msg,))
        if msg is not None:
            return Message(
                id_msg=msg[0],
                id_user=msg[1],
                content=msg[2],
                date_day=msg[3],
                date_time=msg[4],
                id_channel=msg[5]
            )
        return None

    @classmethod
    def get_messages(cls, id_msg) -> list['Message']:
        query = "SELECT chats.id_msg, chats.id_user, chats.content, chats.date_day, chats.date_time, chats.id_channel FROM chats JOIN users ON chats.id_user = users.user_id WHERE id_msg = %s"
        msgs = DatabaseConnection.fetch_all(query, (id_msg,))

        msg_list = []
        for msg in msgs:
            msg_data = Message(
                id_msg=msg[0],
                id_user=msg[1],
                content=msg[2],
                date_day=msg[3],
                date_time=msg[4],
                id_channel=msg[5]
            )
            msg_list.append(msg_data)

        return msg_list

    @classmethod
    def delete_message(cls, id_msg) -> None:
        query = "DELETE FROM chats WHERE id_msg = %s"
        DatabaseConnection.execute_query(query, (id_msg,))

    @classmethod
    def create_message(cls, message: 'Message') -> None:
        query = "INSERT INTO app_codding.chats (content, id_user, id_channel) VALUES (%s, %s, %s)"
        params = (message.content, message.id_user, message.id_channel)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def update_message(cls, params: tuple) -> None:
        query = "UPDATE app_codding.chats SET content = %s, date_day = CURRENT_TIMESTAMP() WHERE id_msg = %s"
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def exist(cls, msg_id: int):
        query = "SELECT 1 FROM app_codding.chats WHERE id_msg = %s"
        result = DatabaseConnection.fetch_one(query, (msg_id,))
        return result is not None

    @classmethod
    def validate_data(cls, data) -> 'Message':
        """Validate message data"""
        msg_content = data[0]
        if len(msg_content) < 1:
            raise BadRequest(
                "El cuerpo del mensaje debe tener al menos un carácter")

        id_msg_user = data[1]
        if not isinstance(id_msg_user, int):
            raise BadRequest("El ID de usuario debe ser un número entero")

        id_msg_channel = data[2]
        if not isinstance(id_msg_channel, int):
            raise BadRequest(
                "El identificador de canal debe ser un número entero")

        return Message(content=msg_content, id_user=id_msg_user, id_channel=id_msg_channel)

    def serialize(self):
        return {
            'message_id': self.id_msg,
            'message_body': self.content,
            'user_id': self.id_user,
            'channel_id': self.id_channel,
            'creation_date': self.date_day,
            'update_date': self.date_time

        }

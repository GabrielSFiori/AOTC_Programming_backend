from ..database import DatabaseConnection
from flask import jsonify
from datetime import datetime


class Messages:
    def __init__(self, id_msg=None, id_user=None, content=None, date_day=None, date_time=None, id_channel=None):
        self.id_msg = id_msg
        self.id_user = id_user
        self.content = content
        self.date_day = date_day
        self.date_time = date_time
        self.id_channel = id_channel

    def formatted_response(self):
        return {
            'id_msg': int(self.id_msg),
            'id_user': int(self.id_user),
            'content': str(self.content),
            'date_day': str(self.date_day),
            'date_time': str(self.date_time),
            'id_channel': int(self.id_channel),
        }

    @classmethod
    def get_messages(cls, messages):
        query = """SELECT chats.id_msg, chats.id_user, chats.content, DATE_FORMAT(chats.date_day, '%d-%m-%Y'), TIME_FORMAT(chats.date_time, '%H:%i'), chats.id_channel FROM app_coding.content as chats WHERE id_channel = %s;"""
        params = messages.id_channel,
        responses = DatabaseConnection.fetch_all(query, params=params)
        all_messages = []

        if responses is not None:
            for response in responses:
                all_messages.append(cls(*response))
            return all_messages
        return None

    @classmethod
    def create_message(cls, messages):
        query = """INSERT INTO app_coding.chats (id_msg, id_user, content, date_day, date_time, id_channel) VALUES (%s, %s, %s, CURDATE(), CURTIME(), %s);"""

        params = messages.id_msg, messages.id_user, messages.content, messages.dateday, messages.date_time, messages.id_channel
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update_message(cls, id_msg, message):
        query = """UPDATE app_coding.chats AS content SET chats.content = %s, chats.date_day = CURDATE(), chats.date_time = CURTIME() WHERE chats.id_msg = %s;"""

        params = message.content, id_msg
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_message(cls, id_msg):
        query = """DELETE FROM app_coding.content WHERE content.id_msg = %s;"""

        params = (id_msg,)

        DatabaseConnection.execute_query(query, params=params)

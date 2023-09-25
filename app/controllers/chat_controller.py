from ..models.chat_model import Messages

from flask import jsonify, request


class ChatController:
    """Comentario"""

    @classmethod
    def get_messages(cls, channel_id):
        """Get all chanel messages"""
        messages = Messages(channel_id=channel_id)
        result = Messages.get_messages(messages)
        all_messages = []
        if result is not None:
            for message in result:
                all_messages.append(message.formatted_response())
            return all_messages, 200

    @classmethod
    def create_message(cls):
        data = request.json

        message = Messages(**data)

        Messages.create_message(message)
        response = {"success": "Exito al crear mensaje"}
        return response, 200

    @classmethod
    def update_message(cls, id_message):
        data = request.json

        # data['id_message'] = id_message

        message = Messages(**data)

        Messages.update_message(id_message, message)
        response = {"success": "Exito al editar mensaje"}
        return response, 200

    @classmethod
    def delete_message(cls, id_message):
        Messages.delete_message(id_message)
        response = {"success": "Exito al borrar mensaje"}
        return response, 200

from flask import Blueprint
from ..controllers.chat_controller import MessageController

messages_bp = Blueprint('message_bp', __name__)

# Ejemplo
messages_bp.route(
    '/<int:id_msg>', methods=['GET'])(MessageController.get_message)
messages_bp.route('', methods=['GET'])(MessageController.get_messages)
messages_bp.route(
    '/<int:id_msg>', methods=['DELETE'])(MessageController.delete_message)
messages_bp.route('', methods=['POST'])(MessageController.create_message)
messages_bp.route(
    '/<int:id_msg>', methods=['PATCH'])(MessageController.update_message)

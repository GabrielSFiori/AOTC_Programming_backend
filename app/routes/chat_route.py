from flask import Blueprint

from ..controllers.chat_controller import ChatController

messages_bp = Blueprint('messages_bp', __name__)

messages_bp.route('/<int:id_channel>',
                  methods=['GET'])(ChatController.get_messages)
messages_bp.route('/', methods=['POST'])(ChatController.create_message)
messages_bp.route('/<int:id_message>',
                  methods=['PUT'])(ChatController.update_message)
messages_bp.route('/<int:id_message>',
                  methods=['DELETE'])(ChatController.delete_message)

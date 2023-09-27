from flask import Blueprint
from ..controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(UserController.get_all)
user_bp.route('/', methods=['POST']
              )(UserController.crear_usuario)
user_bp.route('/<int:user_id>',
              methods=['GET'])(UserController.get)
user_bp.route('/usuario/<int:user_id>',
              methods=['PUT'])(UserController.actualizar_usuario)
user_bp.route('/usuario/<int:user_id>',
              methods=['DELETE'])(UserController.eliminar_usuario)

from flask import Blueprint
from ..controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/usuarios', methods=['GET'])(UserController.get_usuarios)
user_bp.route('/usuarios', methods=['POST']
              )(UserController.crear_usuario)
user_bp.route('/usuarios/<int:user_id>',
              methods=['GET'])(UserController.obtener_usuario_por_id)
user_bp.route('/usuarios/<int:user_id>',
              methods=['PUT'])(UserController.actualizar_usuario)
user_bp.route('/usuarios/<int:user_id>',
              methods=['DELETE'])(UserController.eliminar_usuario)

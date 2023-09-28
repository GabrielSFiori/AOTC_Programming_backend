from flask import Blueprint
from ..controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/usuario', methods=['GET'])(UserController.get_all)
user_bp.route('/usuario', methods=['POST']
              )(UserController.create_user)
user_bp.route('/usuario/<int:user_id>', methods=['GET'])(UserController.get)
user_bp.route('/usuario/<int:user_id>',
              methods=['PUT'])(UserController.update_user_endpoint)
user_bp.route('/usuario/<int:user_id>',
              methods=['DELETE'])(UserController.delete_user)

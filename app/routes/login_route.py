from flask import Blueprint

from ..controllers.login_controllers import LoginController

login_bp = Blueprint('login_bp', __name__)

login_bp.route('/login', methods=['POST'])(LoginController.login)
login_bp.route('/logout', methods=['GET'])(LoginController.logout)

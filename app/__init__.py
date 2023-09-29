from flask import Flask
from flask_cors import CORS
from config import Config

from .database import DatabaseConnection
from .routes.chat_route import messages_bp
from .routes.login_route import login_bp
from .routes.user_route import user_bp
from .routes.error_handlers import errors
from .routes.sv_route import server_bp


def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER,
                template_folder=Config.TEMPLATE_FOLDER)

    CORS(app,
         resources={r"/api/*": {"origins": "*"}},
         supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(messages_bp, url_prefix='/get_messages')

    app.register_blueprint(login_bp, url_prefix='/login')

    app.register_blueprint(user_bp, url_prefix='/usuario')

    app.register_blueprint(errors)

    app.register_blueprint(server_bp, url_prefix='/servers')

    return app

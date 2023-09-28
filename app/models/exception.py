from flask import jsonify


class CustomException(Exception):

    def init(self, status_code, name="Custom Error", description='Error'):
        super().init()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class BadRequest(CustomException):

    def init(self, description='Solicitud inválida'):
        super().init(400, name="Bad Request", description=description)


class NotFound(CustomException):
    def __init__(self, description="Out of range", status_code=404):
        self.description = description
        self.status_code = status_code
        super().__init__(self.description)


class InternalServerError(CustomException):

    def init(self, description='Error interno del servidor'):
        super().init(500, name="Internal Server Error", description=description)


class MethodNotAllowed(CustomException):

    def init(self, description='Método no permitido'):
        super().init(405, name="Method Not Allowed", description=description)


class UsuarioNoEncontrado(CustomException):
    def init(self, description="No se encontro el usuario en la base de datos."):
        super().init(500, name="User not registered", description=description)


class DataBaseError(CustomException):
    def init(self, description="Error al conectarse a la Base."):
        super().init(500, name="Database error", description=description)

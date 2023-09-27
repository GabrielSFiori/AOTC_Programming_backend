from flask import jsonify, request
from mysql.connector import Error as mysqlErrors
from ..models.user_model import User
from ..models.exception import *


class UserController:

    @classmethod  # Endpoint de Prueba http://127.0.0.1:5000/api/usuarios METODO POST
    def crear_usuario(cls):
        data = request.json
        nuevo_usuario = User(
            username=data.get('users'),
            password=data.get('password'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            birthday_date=data.get('birthday_date'),
            avatar_url=data.get('avatar_url')
        )

        user_id = User.crear_usuario(nuevo_usuario)

        if user_id:
            return jsonify({"user_id": user_id}), 201
        else:
            return jsonify({"message": "Error al crear el usuario"}), 500

    @classmethod  # Endpoint de Prueba http://127.0.0.1:5000/api/usuarios METODO GET
    def get_all(cls):
        respuesta = User.get_all()
        if respuesta is not None:
            return respuesta, 200
        raise NotFound()

    @classmethod
    def get(cls, user_id):
        """Get a user by id"""
        user = User(user_id=user_id)  # Crear una instancia de User
        # Llamar al método get de la instancia de User
        result = User.get(user)
        if result is not None:
            return result.serialize(), 200
        else:
            raise NotFound()

    @classmethod  # Endpoint de Prueba http://127.0.0.1:5000/api/usuarios/1 METODO PUT
    def actualizar_usuario(cls, user_id):
        data = request.json
        if User.actualizar_usuario(user_id, data):
            return jsonify({"message": "Usuario actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al actualizar el usuario"}), 500

    @classmethod  # Endpoint de Prueba http://127.0.0.1:5000/api/usuarios/1 METODO DELETE
    def eliminar_usuario(cls, user_id):
        if User.eliminar_usuario(user_id):
            return jsonify({"message": "Usuario eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al eliminar el usuario"}), 500

    @classmethod
    def control_existe_usuario(cls, id_usuario):
        if not (User.user_exist(id_usuario)):
            raise UsuarioNoEncontrado(
                "El usuario con id={} no se encontro en la base de datos.".format(id_usuario))

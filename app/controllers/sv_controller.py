from flask import jsonify, request
from ..models.sv_model import Server
from mysql.connector import Error as mysqlErrors
from ..models.exception import *


class ServerController:

    @classmethod  # Endpoint
    def create_server(cls):
        data = request.json
        new_server = Server(
            name=data.get('name_server'),
            description=data.get('description_server')
        )

        server_id = Server.create_server(new_server)

        if server_id:
            return jsonify({"server_id": server_id}), 201
        else:
            return jsonify({"message": "Error al crear el servidor"}), 500

    # Endpoint
    @classmethod
    def get_all_servers(cls):
        try:
            rta = Server.get_all_servers()
        except mysqlErrors as error:
            raise DataBaseError(
                "Se produjo un error al cargar todos los usuarios de la base de datos. {}".format(error))
        return rta, 200

    # Endpoint
    @classmethod
    def get_server_by_id(cls, server_id):
        server = Server.get_server_by_id(server_id)
        if server:
            return jsonify(server.serialize()), 200
        else:
            return jsonify({"message": "Servidor no encontrado"}), 404

    # Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO PUT
    @classmethod
    def update_server(cls, server_id):
        data = request.json
        if Server.update_server(server_id, data):
            return jsonify({"message": "Servidor actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al actualizar el servidor"}), 500

    # Endpoint de Prueba http://127.0.0.1:5000/api/servidores/{server_id} METODO DELETE
    @classmethod
    def delete_server(cls, server_id):
        if Server.delete_server(server_id):
            return jsonify({"message": "Servidor eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al eliminar el servidor"}), 500

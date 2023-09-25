from ..models.login_models import Login

from flask import jsonify, request, session


class LoginController():

    @classmethod  # ENDPOINT de prueba para login http://127.0.0.1:5000/login
    def login(cls):
        """Realiza el llamado al metodo para realizar el login"""
        data = request.json
        user = Login(
            email=data.get('email'),
            password=data.get('password')
        )

        if Login.login(user):
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401

    @classmethod  # ENDPOINT de prueba para http://127.0.0.1:5000/login/logout
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200
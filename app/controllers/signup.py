from ..models.signup_models import SignUp

from flask import jsonify, request, session


class SignUpController:

    @classmethod  # ENDPOINT de prueba para signup http://127.0.0.1:5000/signup
    def signup(cls):
        """Realiza el llamado al metodo para realizar el signup"""
        data = request.json
        user = SignUp(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            users=data.get('users'),
            email=data.get('email'),
            passwords=data.get('passwords'),
            birthday_date=data.get('birthday_date'),
            route_img=data.get('route_img')
        )

        if SignUp.signup(user):
            return {"message": "Registro exitoso"}, 200
        else:
            return {"message": "ha ocurrido un error"}, 401

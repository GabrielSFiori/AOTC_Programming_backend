import mysql.connector
from datetime import datetime


class DatabaseConnection:
    _connection = None
    _config = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host=cls._config['DATABASE_HOST'],
                user=cls._config['DATABASE_USERNAME'],
                port=cls._config['DATABASE_PORT'],
                password=cls._config['DATABASE_PASSWORD']
            )

        return cls._connection

    @classmethod
    def set_config(cls, config):
        cls._config = config

    @classmethod
    def execute_query(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        cls._connection.commit()

        return cursor

    @classmethod
    def fetch_all(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    @classmethod
    def fetch_one(cls, query, database_name=None, params=None):
        cursor = cls.get_connection().cursor()
        cursor.execute(query, params)

        return cursor.fetchone()

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None

    @classmethod
    def traer_uno(cls, consulta, parametros=None, formato=None, diccionario=False):
        cursor = cls.conectarse().cursor(dictionary=diccionario)
        if parametros != None:
            try:
                iter(parametros)
                if not (isinstance(parametros, str)):
                    if isinstance(parametros, datetime):
                        try:
                            cursor.execute(
                                consulta, parametros.strftime(formato))
                        except:
                            cursor.execute(
                                consulta, parametros.strftime("%Y-%m-%d"))
                    else:
                        cursor.execute(consulta, parametros)
                else:
                    cursor.execute(consulta, (parametros, ))
            except TypeError:
                cursor.execute(consulta, (str(parametros), ))
        else:
            cursor.execute(consulta)
        return cursor.fetchone()

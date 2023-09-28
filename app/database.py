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
    def get_all(cls, consulta, query=None, formato=None, diccionario=False):
        cursor = cls.get_connection().cursor(dictionary=diccionario)
        if query != None:
            try:
                iter(query)
                if not (isinstance(query, str)):
                    if isinstance(query, datetime):
                        try:
                            cursor.execute(
                                consulta, query.strftime(formato))
                        except:
                            cursor.execute(
                                consulta, query.strftime("%Y-%m-%d"))
                    else:
                        cursor.execute(consulta, query)
                else:
                    cursor.execute(consulta, (query, ))
            except TypeError:
                cursor.execute(consulta, (str(query), ))
        else:
            cursor.execute(consulta)
        return cursor.fetchall()

    @classmethod
    def execute_query_pr(cls, query, params=None, formato=None, diccionario=False):
        cursor = cls.get_connection().cursor(dictionary=diccionario)
        if params != None:
            try:
                iter(params)
                if not (isinstance(params, str)):
                    if isinstance(params, datetime):
                        try:
                            cursor.execute(
                                query, params.strftime(formato))
                        except:
                            cursor.execute(
                                query, params.strftime("%Y-%m-%d"))
                    else:
                        cursor.execute(query, params)
                else:
                    cursor.execute(query, (params, ))
            except TypeError:
                cursor.execute(query, (str(params), ))
        else:
            cursor.execute(query)
        cls._connection.commit()
        return cursor

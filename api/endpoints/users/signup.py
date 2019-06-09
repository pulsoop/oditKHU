import json
import pymysql
from flask import request
from flask_restful import Resource, reqparse, abort

import database

class Signup(Resource):
    def post(self):
        req_json = request.get_json(force=True)
        try:
            _id = req_json['id']
            _pw = req_json['password']
            _name = req_json['name']
            _email = req_json['email']
            _phone = req_json['phone']
        except KeyError:
            abort(400, message='Invalid parameter.')

        # db 
        db = database.db_connect()
        try:
            sql = "INSERT INTO dbdbdp.user (`id`, `password`, `name`, `email`, `phone_number`) VALUES ('{}', '{}', '{}', '{}', '{}');".format(_id, _pw, _name, _email, _phone)
            curs = db.cursor()
            curs.execute(sql)
            inserted_id = curs.lastrowid
            db.commit()
            error = False
        except pymysql.err.IntegrityError as exc:
            if str(exc.args[0]) == '1062':
                error = True
        except Exception as exc:
            error = True
        finally:
            curs.close()
            db.close()

        if error:
            return {'status': 500, 'messgae': 'Internal server error.'}, 500
        else:
            return {'status': 200, 'u_id': inserted_id}, 200
            
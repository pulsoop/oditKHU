import json
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
            db.commit()
        except:
            abort(500, message='Internal server error.')
        finally:
            curs.close()
            db.close()
            return {'status': 200}
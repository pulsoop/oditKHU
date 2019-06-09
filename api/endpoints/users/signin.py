import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

class Signin(Resource):
    def post(self):
        req_json = request.get_json(force=True)
        try:
            _id = req_json['id']
            _pw = req_json['password']
        except KeyError:
            abort(400, message='Invalid parameter.')

        # db 
        db = database.db_connect()
        sql = "SELECT count(id), id, name FROM dbdbdp.user WHERE id=\'{}\' AND password=\'{}\'".format(_id, _pw)
        curs = db.cursor()
        curs.execute(sql)
        rows = curs.fetchall()
        row = rows[0]

        # db close
        curs.close()
        db.close()

        if int(row[0]) >= 1:
            return {'id': row[1], 'name': row[2]}, 200   # Return data as JSON Type
        else:
            return {'status': 401, 'message': 'Error with id or password.'}, 401
        
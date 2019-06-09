import json
import bcrypt
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
            return {'status': 400, 'message': 'Invalid parameter.'}, 400
        
        # db 
        db = database.db_connect()
        sql = "SELECT count(id), password, id, name FROM dbdbdp.user WHERE id=\'{}\'".format(_id)
        curs = db.cursor()
        curs.execute(sql)
        rows = curs.fetchall()
        row = rows[0]

        # db close
        curs.close()
        db.close()

        # password check
        hashed = str(row[1]).encode('utf-8')
        pw_flag = bcrypt.checkpw(_pw.encode('utf-8'), hashed)

        if int(row[0]) >= 1 or pw_flag:
            return {'id': row[2], 'name': row[3]}, 200   # Return data as JSON Type
        else:
            return {'status': 401, 'message': 'Error with id or password.'}, 401
        
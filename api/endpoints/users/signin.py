import json
import bcrypt
from flask import request
from flask_restful import Resource, reqparse, abort

import auth
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
        sql = "SELECT count(id), password, u_id, id, name, email, phone_number FROM dbdbdp.user WHERE id=\'{}\'".format(_id)
        curs = db.cursor()
        curs.execute(sql)
        rows = curs.fetchall()
        row = rows[0]

        # db close
        curs.close()
        db.close()

        # password check
        hashed = str(row[1]).encode('utf-8')
        try:
            pw_flag = bcrypt.checkpw(_pw.encode('utf-8'), hashed)
        except:
            return {'status': 401, 'message': 'Error with id or password.'}, 401

        if int(row[0]) >= 1 or pw_flag:
            user = {
                'u_id': row[2],
                'id': row[3],
                'name': row[4],
                'email': row[5],
                'phone': row[6]
            }
            return {'status': 200, 'access_token': auth.generateAccessToken(user)}
        else:
            return {'status': 401, 'message': 'Error with id or password.'}, 401
        
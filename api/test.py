import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

class Test(Resource):
    def post(self):
        req_json = request.get_json(force=True)
        _id = req_json['id']

        # db 
        db = database.db_connect()
        sql = 'SELECT id, name FROM dbdbdp.user WHERE id=\'{}\''.format(_id)
        curs = db.cursor()
        curs.execute(sql)
        rows = curs.fetchall()

        # db close
        curs.close()
        db.close()

        if len(rows) == 1:
            return {'id': rows[0][0], 'name': rows[0][1]}   # Return data as JSON Type
        else:
            return abort(400)   # 400 ERROR
        
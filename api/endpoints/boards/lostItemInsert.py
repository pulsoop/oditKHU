import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

class LostItemInsert(Resource):
    def post(self):
        try:
            req_json = request.get_json(force=True)
            _u_id = req_json['u_id']
            _title = req_json['title']
            _content = req_json['content']
            _c_id = req_json['c_id']
        except KeyError:
            return {'status': 400, 'message': 'Invalid parameter.'}, 400

        # db
        db = database.db_connect()
        sql = 'INSERT INTO lostitem(u_id, title, content, c_id) VALUES ({}, \'{}\', \'{}\', {})'.format(_u_id, _title, _content, _c_id)
        curs = db.cursor()
        curs.execute(sql)
        inserted_id = curs.lastrowid
        db.commit()

        return {'status': 200, 'i_id': inserted_id}

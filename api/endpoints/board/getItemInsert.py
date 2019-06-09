import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

#getitem에 insert
class Test(Resource):

    def post(self):
        req_json = request.get_json(force=True)
        _i_id = req_json['i_id']
        _u_id = req_json['u_id']
        _title = req_json['title']
        _content = req_json['content']
        _c_id = req_json['c_id']

        # db
        db = database.db_connect() #connection객체
        sql = 'insert into getitem(i_id, u_id, title, content, c_id) values(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(_i_id, _u_id, _title, _content, _c_id)
        curs = db.cursor()
        curs.execute(sql)
        db.commit()
        rows = curs.fetchall()

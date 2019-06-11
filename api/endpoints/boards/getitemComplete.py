import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

#getitem ->  completeitem(i_id로 어떤거 옮길건지 선택)
class GetitemComplete(Resource):

     def post(self):
        req_json = request.get_json(force=True)
        _i_id = req_json['i_id']

        # db
        db = database.db_connect()  # connection객체
        sql1 = 'INSERT INTO completeitem (`u_id`, `title`, `content`, `getlost_date`, `c_id`) SELECT u_id, title, content, get_date, c_id FROM getitem WHERE i_id  = \'{}\''.format(_i_id)
        sql2 = 'DELETE FROM getitem WHERE i_id = \'{}\''.format(_i_id)
        curs = db.cursor()
        curs.execute(sql1)
        curs.execute(sql2)
        db.commit()


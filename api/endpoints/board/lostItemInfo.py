import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

class getitemInfo(Resource):
    def get(self):
        # db
        db = database.db_connect()  # connection객체
        sql = 'select u.id, title, content, register_date, get_date from getitem as gi join user as u on gi.u_id = u.u_id'
        curs = db.cursor()
        curs.execute(sql)

        rows = curs.fetchall()

        for row in rows:
            print(row)

        return {'id': rows[0][0], 'title': rows[0][1], 'content': rows[0][2], 'get_date': rows[0][3]}

        # db close - 연결 닫아
        curs.close()
        db.close()

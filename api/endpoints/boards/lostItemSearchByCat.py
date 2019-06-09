import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

#lostItem에서 키워드로 검색
class LostItemSearchByCat(Resource):
    def post(self):
        req_json = request.get_json(force=True)
        _c_id = req_json['c_id']

        # db
        db = database.db_connect() #connection객체
        sql = 'select u.id, title from lostitem as gi join user as u on gi.u_id = u.u_id where c_id = \'{}\''.format(_c_id)
        curs = db.cursor()
        curs.execute(sql)
        #db.commit()
        rows = curs.fetchall()

        curs.close()
        db.close()

        if len(rows) >= 1:
            return {'id': rows[0][0], 'title': rows[0][1]}   # Return data as JSON Type
        else:
            return abort(400)   # 400 ERRROR
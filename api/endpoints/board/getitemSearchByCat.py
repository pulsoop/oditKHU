import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

#getItem에서 키워드로 검색
class Test(Resource):
    def post(self):
        req_json = request.get_json(force=True)
        _c_id = req_json['c_id']

        # db
        db = database.db_connect() #connection객체
        sql = 'select u.id, title from getitem as gi join user as u on gi.u_id = u.u_id where c_id = \'{}\''.format(_c_id)
        curs = db.cursor() #cursor()메소드 호출 - fetch동작 관리
        curs.execute(sql) #sql문장을 DB서버에 보냄
        #db.commit() #db.commit()메서드를 사용하여 데이터 commit
        rows = curs.fetchall() #데이터를 서버로부터 가져온 후, fetch된 데이터 사용

        curs.close()
        db.close()

        #u_id말고 id로
        if len(rows) >= 1:
            return {'id': rows[0][0], 'title': rows[0][1]}   # Return data as JSON Type
        else:
            return abort(400)   # 400 ERRROR

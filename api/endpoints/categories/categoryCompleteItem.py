import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# category id를 통해 getitem
class CategoryCompleteItem(Resource):

    def get(self, c_id):

        # db
        db = database.db_connect() #connection객체
        sql = 'select u.id, title from completeitem as gi join user as u on gi.u_id = u.u_id where c_id = \'{}\''.format(c_id)
        curs = db.cursor() #cursor()메소드 호출 - fetch동작 관리
        curs.execute(sql) #sql문장을 DB서버에 보냄
        rows = curs.fetchall() #데이터를 서버로부터 가져온 후, fetch된 데이터 사용

        curs.close()
        db.close()

        result = {
            'status': 200,
            'c_id': c_id,
            'item_count': len(rows),
            'items': list() 
        }

        #u_id말고 id로
        for row in rows:
            temp = {
                'id': row[0],
                'title': row[1]
            }
            result['items'].append(temp)
        return result, 200

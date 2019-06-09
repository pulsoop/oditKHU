import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# getitem 릴레이션의 데이터를 모두 가져옴. 
class GetItemInfo(Resource):
    def get(self):
        # db
        db = database.db_connect()  # connection객체
        sql = 'SELECT u.id, title, content, register_date, get_date FROM getitem AS gi JOIN user AS u ON gi.u_id = u.u_id'
        curs = db.cursor()
        curs.execute(sql)

        rows = curs.fetchall()

        result = {
            'status': 200,
            'item_count': len(rows),
            'items': list()
        }

        for row in rows:
            temp = {
                'author': row[0],
                'title': row[1],
                'content': row[2],
                'register_date': row[3],
                'get_date': row[4]
            }
            result['items'].append(temp)
        
        # db close - 연결 닫아
        curs.close()
        db.close()

        return result, 200
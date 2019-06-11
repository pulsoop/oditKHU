import json
import datetime
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# lostitem 릴레이션의 데이터를 모두 가져옴. 
class LostItemInfo(Resource):
    def get(self):
        # db
        db = database.db_connect()  # connection객체
        sql = 'SELECT u.id, title, register_date, lost_date FROM lostitem AS li JOIN user AS u ON li.u_id = u.u_id'
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
                'register_date': row[2].strftime('%Y-%m-%d %H:%M:%S'),
                'lost_date': str(row[3])
            }
            result['items'].append(temp)
        
        # db close - 연결 닫아
        curs.close()
        db.close()

        return result, 200

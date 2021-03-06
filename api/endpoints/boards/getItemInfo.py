import json
import datetime
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# getitem 릴레이션의 데이터를 모두 가져옴. 
class GetItemInfo(Resource):
    def get(self):
        # db
        db = database.db_connect()  # connection객체
        sql = 'SELECT u.id, gi.title, gi.register_date, gi.get_date, gi.i_id, gimg.url FROM getitem AS gi JOIN user AS u ON gi.u_id = u.u_id LEFT OUTER JOIN getimage AS gimg ON gi.i_id = gimg.i_id ORDER BY gi.i_id DESC;'
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
                'get_date': row[2].strftime('%Y-%m-%d %H:%M:%S'),
                'url': 'http://oditkhu.dasom.io/page/view.html?board=get&id={}'.format(row[4]),
                'image': ''
            }
            if row[5] is not None:
                temp['image'] = 'http://oditkhu.dasom.io/img/items/' + row[5]
            else:
                temp['image'] = 'http://oditkhu.dasom.io/img/items/no-image-icon.jpg'
            result['items'].append(temp)
        
        # db close - 연결 닫아
        curs.close()
        db.close()

        return result, 200

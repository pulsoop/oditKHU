import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# getitem 게시글의 이미지 링크 데이터.
class GetItemImage(Resource):
    def get(self, i_id):
        result = {
            'status': 200,
            'i_id': i_id,
            'image_count': 0,
            'images': list()
        }

        db = database.db_connect()
        sql = 'SELECT url FROM dbdbdp.getimage WHERE i_id={};'.format(i_id)
        curs = db.cursor()
        curs.execute(sql)

        rows = curs.fetchall()
        curs.close()

        result['image_count'] = len(rows)
        for row in rows:
            link = 'http://oditkhu.dasom.io/img/items/' + row[0]
            result['images'].append(link)
        
        # db close - 연결 닫아
        db.close()

        return result, 200

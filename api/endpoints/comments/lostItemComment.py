import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# lostitem 게시글의 댓글 데이터.
class LostItemComment(Resource):
    def get(self, i_id):
        result = {
            'status': 200,
            'i_id': i_id,
            'comment_count': 0,
            'comments': list()
        }

        db = database.db_connect()
        sql = 'select u.id, u.name, allcomment.content from(select g_com.u_id, g_com.content from (lostcomment as g_com join lostitem as g_i on g_i.i_id = g_com.i_id) where g_i.i_id = {}) as allcomment join user as u on allcomment.u_id = u.u_id;'.format(i_id)
        curs = db.cursor()
        curs.execute(sql)

        rows = curs.fetchall()
        curs.close()

        result['comment_count'] = len(rows)
        for row in rows:
            temp = {
                'author_id': '',
                'author_name': '',
                'comment': ''
            }
            temp['author_id'] = row[0]
            temp['author_name'] = row[1]
            temp['comment'] = row[2]
            result['comments'].append(temp)
        
        # db close - 연결 닫아
        db.close()

        return result, 200

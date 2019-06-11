import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# getitem 게시글 데이터.
class GetItemArticle(Resource):
    def get(self, i_id):
        # 게시글 데이터.
        db = database.db_connect()
        sql = 'SELECT u.id as "author_id", u.name as "author_name", title, content, register_date, get_date FROM getitem AS gi JOIN user AS u ON gi.u_id = u.u_id WHERE gi.i_id={};'.format(i_id)
        curs = db.cursor()
        curs.execute(sql)

        rows = curs.fetchall()
        curs.close()
        if len(rows) <= 0:
            db.close()
            return {'status': 404, 'message': 'There is no item.'}, 404

        result = {
            'status': 200,
            'author_id': '',
            'author_name': '',
            'title': '',
            'content': '',
            'register_date': '',
            'get_date': '',
            'comment_count': 0,
            'comments': list()
        }
        row = rows[0]
        result['author_id'] = row[0]
        result['author_name'] = row[1]
        result['title'] = row[2]
        result['content'] = row[3]
        result['register_date'] = row[4].strftime('%Y-%m-%d %H:%M:%S')
        result['get_date'] = row[5].strftime('%Y-%m-%d %H:%M:%S')

        # comments
        sql = 'select u.id, u.name, allcomment.content from(select g_com.u_id, g_com.content from (getcomment as g_com join getitem as g_i on g_i.i_id = g_com.i_id) where g_i.i_id = 1) as allcomment join user as u on allcomment.u_id = u.u_id;'
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

import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# getitem 게시글의 댓글 추가.
class GetItemCommentInsert(Resource):
    def post(self, i_id):
        try:
            req_json = request.get_json(force=True)
            _u_id = req_json['u_id']
            _content = req_json['content']
        except KeyError:
            return {'status': 400, 'message': 'Invalid parameter.'}, 400

        # db
        db = database.db_connect()
        sql = 'INSERT INTO getcomment(u_id, i_id, content) VALUES ({}, {}, \'{}\')'.format(_u_id, i_id, _content)
        curs = db.cursor()
        curs.execute(sql)
        inserted_id = curs.lastrowid
        db.commit()

        return {'status': 200, 'get_com_id': inserted_id}
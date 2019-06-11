import json
from flask import request
from flask_restful import Resource, reqparse, abort

import database

# search. 
class Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('query', type=str, required=True)
        parser.add_argument('board', type=str, required=True)
        args = parser.parse_args()

        query = args['query'].replace('"', '').strip()
        sql = 'SELECT item.i_id, item.title, item.register_date, u.id, u.name FROM {} as item JOIN user as u ON item.u_id = u.u_id WHERE content LIKE "%{}%";'
        if args['board'] == 'get':
            sql = sql.format('getitem', query)
        elif args['board'] == 'lost':
            sql = sql.format('lostitem', query)
        elif args['board'] == 'complete':
            sql = sql.format('completeitem', query)
        else:
            return {'status': 400, 'message': 'Invalid parameter.'}, 400

        db = database.db_connect()
        curs = db.cursor()
        curs.execute(sql)
        rows = curs.fetchall()
        curs.close()

        result = {
            'status': 200,
            'query': '',
            'item_count': 0,
            'items': list()
        }
        result['item_count'] = len(rows)
        for row in rows:
            temp = {
                'i_id': row[0],
                'title': row[1],
                'register_date': row[2].strftime('%Y-%m-%d %H:%M:%S'),
                'author_id': row[3],
                'author_name': row[4]
            }
            result['items'].append(temp)
        
        db.close()

        return result, 200
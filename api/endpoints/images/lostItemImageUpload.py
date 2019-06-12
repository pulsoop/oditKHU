import os
import json
import werkzeug
from flask import request
from flask_restful import Resource, reqparse, abort

import database

UPLOAD_FOLDER = '../img'
parser = reqparse.RequestParser()
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')

#lostimage에 insert
class LostItemImageUpload(Resource):

    def post(self, i_id):
        data = parser.parse_args()
        if data['file'] == "":
            return {'status': 400, 'message': 'File not found.'}, 400
        photo = data['file']

        if photo:
            filename = 'getitem_{}.jpg'.format(i_id)
            photo.save(os.path.join(UPLOAD_FOLDER, filename))
            print(os.path.join(UPLOAD_FOLDER, filename))

            # db
            db = database.db_connect()
            sql = 'INSERT INTO lostimage(i_id, url) VALUES ({}, \'{}\')'.format(i_id, filename)
            curs = db.cursor()
            curs.execute(sql)
            db.commit()

        return {'status': 200}, 200
import sys
import time

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from endpoints.test import Test

from endpoints.users.signin import Signin
from endpoints.users.signup import Signup

from endpoints.boards.getItemInfo import GetItemInfo
from endpoints.boards.getItemInsert import GetItemInsert
from endpoints.boards.getItemArticle import GetItemArticle
from endpoints.boards.getItemComplete import GetItemComplete  
from endpoints.boards.lostItemInfo import LostItemInfo
from endpoints.boards.lostItemInsert import LostItemInsert
from endpoints.boards.lostItemArticle import LostItemArticle
from endpoints.boards.lostItemComplete import LostItemComplete

from endpoints.comments.getItemComment import GetItemComment
from endpoints.comments.getItemCommentInsert import GetItemCommentInsert
from endpoints.comments.lostItemComment import LostItemComment
from endpoints.comments.lostItemCommentInsert import LostItemCommentInsert

from endpoints.categories.categoryGetItem import CategoryGetItem
from endpoints.categories.categoryLostItem import CategoryLostItem
from endpoints.categories.categoryCompleteItem import CategoryCompleteItem

# Flask Setting
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={
    r"/*": {"origin": "*"}
})

# Endpoints - test
api.add_resource(Test, '/test')

# Endpoints - users
api.add_resource(Signin, '/signin')
api.add_resource(Signup, '/signup')

# Endpoints - boards
api.add_resource(GetItemInfo, '/boards/getitems')   # getitem 목록
api.add_resource(GetItemInsert, '/boards/getitems') # getitem 추가
api.add_resource(GetItemArticle, '/boards/getitems/<int:i_id>') # getitem 게시글 상세
api.add_resource(GetItemComplete, '/boards/getitems/<int:i_id>/complete') # getitem 게시글 완료 상태로 변경
api.add_resource(LostItemInfo, '/boards/lostitems')   # losttitem 목록
api.add_resource(LostItemInsert, '/boards/lostitems') # lostitem 추가
api.add_resource(LostItemArticle, '/boards/lostitems/<int:i_id>') # lostitem 게시글 상세
api.add_resource(GetItemComplete, '/boards/lostitems/<int:i_id>/complete') # lostitem 게시글 완료 상태로 변경

# Endpoints - comments
api.add_resource(GetItemComment, '/boards/getitems/<int:i_id>/comments')    # getitem 게시글의 댓글 목록
api.add_resource(GetItemCommentInsert, '/boards/getitems/<int:i_id>/comments')    # getitem 게시글의 댓글 추가
api.add_resource(LostItemComment, '/boards/lostitems/<int:i_id>/comments')    # getitem 게시글의 댓글 목록
api.add_resource(LostItemCommentInsert, '/boards/lostitems/<int:i_id>/comments')    # lostitem 게시글의 댓글 추가

# Endpoints - categories
api.add_resource(CategoryGetItem, '/categories/<int:c_id>/getitems')
api.add_resource(CategoryLostItem, '/categories/<int:c_id>/lostitems')
api.add_resource(CategoryCompleteItem, '/categories/<int:c_id>/completeitems')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = sys.argv[1]
        if 'release' in sys.argv[2].strip():
            release = True
        else:
            release = False
    else:
        port = 8000
        release = False

    if release:
        print('┌─────────────────────────────┐')
        print('│ port = {} || RELEASE MODE │'.format(port))
        print('└─────────────────────────────┘')
    else:
        print('┌───────────────────────────┐')
        print('│ port = {} || DEBUG MODE │'.format(port))
        print('└───────────────────────────┘')

    time.sleep(0.5)

    if release:
        app.run(debug=False, host='0.0.0.0', port=port)    # for release
    else:
        app.run(debug=True, host='127.0.0.1', port=port)   # for debug
import sys

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from endpoints.test import Test
from endpoints.users.signin import Signin
from endpoints.users.signup import Signup
from endpoints.boards.getItemInfo import GetItemInfo
from endpoints.boards.getItemInsert import GetItemInsert
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

# Endpoints - categories
api.add_resource(CategoryGetItem, '/categories/<int:c_id>/getitems')
api.add_resource(CategoryLostItem, '/categories/<int:c_id>/lostitems')
api.add_resource(CategoryCompleteItem, '/categories/<int:c_id>/completeitems')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000

    #app.run(debug=False, host='0.0.0.0', port=port)    # for release
    app.run(debug=False, host='127.0.0.1', port=port)   # for debug
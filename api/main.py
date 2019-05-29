import sys

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from test import Test

# Flask Setting
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={
    r"/*": {"origin": "*"}
})

# Endpoints
api.add_resource(Test, '/test')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000

    #app.run(debug=False, host='0.0.0.0', port=port)
    app.run(debug=True, host='127.0.0.1', port=port)
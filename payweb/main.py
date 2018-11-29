
from flask import Flask,make_response,jsonify
from app.view import *
from app.merchant.view import *
from app.database import *

baseUrl = "/scancode/api/v1"
app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(merchBlue, url_prefix=baseUrl+"/Merchant")

#创建数据库
init_db()


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host="192.168.5.9", port=8080, debug=True)

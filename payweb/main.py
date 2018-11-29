
from flask import Flask, make_response, jsonify
from app.view import *
from app.merchant.view import *
from app.database import *
from app.response import baseResponse
from app.exceptionHandler.view import exception

baseUrl = "/scancode/api/v1"
app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(merchBlue, url_prefix=baseUrl+"/Merchant")
app.register_blueprint(exception, url_prefix='/error')
# 创建数据库
#init_db()


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@exception.app_errorhandler(404)
@exception.app_errorhandler(401)
@exception.app_errorhandler(500)
def notFound(error):
    baseResponse["ResponseStatus"]["ErrorCode"] = error.code
    if error.code == 404:
        baseResponse["ResponseStatus"]["Message"] = "Not found"
    elif error.code == 500:
        baseResponse["ResponseStatus"]["Message"] = "Not found"
    elif error.code == 401:
        baseResponse["ResponseStatus"]["Message"] = error.to_dict()
    return make_response(jsonify(baseResponse), error.code)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

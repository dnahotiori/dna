
from flask import Flask, make_response, jsonify
from app.view import *
from app.merchant.view import *
from app.database import *
from app.response import BaseResponse,JSONResponse
# from app.exceptionHandler.view import exception

baseUrl = "/scancode/api/v1"
app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(merchBlue, url_prefix=baseUrl+"/merchant")

app.response_class = JSONResponse
# 创建数据库
init_db()


@app.before_request
def beforeRequest():
    print("beforeRequest")
    data = request.get_json()
    print(data)


@app.after_request
def afterRequest(response):
    response.headers["Content-Type"] = "application/json"
    print("after_request")
    return response


@app.teardown_request
def shutdown_session(exception=None):
    dbs.close()
    pass


@app.errorhandler(404)
def notFound(error):
    rsp = BaseResponse(404, "Not Found").ToDict()
    return make_response(jsonify(rsp.data), 404)


@app.errorhandler(400)
@app.errorhandler(500)
def internal_server_error(error):
    rsp = BaseResponse(400, error.args[0]).ToDict()
    return make_response(jsonify(rsp.data), 400)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    # app.run(host="192.168.5.9", port=8080, debug=True)

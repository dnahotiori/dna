
from flask import Flask, make_response, jsonify
from app.view import *
from app.merchant.view import *
from app.database import *
from app.response import BaseResponse, JSONResponse
from app.customError import *
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
    pass
    #print("Main_beforeRequest")


@app.after_request
def afterRequest(response):
    return response
    #response.headers["Content-Type"] = "application/json"
    #print("after_request")
    #return response


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
    if isinstance(error, APIException):
        rsp = BaseResponse(error.code, "%s" %
                           (error.message)).ToDict()
    else:
        rsp = BaseResponse(ErrorCode.BASECODE, error.args[0]).ToDict()
    return make_response(jsonify(rsp.data), 400)


@app.errorhandler(401)
def unauthorized(error):
    rsp = BaseResponse(401, "Unauthorized").ToDict()
    return make_response(jsonify(rsp.data), 401)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    # app.run(host="192.168.5.9", port=8080, debug=True)

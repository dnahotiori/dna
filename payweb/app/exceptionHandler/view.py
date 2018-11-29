# coding:utf-8
# error
from flask import Blueprint, make_response, jsonify
from app.response import baseResponse

exception = Blueprint('exception', __name__)


@exception.app_errorhandler(404)
@exception.app_errorhandler(401)
@exception.app_errorhandler(500)
def error(error):
    baseResponse["ResponseStatus"]["ErrorCode"] = error.code
    if error.code == 404:
        baseResponse["ResponseStatus"]["Message"] = "Not found"
    elif error.code == 500:
        baseResponse["ResponseStatus"]["Message"] = "Not found"
    elif error.code == 401:
        baseResponse["ResponseStatus"]["Message"] = error.to_dict()
    return make_response(jsonify(baseResponse), error.code)

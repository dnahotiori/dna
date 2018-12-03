from marshmallow import Schema, fields
from flask import jsonify
from werkzeug.wrappers import Response


class BaseResponse():
    def __init__(self, code: "int" = 0, msg: "str" = None, data: "dict" = None):
        self.ResponseStatus = ResponseStatus(code, msg)
        self.Data = data

    def ToDict(self):
        schema = BaseResponseSchema()
        return schema.dump(self)
    def __repr__(self):
        return '<BaseResponse(code={self.code!r})>'.format(self=self)


class ResponseStatus():
    def __init__(self, code: "int", msg: "str"):
        self.ErrorCode = code
        self.Message = msg


class ResponseStatusSchema(Schema):
    ErrorCode = fields.Int()
    Message = fields.Str()


class BaseResponseSchema(Schema):
    ResponseStatus = fields.Nested(ResponseStatusSchema())
    Data = fields.Dict()

class JSONResponse(Response):
    default_mimetype = "application/json"

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            rsp = BaseResponse(0, None, response).ToDict()
            response = jsonify(rsp.data)
        elif isinstance(response, BaseResponse):
            response = jsonify(response.ToDict().data)
        return super(JSONResponse, cls).force_type(response, environ)
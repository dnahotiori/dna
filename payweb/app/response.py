from marshmallow import Schema,fields

baseResponse = {
    "ResponseStatus": {"ErrorCode": 0, "Message": ""}
}

class BaseResponse():
    def __init__(self, code: "int", msg: "str"):
        self.ResponseStatus = ResponseStatus(code, msg)

    # def __repr__(self):
    #     return '<BaseResponse(name={self.name!r})>'.format(self=self)
        
class ResponseStatus():
    def __init__(self, code: "int", msg: "str"):
        self.ErrorCode = code
        self.Message = msg

class ResponseStatusSchema(Schema):
    ErrorCode=fields.Int()
    Message=fields.Str()

class BaseResponseSchema(Schema):
    ResponseStatus= fields.Nested(ResponseStatusSchema())
class APIException(Exception):
    def __init__(self, code: "int", message):
        super().__init__(self)
        self.message = message
        self.code = code


class ErrorCode():
    BASECODE = 400000
    # 参数为空
    PARA_NONE = BASECODE+1
    # 验签错误
    SIGN_ERROR = BASECODE+2
    # API超时
    TIME_OUT = BASECODE+3
    # 数据不存在
    DATA_NONE = BASECODE+4

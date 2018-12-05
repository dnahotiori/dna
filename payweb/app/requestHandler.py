from flask import request, abort, json
from app.response import APIBaseRequestSchema
import hmac
from hashlib import sha1
from app.fun_utilitys import *
from datetime import datetime
from app.customError import *
from app.bllBase import *
from app.db_models import Func_MerchantInfo


class requestValidate():
    def __init__(self, request):
        if request.content_length == 0:
            abort(401)
        postData = request.get_json()
        model = APIBaseRequestSchema().load(postData).data
        if model.AppId is None or model.Sign is None or model.MchID is None:
            abort(401)
            # raise APIException(ErrorCode.PARA_NONE,
            #                    "错误的参数[AppId,Sign,MchID]必填")

        merInfo = DbQuery(Func_MerchantInfo).filter(
        Func_MerchantInfo.AppId == model.AppId, Func_MerchantInfo.MchID == model.MchID).first()

        if merInfo is None:
            abort(401)
            #raise APIException(ErrorCode.DATA_NONE,
            #                   "不存在商户数据")

        key = merInfo.Key
        sign = OpenSign().CreateSign(postData, key)
        if model.Sign != sign:
            print("签名错误：POST:%s 生成：%s" % (model.Sign, sign))
            raise APIException(ErrorCode.SIGN_ERROR, "签名错误")

        sysT = getTime()
        dt1 = datetime.utcfromtimestamp(sysT)
        dt2 = datetime.utcfromtimestamp(model.TimeStamp)
        ts = abs((dt1-dt2).seconds)
        if ts > 10*60:
            print("请求超时：POST:%s TS:%s 当前系统时间：%s TS:%s" % (dt2,model.TimeStamp, dt1, sysT))
            raise APIException(ErrorCode.TIME_OUT, "请求超时")

        print("Validate pass,OK!")


class OpenSign():
    def __init__(self):
        pass

    def CreateSign(self, postData: "dict", serkey):
        keys = sorted(postData)
        listParas = []
        for key in keys:
            if key.lower() == "sign":
                continue
            listParas.append("%s=%s" % (key, postData[key]))

        listParas.append("key=%s" % (serkey))
        paraStr = "&".join(listParas)
        print("待验签字符：%s" % (paraStr))
        cryBody = self.hash_hmac(key, paraStr, sha1)
        print("密文：%s" % (cryBody))
        return cryBody

    def hash_hmac(self, key, code, sha1):
        hmac_code = hmac.new(key.encode(), code.encode(), sha1)
        return hmac_code.hexdigest()

from flask import request, abort
from response import APIBaseRequestSchema
import hmac
from hashlib import sha1


class requestValidate():
    def __init__(self, request):
        if request.content_length == 0:
            abort(401)
        postData = request.get_json()
        model= APIBaseRequestSchema().load(postData).data
        
        sign = OpenSign().CreateSign(postData, "")
        pSign = postData["Sign"]
        if pSign is not sign:
            print("签名错误：POST:%s 生成：%s" % (pSign, sign))
            abort(400)


class OpenSign():
    def __init__(self):
        pass

    def CreateSign(self, postData: "dict", key):
        keys = sorted(postData)
        listParas = []
        for key in keys:
            if key.lower() is "sign":
                continue
            listParas.append("%s=%s" % (key, postData[key]))

        listParas.append("key=%s" % (key))
        paraStr = "&".join(listParas)
        print("待验签字符：%s" % (paraStr))
        cryBody = self.hash_hmac(key, paraStr, sha1)
        print("密文：%s" % (cryBody))
        return cryBody

    def hash_hmac(self, key, code, sha1):
        hmac_code = hmac.new(key.encode(), code.encode(), sha1)
        return hmac_code.hexdigest()

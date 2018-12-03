from flask import Blueprint, request, jsonify, json, redirect, abort
from sqlalchemy import Table
from app.database import db_session, engine, metadata
from app.db_models import Func_MerchantInfo
from app.merchant.DTOMerch import DTORegisteredMerchantsRequest, DTORegisteredMerchantsRequestSchema
from app.response import BaseResponse

merchBlue = Blueprint("merch", __name__)


@merchBlue.before_app_request
def beforeRequest():
    if request.endpoint == "merch.RegisteredMerchants":
        pass
    else:
        print(request.get_json())


@merchBlue.route("/", methods=['POST'])
def RegisteredMerchants():
    model = DTORegisteredMerchantsRequestSchema().load(request.get_json()).data
    merchatModel = Table('Func_MerchantInfo', metadata, autoload=True)
    con = engine.connect()
    con.execute(merchatModel.insert(), AppId=model.AppId,
                Key=model.Key, Name=model.Name)
    return BaseResponse()
    #return request.get_json()
    #return {"N":1,"M":"MStr"}


@merchBlue.route("/qrcode", methods=['GET'])
def CreateQrCode():
    return BaseResponse()
    # return redirect('http://weixin.qq.com/q/02jYciEHOL9Y_1fhp9xscJ')

from flask import Blueprint, request, jsonify, json, redirect, abort
from sqlalchemy import Table
from app.database import dbs
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
    reqData = DTORegisteredMerchantsRequestSchema().load(request.get_json()).data
    mmodel = dbs.query(Func_MerchantInfo).filter(
        Func_MerchantInfo.AppId == reqData.AppId).one()
    if mmodel == None:
        mmodel = Func_MerchantInfo()
    mmodel.AppId = reqData.AppId
    mmodel.Key = reqData.Key
    mmodel.Name = reqData.Name
    if mmodel == None:
        dbs.add(mmodel)
    dbs.commit()
    # merchatModel = Table('Func_MerchantInfo', metadata, autoload=True)

    # merchatInfo = merchatModel.select(
    #     merchatModel.c.AppId == model.AppId).execute().first()
    # if merchatInfo == None:
    #     con = engine.connect()
    #     con.execute(merchatModel.insert(), AppId=model.AppId,
    #                 Key=model.Key, Name=model.Name)

    return BaseResponse()
    # return request.get_json()
    # return {"N":1,"M":"MStr"}


# @merchBlue.route("/qrcode", methods=['GET'])
# def CreateQrCode():
#     return BaseResponse()
#     # return redirect('http://weixin.qq.com/q/02jYciEHOL9Y_1fhp9xscJ')

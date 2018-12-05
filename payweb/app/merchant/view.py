from flask import Blueprint, request, jsonify, json, redirect, abort
from sqlalchemy import Table
from app.bllBase import *
from app.db_models import Func_MerchantInfo
from app.merchant.DTOMerch import DTORegisteredMerchantsRequest, DTORegisteredMerchantsRequestSchema
from app.response import BaseResponse
from app.requestHandler import requestValidate
from app.customError import *

merchBlue = Blueprint("merch", __name__)


@merchBlue.before_app_request
def merchbeforeRequest():
    if request.endpoint is None:
        pass
    elif "merch." in request.endpoint:
        if request.endpoint == "merch.RegisteredMerchants":
            pass
        else:
            requestValidate(request)


@merchBlue.route("/", methods=['POST'])
def RegisteredMerchants():
    reqData = DTORegisteredMerchantsRequestSchema().load(request.get_json()).data
    mmodel = DbQuery(Func_MerchantInfo).filter(
        Func_MerchantInfo.AppId == reqData.AppId, Func_MerchantInfo.MchID == reqData.MchID).first()
    isAdd = False
    if mmodel == None:
        isAdd = True
        mmodel = Func_MerchantInfo()
    if reqData.AppId is None or reqData.Key is None or reqData.Name is None or reqData.MchID is None:
        raise APIException(ErrorCode.PARA_NONE,
                           "错误的参数[AppId,Key,Name,MchID]必填")
    mmodel.AppId = reqData.AppId
    mmodel.Key = reqData.Key
    mmodel.Name = reqData.Name
    mmodel.MchID = reqData.MchID
    if isAdd:
        DbAdd(mmodel)
    else:
        DbUpdate(mmodel)
    SaveChange()

    return BaseResponse()


@merchBlue.route("/getMerInfo", methods=['POST'])
def getMerInfo():
    postData = request.get_json()
    merlist = DbQuery(Func_MerchantInfo).filter(
        Func_MerchantInfo.AppId == postData["AppId"]).all()
    rsp = []
    for item in merlist:
        rsp.append({"AppId": item.AppId,"Name": item.Name,"MchID": item.MchID})
    return rsp

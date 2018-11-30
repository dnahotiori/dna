from flask import Blueprint, request, jsonify, json,redirect,abort
from sqlalchemy import Table
from app.database import db_session, engine, metadata
from app.db_models import Func_MerchantInfo

merchBlue = Blueprint("merch", __name__)


@merchBlue.route("/", methods=['POST'])
def RegisteredMerchants():
    data = request.get_json()
    merchatModel = Table('Func_MerchantInfo', metadata, autoload=True)
    con = engine.connect()
    con.execute(merchatModel.insert(), AppId=data["AppId"],
                Key=data["Key"], Name=data["Name"])

    return jsonify(data)

@merchBlue.route("/qrcode", methods=['GET'])
def CreateQrCode():
    return "dddddd"
    #return redirect('http://weixin.qq.com/q/02jYciEHOL9Y_1fhp9xscJ')
 

from flask import Blueprint, request, jsonify,json
from sqlalchemy import Table
from app.database import db_session, engine, metadata
from app.db_models import Func_MerchantInfo

merchBlue = Blueprint("merch", __name__)


@merchBlue.route("/", methods=['POST'])
def RegisteredMerchants():
    data = request.get_json()
    try:
        merchatModel = Table('Func_MerchantInfo', metadata, autoload=True)
        con = engine.connect()
        con.execute(merchatModel.insert(), AppId=data["AppId"],
                    Key=data["Key"], Name=data["Name"])
    except Exception:
        print("错误")
    return jsonify(data)

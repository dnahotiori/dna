from flask import Blueprint

merch = Blueprint("merch", __name__)


@merch.route("/")
def RegisteredMerchants():
    return "RegisteredMerchants"

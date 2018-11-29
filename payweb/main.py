
from flask import Flask
from app.view import *
from app.merchant.view import *
from app.database import *

baseUrl = "/scancode/api/v1"
app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(merch, url_prefix=baseUrl+"/Merchant")

if __name__ == "__main__":
    app.run(host="192.168.5.9", port=8080, debug=True)

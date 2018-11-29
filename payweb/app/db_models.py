from sqlalchemy import Column, Integer, String
from database import db


class func_merchantInfo(db.Model):
    __tablename__ = "func_merchantInfo"
    id = Column(String(36), primary_key=True)
    appId = Column(String(32))
    key = Column(String(64))
    name = Column(String(128))
    def __repr__(self):
        return '<func_merchantInfo %r>' % (self.name)
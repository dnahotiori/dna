from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper
from app.database import metadata, db_session, BASE
import uuid
import time


def getId():
    return uuid.uuid1().hex


def getTime():
    SysTime = time.time()
    return int(SysTime)

class TableBase():
    ID = Column(String(36), default=getId, primary_key=True)
    CreateTime = Column(Integer, default=getTime)
    Updated = Column(Integer, default=getTime)
    IsDelete = Column(Boolean, default=True)

class Func_MerchantInfo(BASE,TableBase):
    __tablename__ = "Func_MerchantInfo"
    AppId = Column(String(32), unique=True)
    Key = Column(String(64))
    Name = Column(String(50))
    def __repr__(self):
        return '<Func_MerchantInfo %r>' % (self.AppId)

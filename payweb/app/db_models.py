from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper
from app.database import metadata, db_session
import uuid
import time

SysTime = time.time()


def getId():
    return uuid.uuid1().hex


def getTime():
    return int(SysTime)


class Func_MerchantInfo(object):
    query = db_session.query_property()

    def __init__(self, AppId=None, Key=None, Name=None):
        self.AppId = AppId
        self.Key = Key
        self.Name = Name

    def __repr__(self):
        return '<Func_MerchantInfo %r>' % (self.Name)


merchantInfo = Table('Func_MerchantInfo', metadata,
                     Column('ID', String(36), default=getId, primary_key=True),
                     Column('AppId', String(32)),
                     Column('Key', String(64)),
                     Column('Name', String(50)),
                     Column('CreateTime', Integer, default=getTime),
                     Column("Updated", Integer, default=getTime),
                     Column("IsDelete", Boolean, default=True)
                     )

mapper(Func_MerchantInfo, merchantInfo)

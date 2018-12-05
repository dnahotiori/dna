from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper
from app.database import metadata, db_session, BASE, TableBase
import app.fun_utilitys


class Func_MerchantInfo(BASE, TableBase):
    __tablename__ = "Func_MerchantInfo"
    AppId = Column(String(32))
    Key = Column(String(64))
    Name = Column(String(50))
    MchID = Column(String(32))

    def __repr__(self):
        return '<Func_MerchantInfo %r>' % (self.AppId)

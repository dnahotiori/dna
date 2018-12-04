from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from app.fun_utilitys import *


engine = create_engine(
    "mysql+pymysql://root:@localhost:3306/webapidb", max_overflow=5)
BASE = declarative_base()


metadata = MetaData()
# db_session = scoped_session(sessionmaker(
#     autocommit=True, autoflush=True, bind=engine))

db_session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
dbs = db_session()


class TableBase():
    ID = Column(String(36), default=getId, primary_key=True)
    CreateTime = Column(Integer, default=getTime)
    Updated = Column(Integer, default=getTime)
    IsDelete = Column(Boolean, default=True)


def init_db():
    import app.db_models
    BASE.metadata.create_all(bind=engine)
    # metadata.create_all(bind=engine)


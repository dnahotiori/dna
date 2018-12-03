from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "mysql+pymysql://root:@localhost:3306/webapidb", max_overflow=5)
BASE = declarative_base()


metadata = MetaData()
# db_session = scoped_session(sessionmaker(
#     autocommit=True, autoflush=True, bind=engine))

db_session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
dbs = db_session()


def init_db():
    import app.db_models
    BASE.metadata.create_all(bind=engine)
    # metadata.create_all(bind=engine)


def Commint(model):
    pass

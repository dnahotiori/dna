from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "mysql+pymysql://root:@localhost:3306/webapidb", max_overflow=5)
metadata = MetaData()
db_session = scoped_session(sessionmaker(
    autocommit=True, autoflush=True, bind=engine))


def init_db():
    import app.db_models
    metadata.create_all(bind=engine)
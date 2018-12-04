from app.database import dbs, TableBase
from app.fun_utilitys import *


def COmmintBegin():
    dbs.begin(subtransactions=True)


def DbAdd(model: "TableBase"):
    dbs.add(model)


def DbUpdate(model: "TableBase"):
    model.Updated = getTime()


def DbDelete(model: "TableBase"):
    model.Updated = getTime()
    model.IsDelete = True


def DbQuery(tableModel: "TableBase"):
    return dbs.query(tableModel)


def SaveChange():
    try:
        dbs.commit()
    except Exception as et:
        dbs.rollback()
    finally:
        if not dbs:
            dbs.close()

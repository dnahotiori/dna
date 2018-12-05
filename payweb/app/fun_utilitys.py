import uuid
import time


def getId():
    return uuid.uuid1().hex


def getTime():
    SysTime = time.time()
    return int(SysTime)

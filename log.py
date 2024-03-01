# Module

import datetime

messageLevels = ["default ","message ", "warning ", "error   ", "fatal   "]
seperator = ","

def getTimeNow() -> str:
    return str(datetime.datetime.now())

def makestring(severity, message):
    global messageLevels, seperator
    message = getTimeNow()
    message += seperator
    message += messageLevels[severity]
    message += seperator
    message += message

def log(severity: int, message: str):
    with open("data/logs", "a") as f:
        f.write(makestring(severity, message))
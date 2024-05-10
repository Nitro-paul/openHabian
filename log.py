# Module

import datetime

messageLevels = ["default","message","warning","error", "fatal"]
seperator = ",\t"

def getTimeNow() -> str:
    return str(datetime.datetime.now())

def makestring(severity, message):
    global messageLevels, seperator
    message1 = getTimeNow()
    message1 += seperator
    message1 += messageLevels[severity]
    message1 += seperator
    message1 += message
    message1 += "\n"
    return message1


def log(severity: int, message: str):
    with open("data/logs", "a") as f:
        f.write(makestring(severity, message))

def msg(message):
    log(0,message)
# Module

import log

def message(message)->None:
    log.log(1, message)

def warning(message)->None:
    log.log(2,message)

def error(message)-> None:
    log.log(3,message)

def fatal(message) -> None:
    log.log(4,message)
    print('\033[91m',f'Fatal   {message} \n quiting','\033[0m')
    exit(-1)
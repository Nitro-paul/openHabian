def testPackages():
    try:
        import ErrorHandler
    except Exception as error:
        print('\033[91m', f'Fatal   Unable to load module  ({error}) \n quiting', '\033[0m')
        exit(-1)
    try:
        import localDataGrab
    except Exception as error:
        ErrorHandler.fatal(f"unable to load module  ({error})")
    try:
        import log
    except Exception as error:
        ErrorHandler.fatal(f"unable to load module ({error})")
    try:
        import OpenHabInterface
    except Exception as error:
        ErrorHandler.fatal(f"unable to load module ({error})")
    try:
        import SettingHandler
    except Exception as error:
        ErrorHandler.fatal(f"unable to load module ({error})")
    log.msg("all packages loaded")

def testNetwork():


if __name__ == "__main__":
    testPackages()
    testNetwork()

import ErrorHandler
import SettingHandler


def read():
    path = SettingHandler.get(["LocalDataGrabber", "modprobe", "path"])
    try:
        with open(path, "r") as f:
            data = f.read()
    except Exception:
        ErrorHandler.error("modprobe outputfile not found or unable to read, using fallback data")
        data = SettingHandler.get(["LocalDataGrabber", "modprobe", "fallbackData"])
    try:
        data = int(data)
    except  Exception:
        ErrorHandler.error("data is not an integer, please check modprobe output, using fallback data")
        data = SettingHandler.get(["LocalDataGrabber", "modprobe", "fallbackData"])
    return data


def IsNew(oldData: int) -> bool:
    newData = read()
    if newData == oldData:
        return False
    else:
        return True


def get() -> int:
    return read()

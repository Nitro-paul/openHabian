# Module

import json

with open("data/settings.json", "r") as f:
    rawdata = f.read()

jdata : dict
jdata = json.loads(rawdata)

def get(path: list):
    global jdata
    upper = jdata[path[0]]
    for c, i in enumerate(path):
        if not c == 0:
            upper = upper[i]
    return upper

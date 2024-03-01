# curl -X POST --header "Content-Type: text/plain" --header "Accept: application/json" -d "test" "http://192.168.99.70:8080/rest/items/test
# curl -X POST --header "Content-Type: text/plain" --header "Accept: application/json" -d 0 "http://192.168.99.70:8080/rest/items/integerAutomatedTest"

import requests
import time

url = "http://192.168.99.70:8080/rest/items/integerAutomatedTest"

inp = input("desired Integer: ")


def requestSending(data):
    request = requests.post(
        url,
        headers={
            "Content-Type": "text/plain",
            "Accept": "applicatoin/json"
        },
        data=f'{data}'
    )


count_up = False
number = 0
for i in range(0, int(inp)):
    if i % 10 == 0:
        if count_up:
            count_up = False
        else:
            count_up = True
    if count_up:
        number += 1
    else:
        number -= 1
    num = number
    requestSending(num)
    print("set to", num)
    time.sleep(50)

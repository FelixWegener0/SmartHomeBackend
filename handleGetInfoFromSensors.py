import requests
import json
import my_time as mytime

data = json.load(open("endpoints.json"))


def getAllTempData():
    print('log get sensor data')
    result = []

    for room in data:
        temp = requests.get(room["ip"] + '/temp').json()
        humid = requests.get(room["ip"] + '/humid').json()

        result.append({
            "name": room["name"],
            "temp": temp,
            "humid": humid,
            "time": mytime.getCurrentTime(),
            "date": mytime.getCurrentDate()
        })
    print("result: ", result)
    return result

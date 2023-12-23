import requests
import json
import my_time as mytime
import Pythonlog as log

data = json.load(open("/home/pi/project/SmartHomeBackend/endpoints.json"))


def getAllTempData():
    log.info('log get sensor data')
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
    log.info("result: ", result)
    return result

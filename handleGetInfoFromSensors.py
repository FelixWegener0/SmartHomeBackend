import requests
import json
import my_time as mytime
import Pythonlog as log

# data = json.load(open("/home/pi/project/SmartHomeBackend/endpoints.json"))


def getAllTempData():
    log.info('log get sensor data')
    result = []

    temp = requests.get('http://192.168.0.187/temp').json()
    humid = requests.get('http://192.168.0.187/humid').json()

    result.append({
        "name": "Schlafzimmer",
        "temp": temp,
        "humid": humid,
        "time": mytime.getCurrentTime(),
        "date": mytime.getCurrentDate()
    })
    log.info(f"result: {result}")

    return result

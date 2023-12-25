import requests
import json
import my_time as mytime
import Pythonlog as log

data = [
    {
        "name": "Schlafzimmer",
        "ip": "192.168.0.187"
    }
]


def getAllTempData():
    log.info('log get sensor data')
    result = []

    for sensor in data:
        temp = requests.get(f'http://{sensor["ip"]}/temp').json()
        humid = requests.get(f'http://{sensor["ip"]}/humid').json()

        result.append({
            "name": sensor["name"],
            "temp": temp,
            "humid": humid,
            "time": mytime.getCurrentTime(),
            "date": mytime.getCurrentDate()
        })
    log.info(f"result: {result}")
    return result

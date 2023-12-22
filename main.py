import threading
import RESTapi as Restapi
import handleDatabaseInteractions as database

from time import sleep


def collectSensorData():
    print('start collectSensorData as deaon')
    while (True):
        database.loopWriteToDB()
        sleep(900)


thraedSensorData = threading.Thread(target=collectSensorData, daemon=True)
threadRestApi = threading.Thread(target=Restapi.runServer, daemon=True)

if (__name__ == "__main__"):
    threadRestApi.start()
    thraedSensorData.start()

    while (True):
        sleep(100000)
        pass

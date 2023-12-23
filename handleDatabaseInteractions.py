import handleGetInfoFromSensors as apiInput
import database_main as db
import Pythonlog as log

database = db.connectToDatabse()
cursor = db.connectCursor(database)


def writeDataToDatabase(data):
    log.info('write new Data to database data: ', data)
    db.addDataBySQL(
        cursor, database, "INSERT INTO TempData(date, time, temperature, humidity, name) VALUES (?, ?, ?, ?, ?)", (data["date"], data["time"], data["temp"], data["humid"], data["name"]))


def getAllData():
    result = db.getDataBySQL(cursor, "SELECT * FROM TempData")
    return result


def loopWriteToDB():
    log.info('log loopWriteToDatabase')
    data = apiInput.getAllTempData()
    for info in data:
        writeDataToDatabase(info)

import handleGetInfoFromSensors as apiInput
import database_main as db

database = db.connectToDatabse()
cursor = db.connectCursor(database)


def writeDataToDatabase(data):
    db.addDataBySQL(
        cursor, database, "INSERT INTO TempData(date, time, temperature, humidity, name) VALUES (?, ?, ?, ?, ?)", (data["date"], data["time"], data["temp"], data["humid"], data["name"]))


def getAllData():
    result = db.getDataBySQL(cursor, "SELECT * FROM TempData")
    return result


def loopWriteToDB():
    print('log loopWriteToDatabase')
    data = apiInput.getAllTempData()
    for info in data:
        writeDataToDatabase(info)

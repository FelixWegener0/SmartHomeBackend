import handleGetInfoFromSensors as apiInput
import database_main as db
import Pythonlog as log
import my_time as my_time

database = db.connectToDatabse()
cursor = db.connectCursor(database)


def writeDataToDatabase(data):
    log.info(f'write new Data to database data: {data}')
    db.addDataBySQL(
        cursor, database, "INSERT INTO TempData(date, time, temperature, humidity, name) VALUES (?, ?, ?, ?, ?)", (data["date"], data["time"], data["temp"], data["humid"], data["name"]))


def getAllData():
    result = db.getDataBySQL(cursor, "SELECT * FROM TempData")
    return result


def getAllTodaysData():
    result = db.getDataBySQL(
        cursor, f"SELECT * FROM TempData WHERE date = '{my_time.getCurrentDate()}'")
    return result


def getAllTodaysDataForRoom(room, allData):
    if (allData):
        result = db.getDataBySQL(
            cursor, f"SELECT * FROM TempData WHERE date = '{my_time.getCurrentDate()}' AND name = '{room}'")
        return result
    else:
        result = db.getDataBySQL(
            cursor, f"SELECT * FROM TempData WHERE name = '{room}'")
        return result


def loopWriteToDB():
    log.info('log loopWriteToDatabase')
    data = apiInput.getAllTempData()
    for info in data:
        writeDataToDatabase(info)

import sqlite3


def connectToDatabse():
    return sqlite3.connect("backendData.db", check_same_thread=False)


def connectCursor(database):
    return database.cursor()


def getDataBySQL(cursor, sql):
    cursor.execute(sql)
    return cursor.fetchall()


def addDataBySQL(cursor, database, sql, var):
    cursor.execute(sql, var)
    database.commit()


def databseColseConnect(database):
    database.close()

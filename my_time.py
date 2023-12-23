from datetime import date, datetime


def getCurrentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def getCurrentDate():
    return date.today()

# call this file once to Initialize the database
import sqlite3

con = sqlite3.connect("backendData.db")

cur = con.cursor()

cur.execute(
    "create table TempData(date date, time timestamp, temperature real, humidity real, name string)")
con.commit()

con.close()

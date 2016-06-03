#!/usr/bin/python3.5
import sqlite3


uId = input("Enter record Id: ")

con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", {"Id": uId})
    con.commit()
    row = cur.fetchone()
    print(row[0], row[1])

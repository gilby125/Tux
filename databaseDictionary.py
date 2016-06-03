#!/bin/python3.5

import sqlite3
con = sqlite3.connect('test.db')    

with con:
    con.row_factory = sqlite3.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print (row["Id"], row["Name"], row["Price"])

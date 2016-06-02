#!/usr/bin/python3.5

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break

        print row.__type__
        # print("%s %s %i") % row[0] % row[1] % row[2]

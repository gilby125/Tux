#!/bin/python3.5
import sqlite3
import sys

con = None

try:
	con = sqlite3.connect('test.db')
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')

	data = cur.fetchone()

	print("SQLITE version %s" % data)

except sqlite3.Error:
	print("Error %s" % e.args[0])
	sys.exit(1)

finally:

	if con:
		con.close()

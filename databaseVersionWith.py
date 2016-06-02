#!/usr/bin/python3.5

import sqlite3
import sys

con = lite.connect('test.db')

with con:

	cur = con.cursor()
	cur.execute('SELECT SQULITE_VERSION()')

	data = cur.fetchone()

	print "SQLite version %s" % data

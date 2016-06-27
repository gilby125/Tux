# tux_database
# Ryan Gavigan
# 06/26/16
import sqlite3 as sql
from contextlib import closing


con = None
try:
	con = sql.connect('tux.db')
	cur = con.cursor()
except sql.Error:
	file = open('tux.db','w+')
	con = sql.connect('tux.db')
	cur = con.cursor()
	print("ln 16: TEST")

try:
	cur.execute('SELECT * FROM tux.sqlite_master WHERE type = "table";')
	print("ln 19: TEST")
	data = cur.fetchall()
	print(data)
except sql.OperationalError:
	cur.executescript("""
					CREATE TABLE Events(EventId INT, EventType TEXT, EventDate);
					CREATE TABLE Types(Abbv TEXT, Full TEXT);
					INSERT INTO Types VALUES('IO','Input Okay');
					INSERT INTO Types VALUES('IF', 'Input Fail');
					INSERT INTO Types Values('RO','RSS Okay');
					INSERT INTO Types Values('RF','RSS Fail');
					INSERT INTO Types Values('EO','Email Okay');
					INSERT INTO Types Values('EF','Email Fail');
					""")
finally:
	cur.close()

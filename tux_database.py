# tux_database
# Ryan Gavigan
# 06/29/16
import random
import sqlite3 as sql
from contextlib import closing


def dbConnect():
	'''
	Any database accesses with require this series of try/excepts
	'''
	con = None
	try:
		con = sql.connect('tux.db')
		cur = con.cursor()
	except sql.Error:
		file = open('tux.db', 'w+')
		con = sql.connect('tux.db')
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
	return con


def insertEvent(table, eventType, dt):
	if(eventType not in ['IO', 'IF', 'RO', 'RF', 'EO', 'EF']):
		print("That event type is not valid.")
		return insertEvent("IO", dt)
	if(dt is None):
		dt = datetime.d
	con = dbConnect()
        id = 0
        while(True):
                id = random.random()
                keys = cur.execute('SELECT * FROM table WHERE EventId = id')
                if(id not in keys):
                        break
        cur = con.cursor()
        cur.execute("INSERT INTO table VALUES(id, eventType, dt)")
	con.close()

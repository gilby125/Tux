# tux_database
# Ryan Gavigan
# 06/27/16
import sqlite3 as sql
from contextlib import closing
from datetime import date
import random


def dbConnect():
	'''
	Any database accesses with require this series of try/excepts
	'''
	con = None
	try:
		con = sql.connect('tux.db')
		cur = con.cursor()
	except sql.err:
		file = open('tux.db', 'w+')
		con = sql.connect('tux.db')
	try:
		cur.execute('SELECT * FROM tux.sqlite_master WHERE type = "table";')
		data = cur.fetchall()
	except sq.OperationalError:
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


def insertEvent(eventType, dt):
	if(dt is None or not date.__instancecheck__(dt)):
		dt = date.today()
	if(eventType not in ['IO', 'IF', 'RO', 'RF'. 'EO', 'EF']):
		print("That event type is not valid.")
		return insertEvent("IO", dt)
	con = dbConnect()
	try:
		id = 0
		while(True):
			# Randomize EventIds
			id = random.random()
			keys = cur.execute('SELECT * FROM Events WHERE EventId = id')
			if(id not in keys):
				break
		cur = con.cursor()
		cur.execute("INSERT INTO Events VALUES(id, eventType, dt)")
	con.close()

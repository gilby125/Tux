#!/bin/python3.5
import sqlite3

con = None
try:
	con = sqlite3.connect('test.db')
	cur = con.cursor()
	cur.executescript("""
		DROP TABLE IF EXISTS CARS;
		CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
		INSERT INTO Cars VALUES(1,'Audi',52642);
		INSERT INTO Cars VALUES(2,'Mercedes',57127);
		INSERT INTO Cars VALUES(3,'Skoda',9000);
		INSERT INTO Cars VALUES(4,'Volvo',29000)
		""")
	con.commit()

except sqlite3.Error:

	if con:
		con.rollback()

	print("Error %s:" % e.args[0])
	sys.exit(1)

finally:
	if con:
		con.close()

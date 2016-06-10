#!/bin/python

import sqlite3


con = None

try:
	con = sqlite3.connect('test.db')
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')

	data = cur.fechone()

	print("SQLITE version %s" % data)

except sqlite3.Error:
	print("Error %s" % sqlite3.Error.args[0])


def main():
	print("DATABASE")

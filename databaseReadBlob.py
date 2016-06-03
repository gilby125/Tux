#!/usr/bin/python3.5

import sqlite3
import sys


def writeImage(data):
	try:
		fout = open('ebayLogo.png', 'wb')
		fout.write(data)

	except IOError:
		print("Error %d: %s" % IOError.args[0], IOError.args[1])
		sys.exit(1)

	finally:

		if fout:
			fout.close()


con = sqlite3.connect('test.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT Data FROM Images LIMIT 1")
	data = cur.fetchone()[0]
	writeImage(data)

	con.commit()

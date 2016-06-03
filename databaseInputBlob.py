#!/usr/bin/python3.5
import sqlite3
import urllib.request
import sys

# url string data type
url = "http://p.ebaystatic.com/aw/pics/globalheader/spr11.png"
fname = "ebayLogo.png"

urllib.request.urlretrieve(url, fname)


def readImage():
	try:
		fin = open("ebayLogo.png", "rb")
		img = fin.read()
		return img

	except IOError:
		print("Error %d: %s" % IOError.args[0], IOError.args[1])
		sys.exit(1)

	finally:
		if fin:
			fin.close()

	con = sqlite3.connect('test.db')

	with con:
		cur = con.cursor()
		data = readImage()
		binary = sqlite3.Binary(data)
		cur.execute("DROP TABLE IF EXISTS Images")
		cur.execute("CREATE TABLE Images(Data BLOB)")
		cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,))

		con.commit()

# tux_database
# Ryan Gavigan
# 06/20/16
import sqlite3 as sql

con = None

try:
    con = sql.connect('tux.db')
except sql.Error:
	file = open('tux.db','w+')
	con = sql.connect('tux.db')

try:
    cur = con.cursor()
	print((cur.description()))
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fechone()
    print("SQLITE version %s" % data)

except sqlite3.Error:
    print("Error %s" % sqlite3.Error.args[0])

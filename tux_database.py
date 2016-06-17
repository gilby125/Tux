import sqlite3


con = None
try:
    con = sqlite3.connect('tux.db')
    cur = con.cursor()
	print((cur.description()))
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fechone()
    print("SQLITE version %s" % data)

except sqlite3.Error:
    print("Error %s" % sqlite3.Error.args[0])

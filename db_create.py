import sqlite3

conn = sqlite3.connect('test.db')

def create():
	conn.execute('''CREATE TABLE TELEMETRY
	       (ID INT PRIMARY KEY     NOT NULL,
	       TYPE           TEXT    NOT NULL,
	       ITEM        CHAR(50));
	       ''')

	conn.close()

def write(table, values):
    """ Execute an Insert SQL Query. """
    sql = "INSERT INTO ? VALUES (?, ?, ?, ?, ?);".format(table, values)
	conn.cursor().execute(sql)
	conn.commit()

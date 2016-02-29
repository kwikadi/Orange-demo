import sqlite3

connection = sqlite3.connect('test.db', check_same_thread=False)

def create():
	con.execute('''CREATE TABLE TELEMETRY
	       (ID INT	PRIMARY KEY	NOT NULL,
	       TYPE	CHAR(50)	NOT NULL,
	       ITEM	CHAR(50));
	       ''')

	con.close()

def write(con, values):
	""" Execute an Insert SQL Query. """
	sql = "INSERT INTO TELEMETRY VALUES (?, ?, ?);"
	con.cursor().execute(sql, (1, values[0], values[1]))
	con.commit()

if __name__ == '__main__':
	create()

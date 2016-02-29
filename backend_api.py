from flask import Flask, request
import database as db

app = Flask(__name__)


@app.route('/data', methods=['POST'])
def button():
	# read POSTed data
	ttype = request.form.get('type')
	titem = request.form.get('item')
	print(ttype,titem)
	print ('Telemetry data recieved')
	# Send to DB
	db.write(db.connection, (ttype, titem))
	return ""

if __name__ == '__main__':
	app.run(debug = True)

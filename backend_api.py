from flask import Flask
import db_store
app = Flask(__name__)

@app.route('/button')
def button():
	# read POSTed data
	print ('Telemetry-button')
	db_store.write()
	return 'Hello button'

@app.route('/menu')
def menu():
	# read POSTed data
	print ('Telemetry-menu')
	db_store.write('TELEMETRY', 'menu')
	return 'Hello menu'

if __name__ == '__main__':
	app.run(debug = True)

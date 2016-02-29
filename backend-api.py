from flask import Flask
app = Flask(__name__)

@app.route('/button')
def button():
    print ('Telemetry-button')
    return 'Hello button'

@app.route('/menu')
def menu():
    print ('Telemetry-menu')
    return 'Hello menu'

if __name__ == '__main__':
    app.run(debug = True)

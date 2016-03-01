#Telemetry demo

##Running information

1. Create venv
2. pip install -r requirements.txt

```

python database.py # creates the initial database

python backend_api.py # sets up the webserver to accept data

python client_app.py # an example app with telemetry data being sent to the webserver

```

After backend_api.py and client_app.py are running (database.py will create the DB and stop running), Clicking on any of the buttons or menu options will send the data over to the webserver. Note that several features (such as non blocking server calls, and batched requests) have not been implemented since this is just a 'prototype' at best. Code shows where a few other features (ex: github issue creation) will exist within the codebase.

![Running Demo Screenshot](/telemetry.png)

from flask import Flask, g
from flaskext.mongoalchemy import MongoAlchemy
from gridFsFileStore import GridFsFileStore

db = MongoAlchemy()
fs = None

def create_app(config, enable_frontend=True):
	app = Flask(__name__)
	app.config["MONGOALCHEMY_DATABASE"] = config["APP_DB_NAME"]

	try:
		db.init_app(app)
	except:
		print "Unable to connect to MongoDB. Make sure your connection settings are correct and that the server is running"

	from api import api
	from frontend import frontend

	app.register_blueprint(api)

	if enable_frontend:
		app.register_blueprint(frontend)
	
	return app

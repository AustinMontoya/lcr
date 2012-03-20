from flask import Flask
from flask.ext.pymongo import PyMongo
from gridFsFileStore import GridFsFileStore

mongo = PyMongo()
fs = None

def create_app(config, enable_frontend=True):
	app = Flask(__name__)
	app.config.from_object(config)

	mongo.init_app(app)

	from api import api
	from frontend import frontend

	app.register_blueprint(api)

	if enable_frontend:
		app.register_blueprint(frontend)
	
	return app

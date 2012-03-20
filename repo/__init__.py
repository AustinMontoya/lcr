from flask import Flask, g
from flaskext.mongoalchemy import MongoAlchemy
from gridFsFileStore import GridFsFileStore

db = MongoAlchemy()
fs = None

def create_app(config, enable_frontend=True):
	app = Flask(__name__)
	app.config.from_object(config)

	db.init_app(app)

	from api import api
	from frontend import frontend

	app.register_blueprint(api)

	if enable_frontend:
		app.register_blueprint(frontend)
	
	return app

from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy
from gridFsFileStore import GridFsFileStore
from settings import config

fs = None
if config["FS_TYPE"] == 'gridfs':
	fs = GridFsFileStore(config["APP_DB_NAME"], config["DB_HOST"], config["DB_PORT"])
else:
	raise Exception("No FileStore specified!")

app = Flask(__name__)

app.config["MONGOALCHEMY_DATABASE"] = config["APP_DB_NAME"]
db = MongoAlchemy(app)

import repo.views
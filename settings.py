class Config():
	FS_TYPE = 'gridfs'
	MONGO_HOST = '127.0.0.1'
	MONGO_PORT = 27017
	
class DevConfig(Config):
	DEBUG = True
	MONGO_DBNAME = 'scorm-repo'

class TestConfig(Config):
	TESTING = True
	DEBUG = False
	MONGO_DBNAME = 'test-repo'
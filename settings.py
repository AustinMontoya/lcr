class Config():
	DB_TYPE = 'mongodb'
	FS_TYPE = 'gridfs'
	DB_HOST = '127.0.0.1'
	DB_PORT = 27017
	
class DevConfig(Config):
	DEBUG = True
	MONGOALCHEMY_DATABASE = 'scorm-repo'

class TestConfig(Config):
	TESTING = True
	DEBUG = False
	MONGOALCHEMY_DATABASE = 'test-repo'
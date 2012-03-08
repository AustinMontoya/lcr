from abc import ABCMeta, abstractmethod

class MetadataStore:
	__metaclass__ = ABCMeta

	def __init__(self, dbHost, dbPort, user=None, password=None):
		self.dbHost = dbHost
		self.dbPort = dbPort
		self.user = user
		self.password = password

	@abstractmethod
	def setCollection(self, collectionName):
		pass

	@abstractmethod
	def create(self, val):
		pass

	@abstractmethod
	def read(self, id):
		pass

	@abstractmethod
	def update(self, val):
		pass

	@abstractmethod
	def delete(self, val):
		pass

class FileStore:
	__metaclass__ = ABCMeta

	def __init__(self):
		pass

	@abstractmethod
	def getFile(self, fileId):
		pass

	@abstractmethod
	def setFile(self, stream, fileId):
		pass

	@abstractmethod
	def deleteFile(self, fileId):
		pass
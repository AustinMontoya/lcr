from datastore import FileStore
from pymongo import Connection
import gridfs

class GridFsFileStore(FileStore):

	def __init__(self, dbName, mongoHost='127.0.0.1', mongoPort=27017):
		FileStore.__init__(self)
		self.connection = Connection(mongoHost, mongoPort)
		self.__gridfs = gridfs.GridFS(self.connection[dbName])

	def getFile(self, fileId):
		return self.__gridfs.get(fileId).read()

	def setFile(self, file):
		return self.__gridfs.put(file.read())

	def deleteFile(self, fileId):
		return self.__gridfs.delete(fileId)
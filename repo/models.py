from repo import db, fs

class Resource(db.Document):
	id = db.ObjectIdField(required=True)
	name = db.StringField(required=True, min_length=3)
	type = db.EnumField(db.StringField(), "file", "resource")

class FileResource(Resource):
	gridFsId = db.ObjectIdField(required=True)

	def getData(self):
		return fs.getFile(self.gridFsId)

	def setData(self, data):
		self.gridFsId = fs.setFile(data)

class WebResource(Resource):
	url = db.StringField(required=True, min_length=5)

class LearningObject(db.Document):
	id = db.ObjectIdField(required=True)
	title = db.StringField(min_length=3, max_length=50, required=True)
	description = db.StringField(max_length=140, required=False)
	tags = db.ListField(db.StringField(), required=False)
	files = db.ListField(db.DocumentField(Resource), min_capacity=1)
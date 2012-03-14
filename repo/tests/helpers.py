def _make_todo_document(db):
    class Todo(db.Document):
        description = db.StringField()
    return Todo

def _make_LCR_Resource(db):
	class Resource(db.Document):
		id = db.ObjectIdField(required=True)
		name = db.StringField(required=True, min_length=3)
		type = db.EnumField(db.StringField(), "file", "resource")
	return Resource

def _make_LCR_Object(db):	
	class LCR_Object(db.Document):
		id = db.ObjectIdField(required=True)
		title = db.StringField(min_length=3, max_length=50, required=True)
		description = db.StringField(max_length=140, required=False)
		tags = db.ListField(db.StringField(), required=False)
		files = db.ListField(db.DocumentField( _make_LCR_Resource(db)), min_capacity=1)
	return LCR_Object
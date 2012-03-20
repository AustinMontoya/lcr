function LearningObject(data) {

	// Data
	var self = this;

	self.id = ko.observable();
	self.title = ko.observable();
	self.description = ko.observable();
	self.tags = ko.observable("");
	self.resources = ko.observableArray();
	self.errors = ko.observableArray([]);
	self.metadata = ko.computed(function() {
		return {
			"title": self.title(),
			"description" : self.description(),
			"tags" : self.tags().split(',')
		}
	});

	
	// Behaviors
	self.validate = function() {
		var newErrors = [];
		if(!self.title() || self.title() == "")
			newErrors.push("Title is required.");
		if(self.description() && self.description().length > 140)
			newErrors.push("Description cannot exceed 140 characters.");
		if(self.resources().length < 1)
			newErrors.push("At least one resource must be included to upload.")

		var hasResourceErrors = false;
		for(var i=0; i < self.resources().length; i++)
			hasResourceErrors = !self.resources()[i].validate();

		self.errors(newErrors);
		return self.errors().length === 0 && !hasResourceErrors;
	}

	self.load = function(data) {
		self.id(data.id);
		self.title(data.title);
		self.description(data.description);
		self.tags(data.tags.join(','));

		if(data.resources) {
			for (var id in data.resources) {
				$.get('/api/resource/'+id+"?metadata=true", function(resourceMetadata) {
					self.resources.push(new Resource(item));
				});
			}
		}	
	}
}

function Resource(data) {
	// Data 
	var self = this;
	var id = data && data.id ? data.id : null,
		resourceId = data && data.resourceId ? data.resourceId : "",
		name = data && data.name ? data.name : "",
		type = data && data.type ? data.type : "file";

	self.id = ko.observable();
	self.name = ko.observable(name);
	self.currentFileValue = ko.observable();
	self.currentUrlValue = ko.observable();
	self.type = ko.observable(type);
	self.errors = ko.observableArray();

	self.errorList = ko.computed(function(){
		var html = "<ul class='error-container'>";
		for(var i =0; i < self.errors().length; i++)
			html += "<li>"+self.errors()[i]+"</li>";
		return html+"</ul>";
	});

	self.locator = ko.computed(function() {
		return "http://"+location.host+"/api/resource/"+self.id();
	});

	// Behaviors
	self.validate = function() {
		self.errors([]);
		if((self.type() == "file" && !self.currentFileValue())
			|| (self.type() == "url" && !self.currentUrlValue())) {
			self.errors.push(self.type()+" cannot be empty");
			return false;
		}
		return true;
	}
}
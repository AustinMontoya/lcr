function LearningObject(data) {

	// Data
	var self = this;

	self.id = null;
	self.title = ko.observable();
	self.description = ko.observable();
	self.tags = ko.observable("");
	self.resources = ko.observableArray();

	if(data && data.resources) {
		for (var id in data.resources) {
			$.get('/api/resource/'+id+"?metadata=true", function(resourceMetadata) {
				self.resources.push(new Resource(item));
			});
		}
	}
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
		self.id = data.id;
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

	self.id = id;
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
		return "http://"+location.host+"/api/resource/"+self.id;
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

function CreateAndEditViewModel() {
	var self = this;
	self.resourceTypes = ["url", "file"];
	self.modes = ["create", "update"];
	self.resourceDeleteQueue = [];
	self.notification = ko.observable();

	// Behaviors
	self.addResource = function() {
		self.learningObject.resources.push(new Resource({ type: "file" }))
	};
	self.removeResource = function(resource) { 
		if(resource.id)
			self.resourceDeleteQueue.push(resource.id);

		self.learningObject.resources.remove(resource);
	}

	self.saveContent = function() {
		var onSuccess = function(data) {
			if(self.mode == "create") {
				self.learningObject.id = data.id;
				self.mode = "update";
			}
			self.showStatusBox("Learning Content package saved successfully.", 
						  		"success-container");
		}

		var onError = function(xhr) {
			self.showStatusBox(JSON.parse(xhr.responseText).error,
								"error-container");
		}

		if(self.learningObject.validate()) {
			var url = "/api/"+self.mode+"/content";
			if(self.mode === "update")
				url += "/"+self.learningObject.id;

			$.ajax(url, {
				contentType: 'application/json',
				type: "POST", 
				processData: false,
				data: JSON.stringify(self.learningObject.metadata()),
				success: onSuccess,
				error: onError
			});
		}
	}

	self.showStatusBox = function(msg, className) {
		self.notification(msg);
		$("statusBox")
			.attr("class", className)
			.show();
	}

	// Client-side routing
	Sammy(function() {
		this.get('/edit/:id', function() {
			self.learningObject = new LearningObject();
			$.get('/api/content/'+this.params['id'], function(data) {
				self.mode = 'update';
				self.learningObject.load(data);
				self.resources = self.learningObject.resources();
			})
			.error(function() { window.location = '/404' });
		});
		this.get('/create', function() {
			self.mode = 'create';
			self.learningObject = new LearningObject();
			self.resources = self.learningObject.resources();
		});
	}).run();
}
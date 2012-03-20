function CreateAndEditViewModel() {
	var self = this;
	self.resourceTypes = ["url", "file"];
	self.mode = ko.observable('create');
	self.resourceDeleteQueue = [];
	self.notification = ko.observable();

	// Behaviors
	self.addResource = function() {
		self.learningObject.resources.push(new Resource({ type: "file" }))
	};
	self.removeResource = function(resource) { 
		if(resource.id())
			self.resourceDeleteQueue.push(resource.id());

		self.learningObject.resources.remove(resource);
	}

	self.saveContent = function() {
		var onSuccess = function(data) {
			if(self.mode() === "create") {
				self.learningObject.id(data.id);
				self.mode("update");
			}
			self.showStatusBox("Learning Content package saved successfully.", 
						  		"success-container");
		}

		if(self.learningObject.validate()) {
			var url = "/api/"+self.mode()+"/content";
			if(self.mode() === "update")
				url += "/"+self.learningObject.id();

			$.ajax(url, {
				contentType: 'application/json',
				type: "POST", 
				processData: false,
				data: JSON.stringify(self.learningObject.metadata()),
				success: onSuccess
			});
		}
	};

	self.deleteContent = function(){
		var confirmed = confirm("Are you sure you want to delete this Learning Content? "+
								"All associated resources willl be deleted, and this action "+
								"cannot be undone.");
		if(confirmed) {
			$.post("/api/delete/content/"+self.learningObject.id(), function(){
				window.location = '/';
			});
		}
	};

	self.showStatusBox = function(msg, className) {
		self.notification(msg);
		$("statusBox")
			.attr("class", className)
			.show();
	};

	// General error handling
	$(document).ajaxError(function(event, jqXhr){
		var msg;
		try { msg = JSON.parse(jqXhr.responseText).error; } 
		catch(e) { msg = jqXhr.responseText; }
		self.showStatusBox(msg,"error-container");
	});

	// Client-side routing
	Sammy(function() {
		this.get('/edit/:id', function() {
			self.learningObject = new LearningObject();
			$.get('/api/content/'+this.params['id'], function(data) {
				self.mode('update');
				self.learningObject.load(data);
				self.resources = self.learningObject.resources();
			});
		});
		this.get('/create', function() {
			self.learningObject = new LearningObject();
			self.resources = self.learningObject.resources();
		});
	}).run();
}
function CreateAndEditViewModel() {
	var self = this;
	self.resourceTypes = ["url", "file"];
	self.mode = ko.observable('create');
	self.resourceDeleteQueue = [];
	self.notification = ko.observable();

	// Behaviors
	self.addResource = function() {
		self.learningPackage.resources.push(new Resource({ type: "file" }))
	};
	self.removeResource = function(resource) { 
		if(resource.id())
			self.resourceDeleteQueue.push(resource.id());

		self.learningPackage.resources.remove(resource);
	}

	self.saveContent = function() {
		var onSuccess = function(data) {
			if(self.mode() === "create") {
				self.learningPackage.id(data.id);
				self.mode("update");
			}
			self.showStatusBox("Learning Package saved successfully.", 
						  		"success-container");
		}

		if(self.learningPackage.validate()) {
			var url = "/api/"+self.mode()+"/package";
			if(self.mode() === "update")
				url += "/"+self.learningPackage.id();

			$.ajax(url, {
				contentType: 'application/json',
				type: "POST", 
				processData: false,
				data: JSON.stringify(self.learningPackage.metadata()),
				success: onSuccess
			});
		}
	};

	self.deleteContent = function(){
		var confirmed = confirm("Are you sure you want to delete this Learning Package? "+
								"All associated resources willl be deleted, and this action "+
								"cannot be undone.");
		if(confirmed) {
			$.post("/api/delete/package/"+self.learningPackage.id(), function(){
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
			self.learningPackage = new LearningPackage();
			$.get('/api/package/'+this.params['id'], function(data) {
				self.mode('update');
				self.learningPackage.load(data);
				self.resources = self.learningPackage.resources();
			});
		});
		this.get('/create', function() {
			self.learningPackage = new LearningPackage();
			self.resources = self.learningPackage.resources();
		});
	}).run();
}
function CreateAndEditViewModel() {
	var self = this;
	self.resourceTypes = ["url", "file"];
	self.mode = ko.observable('create');
	self.resourceDeleteQueue = [];
	self.notification = ko.observable();

	// Behaviors
	self.addResource = function() {
		self.learningPackage.resources.push(new Resource({ type: "file" }));
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
			self.saveResources();
			self.showStatusBox("Learning Package saved successfully.", 
						  		"success");
		}

		if(self.learningPackage.validate()) {
			var url = "/api/"+self.mode()+"/package";
			if(self.mode() === "update")
				url += "/"+self.learningPackage.id();

			$.ajax(url, {
				data: JSON.stringify(self.learningPackage.metadata()),
				success: onSuccess
			});
		}
	};

	self.saveResources = function() {
		var saveResource = function(resource, container) {
			function assignId(data) {
				if(!resource.id())
					resource.id(data.id);
			}

			var action = (!resource.id()) ? "create" : "update",
				url = "/api/" + action 
					+ "/package/" + self.learningPackage.id()
					+ "/resource";

			if(action == "update") {
				console.log("resourceId: "+resource.id())
				url += "/"+resource.id();
			}

			var qs = "?",
				vals = [],
				metadata = resource.metadata();

			for(var prop in metadata)
				vals.push(prop+"="+metadata[prop]);
			qs += vals.join('&');

			url += qs;

			if(resource.type() == "url") {
				$.ajax(url, {
					data: JSON.stringify({ url: resource.currentUrlValue() }),
					success: assignId
				});
			} else {
				var $form = $(container).find("form"),
					$progress = $(container).siblings(".status");

				// Use the FormData object if supported by the browser
				if (window.FormData) {
					formData = new FormData($form.get(0));

					var xhr = new XMLHttpRequest();
					xhr.open("POST", url, false);

					xhr.onload = function(event) { 
						if(xhr.status == 200) {
							$progress.text("done!");
							resource.id(JSON.parse(xhr.responseText).id); 
						} else 
							$progress.text("An error occurred while uploading.")
					};

					xhr.upload.onprogress = function (event) {
						if(event.lengthComputable) {
							var pct = (event.loaded / event.total) * 100;
							$progress.text(pct+"%");
						} else
							console.log("WTFmate");
					};

					xhr.send(formData);

				} else //Otherwise use disgusting iframe method
					fileUpload_noprogress(form, url, function(e){
						console.log("this happened")
					});
			}
		}

		var elems = $("#resourcesTable tr .input-container");
		for(var i = 0; i < elems.length; i++) 
			saveResource(self.learningPackage.resources()[i], elems[i]);
	}

	self.deleteContent = function() {
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
		$statusBox = $("#statusBox");
		var heading = className.charAt(0).toUpperCase() + className.slice(1)

		$statusBox
			.find(".alert-heading").text(heading);

		$statusBox
			.attr("class", "alert alert-"+className)
			.show();
	};

	// Default ajax settings
	$.ajaxSetup({
		contentType: 'application/json',
		type: "POST", 
		processData: false
	})

	// General error handling
	$(document).ajaxError(function(event, jqXhr){
		var msg;
		try { msg = JSON.parse(jqXhr.responseText).error; } 
		catch(e) { msg = jqXhr.responseText; }
		self.showStatusBox(msg,"error");
	});

	// Client-side routing
	Sammy(function() {
		this.get('/edit/:id', function() {
			self.learningPackage = new LearningPackage();
			self.learningPackage.load(this.params['id'], function(data) {
				self.mode('update');
				self.resources = self.learningPackage.resources();
			});
		});
		this.get('/create', function() {
			self.learningPackage = new LearningPackage();
			self.resources = self.learningPackage.resources();
		});
	}).run();
}

function fileUpload_noprogress(form, action_url, onLoadCallback) {

    // Create the iframe...
    var iframe = document.createElement("iframe");
    iframe.setAttribute("id", "upload_iframe");
    iframe.setAttribute("name", "upload_iframe");
    iframe.setAttribute("width", "0");
    iframe.setAttribute("height", "0");
    iframe.setAttribute("border", "0");
    iframe.setAttribute("style", "width: 0; height: 0; border: none;");
 
    // Add to document...
    form.parentNode.appendChild(iframe);
    window.frames['upload_iframe'].name = "upload_iframe";
 
    var iframeId = document.getElementById("upload_iframe");
 
    if (iframeId.attachEvent) iframeId.attachEvent("onload", onLoadCallback);
 
    // Set properties of form...
    form.setAttribute("target", "upload_iframe");
    form.setAttribute("action", action_url);
    form.setAttribute("method", "post");
    form.setAttribute("enctype", "multipart/form-data");
    form.setAttribute("encoding", "multipart/form-data");
 
    // Submit the form...
    form.submit();
}
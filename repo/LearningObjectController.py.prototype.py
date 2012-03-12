def LearningObjectController:
	def handleRequest(action, requestBody):
		if action == "add":
			# Input: 
			# {
			#	title: <string>,
			#   description: <string>|null
			#	tags: <string>|null
			# }
			#
			# Output:
			# Success:
			# { id: LearningObject.id }
			# Error:
			# { error: ErrorMessage }
			pass
		elif action == "addWebResource":
			# Input
			# [{
			# 	TODO
			# }]
			pass
		elif action == "files":
			# if input is none, return ids
			# if input is id, return the file
			# if input is file, then store the file     
			# Input
			# {
			#	
			# }
		elif action is None:
			# /object/id
			# Output
			# JSON object	

import urllib
import urllib2
import json

url = "http://localhost:5000/api/create/content?multi=true"
#values = [{ "title": "Birds of Prey",
#    		"description": "Lesson on all kinds of birds",
#    		"tags": ["eagle", "falcon"] }, { "title": "Birds of Prey",
#    		"description": "Lesson on all kinds of birds",
#    		"tags": ["eagle", "falcon"] }]
values = { "title": "Birds of Prey",
    		"description": "Lesson on all kinds of birds",
    		"tags": ["eagle", "falcon"] }

req = urllib2.Request(url, json.dumps(values))
req.add_header('content-type', 'application/json')
response = urllib2.urlopen(req)
print response.read()
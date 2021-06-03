import json
import os
import sys

class JSONPopulator:
		
	sample = """
	[
   {
      "datestamp":"2000-06-28",
      "plans":[
         {
            "added":"2000-06-28",
            "body":"Birthday"
         }
      ]
   }
]
"""

	@staticmethod
	def write(data):
		encoded = json.loads(data)
		with open("calendar.json", "w+") as f:
			json.dump(encoded, f, indent=4)

	@staticmethod
	def read():
		path = ""
		if sys.platform.startswith('win'):
			path = os.path.normpath(os.getcwd()) + '\\calendar.json'
		elif sys.platform.startswith('darwin'):
			path = os.path.normpath(os.getcwd()) + '/calendar.json'
		elif sys.platform.startswith('linux'):
			path = os.path.normpath(os.getcwd()) + '/calendar.json'

		mode = 'r' if os.path.exists(path) else 'w'
		with open("calendar.json", f"{mode}") as f:
			try:
				data = json.load(f)
			except:
				data = json.loads(JSONPopulator.sample)
		return data

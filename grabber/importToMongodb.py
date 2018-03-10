from os import listdir
from os.path import isfile, join
from pymongo import MongoClient
import json
from GoogleNlpClassifier import GoogleNlpClassifier as gnc

client = MongoClient('localhost', 27017)
db = client['dataex']
collection = db['datasets']

#remove all of the old records
collection.remove() 
path="data"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('json')]
classifier = gnc()

for file in onlyfiles:
	with open(join(path, file)) as json_data:
		print("importing %s"%file)
		data = json.load(json_data)
		try:
			categories = classifier.process('{}. {}'.format(data['name'], data['notes']))
			category = [c.name for c in categories]
			data['categories']=category
			print(data)
			id = collection.insert_one(data)
			print("inserted: %s"%id)
		except Exception as err:
			print(u"error processing {}".format(data['name']))
			print(err)
		
		
from os import listdir
from os.path import isfile, join

class DatatypeClassifier:
	'''
	returns the data types in a dataset based on the 
	'''
	def classify(self, datajson, dataseturl):
		with open(dataseturl) as file:
			line = file.readline()
			if line.find('city')!=-1 and line.find('state')!=-1:
				print("found location info in {}".format(dataseturl))
				# print(line)


def main():
	filelist = [f for f in listdir('dat') if isfile(join('dat', f))]
	classifier = DatatypeClassifier()
	#classifier.classify("", join('dat', 'data154.json'))
	for file in filelist:
		classifier.classify('', join('dat', file))

if __name__ == '__main__':
	main()

if __name__ == '__main__':
	main()
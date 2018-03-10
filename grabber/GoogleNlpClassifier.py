from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

class GoogleNlpClassifier:
	api_key = 'AIzaSyCHAExm2iofgvIQG8dS-Ax6Ki1MioIDe24'
	client = language.LanguageServiceClient()

	def process(self, text):
		document = types.Document(
			content=text,
			type=enums.Document.Type.PLAIN_TEXT)
		categories = self.client.classify_text(document=document).categories
		print('Text: {}'.format(text))
		for category in categories:
			print('Category: {}, {}'.format(category.name, category.confidence))
		return categories

def main() :
	classifier = GoogleNlpClassifier()
	classifier.process('The Department of State keeps a record of every filing for every incorporated business in the state of New York. This dataset contains information on all active')

if __name__ == '__main__':
	main()
import scrapy
import pprint
import json

class DataSourceFinder(scrapy.Spider):
    name = 'datasetspider'
    start_urls = ['https://catalog.data.gov/dataset']
    count=1
    def parse(self, response):
        for dataset in response.css('div.dataset-content'):
            dataset_name = dataset.css('h3.dataset-heading').xpath('a/text()').extract_first()
            dataset_url = dataset.css('ul.dataset-resources').xpath('li/a/@href').extract_first()
            dataset_format = dataset.css('ul.dataset-resources').xpath('li/a/@data-format').extract_first()
            dataset_notes = dataset.css('div.notes').xpath('div/text()').extract_first()
            if dataset_format in set(["csv", "json", "zip"]):
                filename='data/data%d.json'%self.count
                with open(filename, 'w') as outfile:
                    item = {"name": dataset_name, "url": dataset_url, "notes": dataset_notes, "format": dataset_format}
                    json.dump(item, outfile)
                    print json.dumps(item)
                    self.count+=1

    			#yield item

        for next_page in response.css('div.pagination').xpath('ul/li/a'):
            yield response.follow(next_page, self.parse)

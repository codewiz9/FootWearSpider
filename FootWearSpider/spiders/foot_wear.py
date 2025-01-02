import scrapy
import json

class FootWearSpider(scrapy.Spider):
    name = "foot_wear"
    #x is the ammount of response on each page 
    x = 30
    start_urls = [f"https://rulings.cbp.gov/api/search?term=foot%20wear&collection=ALL&pageSize={x}&page=1&sortBy=RELEVANCE"]

    def parse(self, response):
        data = json.loads(response.body)
        id_nums = data['rulings']
        list_of_ids = []
        for ruling in id_nums:
            list_of_ids.append(ruling['rulingNumber'])
        
        for i in list_of_ids:
            url = f'https://rulings.cbp.gov/api/ruling/{i}?textToHighlight=foot%20wear'
            yield scrapy.Request(url, callback=self.parse_ruling)

        
    def parse_ruling(self, response):
        #data = json.loads(response.body)
        yield{
            'data': response.body
        }

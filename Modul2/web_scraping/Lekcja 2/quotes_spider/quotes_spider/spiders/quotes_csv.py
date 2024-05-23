import scrapy


'''
Uruchomienie scrapera:
scrapy crawl quotes -o quotes.csv
'''

class QuotesSpiderCSV(scrapy.Spider):
    name = 'quotestwo'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        page_number = response.meta.get('page_number', 1)

        # Scrapowanie listy elementów (wszystkie cytaty na stronie)
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()').get()
            author = quote.xpath('.//small[@class="author"]/text()').get()
            tags = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            yield {
                'text': text,
                'author': author,
                'tags': ', '.join(tags),
                'page_number': page_number
            }

        # Scrapowanie z paginacją - przejście do następnej strony
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            next_page_number = page_number + 1
            yield response.follow(next_page, self.parse, meta={'page_number': next_page_number})

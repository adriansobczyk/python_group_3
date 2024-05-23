import scrapy

'''
Uruchomienie scrapera:
scrapy crawl quotes -o quotes.json
'''

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies={'currency': 'USD'}, callback=self.parse)

    def parse(self, response):
        page_number = response.meta.get('page_number', 1)

        # Scrapowanie pojedynczego elementu
        single_quote = response.xpath('//div[@class="quote"]/span[@class="text"]/text()').get()
        self.log(f'Single quote: {single_quote}')

        # Scrapowanie listy elementów (wszystkie cytaty na stronie)
        quotes = response.xpath('//div[@class="quote"]/span[@class="text"]/text()').getall()
        for quote in quotes:
            yield {
                'quote': quote,
                'page_number': page_number
            }

        # Scrapowanie konkretnych atrybutów (autorzy cytatów)
        authors = response.xpath('//div[@class="quote"]/span/small[@class="author"]/text()').getall()
        for author in authors:
            yield {
                'author': author,
                'page_number': page_number
            }

        # Scrapowanie elementów z atrybutami HTML (linki do szczegółów autora)
        author_links = response.xpath('//div[@class="quote"]/span/a/@href').getall()
        for link in author_links:
            yield {
                'author_link': response.urljoin(link),
                'page_number': page_number
            }

        # Scrapowanie z paginacją - przejście do następnej strony
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            next_page_number = page_number + 1
            yield response.follow(next_page, self.parse, meta={'page_number': next_page_number})

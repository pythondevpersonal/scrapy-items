import scrapy

from ..items import GeeksItem


class SampleSpider(scrapy.Spider):
    name = 'sample'
    allowed_domains = ['quotes.toscrape.com/tag/reading/']
    start_urls = ['http://quotes.toscrape.com/tag/reading//']

    def parse(self, response):
         # Fetch all quotes tags
        item = GeeksItem()
        quotes = response.xpath('//*[@class="quote"]')
         
        # Loop through the Quote selector elements
        # to get details of each
        for quote in quotes:
             
            # XPath expression to fetch text of the Quote title
            item['quotetitle'] = quote.xpath('.//*[@class="text"]/text()').extract_first()
             
            # XPath expression to fetch author of the Quote
            item['author'] = quote.xpath('.//*[@itemprop="author"]/text()').extract()
             
            # XPath expression to fetch Tags of the Quote
            item['tags'] = quote.xpath('.//*[@itemprop="keywords"]/@content').extract()
             
            # Yield all elements
            yield item

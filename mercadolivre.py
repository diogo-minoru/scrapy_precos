import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/busca/smart+tv+4k/"]

    def parse(self, response):
        pass

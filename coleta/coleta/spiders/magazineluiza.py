import scrapy


class MagazineluizaSpider(scrapy.Spider):
    name = "magazineluiza"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/busca/smart+tv+4k/"]

    def parse(self, response):
        produtos = response.css('h2.sc-gQSkpc.iWaBVz')
        
        for produto in produtos:
            yield{
                'nome_produto': produto.css('h2.sc-gQSkpc.iWaBVz::text').get()
            }
#scrapy crawl magazineluiza -o data.jsonl
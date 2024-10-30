import scrapy


class MagazineluizaSpider(scrapy.Spider):
    name = "magazineluiza"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/busca/smart+tv+4k/"]

    def parse(self, response):
        produtos = response.css('li.sc-fTyFcS.iTkWie')
        
        for produto in produtos:
            yield{
                'nome_produto': produto.css('h2.sc-gQSkpc.iWaBVz::text').get(),
                'preco_prazo': produto.css('p.sc-dcJsrY.dpUJi.sc-bdOgaJ.gYMJkM::text').get(),
                'preco_pix': produto.css('p.sc-dcJsrY.eLxcFM.sc-eHsDsR.eGPZvr::text').get()
            }
#scrapy crawl magazineluiza -o data.jsonl
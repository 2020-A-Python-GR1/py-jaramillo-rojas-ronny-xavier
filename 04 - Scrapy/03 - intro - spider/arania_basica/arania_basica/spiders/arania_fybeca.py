import scrapy
class IntroSpider(scrapy.Spider):
    name = 'spider_fybeca'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'ul.products-list > li.product-tile'
        )
        titulos = etiqueta_contenedora.css(
            'div.product-tile-inner > div.detail > div.side > div.price-member > div::attr(data-bind)'
        ).extract()
        print('#####################ETIQUETA###################')
        print(titulos)
        precios = []
        for item in titulos
            precios.append(item.split(''))
        #Producto mas caro y mas barato
        #Cuanto se ahorra si se compra como afiliado todo
        
    
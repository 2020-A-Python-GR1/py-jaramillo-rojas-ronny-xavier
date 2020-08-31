import scrapy
class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        #Precio
        print('############PRECIO############')
        precio_c = response.css('div.product_price')
        precio_n = precio_c.css('p.price_color::text').extract()
        print(precio_n)
        final = []
        for item in precio_n:
                final.append(item.replace('£',''))
        print(final)
        #Stock
        print('############STOCK############')
        stock = precio_c.css('p.instock::text').extract()
        print(stock)
        #Imagen
        print('############IMAGEN############')
        img_cont = etiqueta_contenedora.css('div.image_container')
        img = img_cont.css('a > img::attr(src)').extract()
        print(img)
        #Estrellas
        print('############ESTRELLAS############')
        estrellas = response.css('p.star-rating').extract()
        for i in estrellas:
            print(i.partition('\n')[0].split('rating')[1].split('\"')[0])
    #
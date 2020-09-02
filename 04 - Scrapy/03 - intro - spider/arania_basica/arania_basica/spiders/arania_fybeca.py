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
        etiqueta_contenedora = response.css('div.product-tile-inner')
        #Producto mas caro y mas barato
        #Cuanto se ahorra si se compra como afiliado todo
        productos = list(etiqueta_contenedora.css("a.name::text").extract())
        print("######Productos######")
        print(productos)
        imgs = list(etiqueta_contenedora.css(
            "div.detail > a.image > img#gImg.productImage::attr(src)"
        ).extract())
        print("######Imagenes######")
        print(imgs)
        p_original = etiqueta_contenedora.css(
            "div.detail > div.side > div.price::attr(data-bind)"
        ).extract()
        print("######Original######")
        print(p_original)
        p_original_clean = []
        for i in p_original:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            p_original_clean.append(precio) 
        print(p_original_clean)
        print("Más caro original:"+ str(max(p_original_clean)))
        print("Más barato original:"+ str(min(p_original_clean)))
        print("Suma Original: "+str(sum(p_original_clean)))
        p_afiliado = list(etiqueta_contenedora.css(
            "div.detail > div.side > div.price-member > div::attr(data-bind)"
        ).extract())
        print("######Afiliado######")
        print(p_afiliado)
        p_afiliado_clean = []
        for i in p_afiliado:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            p_afiliado_clean.append(precio)
        print(p_afiliado_clean)
        print("Más caro para afiliados:"+ str(max(p_afiliado_clean)))
        print("Más barato para afiliados:"+ str(min(p_afiliado_clean)))
        print("Suma Afiliado: "+str(sum(p_afiliado_clean)))
        print("Ahorro  total: "+str(sum(p_original_clean) - sum(p_afiliado_clean)))

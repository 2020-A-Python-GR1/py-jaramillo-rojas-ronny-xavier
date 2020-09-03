import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class AraniaCrawlFybeca(CrawlSpider):
    name  = 'crawl_fybeca' #Heredado
    #Categoría: Belleza
    #Cabello -> cat=446
    #Manicure y Pedicure -> cat=627
    #Cuidado de la piel -> cat=489
    #Maquillaje -> cat=537
    #Perfumes y Colonas -> cat=558 (Solo hay 15 productos en esta categoría)
    #Lencería -> cat=562
    #Producto por sección -> pp=5000
    cats = ['446','627','489','537','558','562']
    allowed_domains = ['fybeca.com']
    urls_permitidos = []
    i_urls = []
    for item in cats:
        i_urls.append('https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat='+item+'&s=0&pp=5000')
        urls_permitidos.append('search-results.jsf\?cat='+item+'&s=0&pp=5000')
    start_urls = i_urls
    #start_urls = ['https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=25']
    #No se detectan las páginas con 5000 productos si se usa el LinExtractor(allow)
    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = urls_permitidos
            ),
            callback = 'parse_page'
        ),
    )
    rules = regla_dos
    total_afiliado = 0
    total_original = 0
    def parse_page(self,response):
        #Productos
        etiqueta_contenedora = response.css('div.product-tile-inner')
        productos = list(etiqueta_contenedora.css("a.name::text").extract())
        print(productos)
        for producto in productos:
            with open('titulos_productos_belleza.txt','a+',encoding='utf-8') as archivo:
                archivo.write(producto + '\n')
        #Precio Original
        p_original = etiqueta_contenedora.css(
            "div.detail > div.side > div.price::attr(data-bind)"
        ).extract()
        p_original_clean = []
        for i in p_original:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            p_original_clean.append(precio) 
        for po in p_original_clean:
            with open('precios_originales_belleza.txt','+a',encoding='utf-8') as archivo:
                archivo.write(str(po) + '\n')
        with open('total_originales_categoria.txt','+a',encoding='utf-8') as archivo:
                archivo.write(str(response.css('div.breadcrumb > a:nth-child(2)::text').extract()[0]) + '\n')
                archivo.write(("Más caro original:"+ str(max(p_original_clean)) + '\n'))
                archivo.write(("Más barato original:"+ str(min(p_original_clean)) + '\n'))
                archivo.write(("Suma Original: "+str(sum(p_original_clean)) + '\n'))
        #Precio Afiliado
        p_afiliado = list(etiqueta_contenedora.css(
            "div.detail > div.side > div.price-member > div::attr(data-bind)"
        ).extract())
        p_afiliado_clean = []
        for i in p_afiliado:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            p_afiliado_clean.append(precio)
        for pa in p_afiliado_clean:
            with open('precios_afiliados_belleza.txt','+a',encoding='utf-8') as archivo:
                archivo.write(str(pa) + '\n')
        with open('total_afiliados_categoria.txt','+a',encoding='utf-8') as archivo:
                archivo.write(str(response.css('div.breadcrumb > a:nth-child(2)::text').extract()[0]) + '\n')
                archivo.write(("Más caro afiliado:"+ str(max(p_afiliado_clean)) + '\n'))
                archivo.write(("Más barato afiliado:"+ str(min(p_afiliado_clean)) + '\n'))
                archivo.write(("Suma afiliado: "+str(sum(p_afiliado_clean)) + '\n'))
        self.total_afiliado = self.total_afiliado + sum(p_afiliado_clean)
        self.total_original = self.total_original + sum(p_original_clean)
    def closed( self, reason ):
        print("Total gasto afiliado: "+ str(self.total_afiliado))
        print("Total gasto no afiliado: " + str(self.total_original))
        print("Total ahorro: " + str(self.total_original - self.total_afiliado))




import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class AraniaCrowlOnu(CrawlSpider):
    name  = 'crawl_onu' #Heredado
    
    allowed_domains = [ #Heredado
        'un.org'
    ]
    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]
    
    regla_uno = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' #Nombre de función a ejecutar para parsear
        ),
    )
    rules = regla_uno #Heredada
    segmentos_url_permitidos = (
        'funds-programmes-specialized-agencies-and-others'
    )
    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ),
            callback = 'parse_page'
        ),
        #Parametro Vacío
    )
    rules = regla_dos
    segmentos_restringidos = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos,
                deny = segmentos_restringidos
            ),
            callback = 'parse_page'
        ),
    )
    rules = regla_tres
    def parse_page(self,response):
        lista_programas_onu = response.css(
            "div.content > div.field-type-text-with-summary > div.field-items > div.field-item > h4::text"
        ).extract()
        print(lista_programas_onu)
        for agencia in lista_programas_onu:
            with open('onu_agencias.txt','a+',encoding = 'utf-8') as archivo:
                archivo.write(agencia + '\n')
    
    #Con fybeca
    #Obtener todos los productos de las subcategorías de Belleza (menos Marcas).
    #Sacar el total de afiliado/original y el ahorro considerando todos los productos sacados por todas las categorias.
    #Utilizando esta araña.
    #Cambiar la url para que se muestren al menos 5000 productos.
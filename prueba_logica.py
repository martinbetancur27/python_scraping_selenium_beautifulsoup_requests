from scraper_web_static_or_dynamic import Scraper

if __name__ == "__main__":
    
    #Instanciar la clase
    scraper = Scraper()

    #Prueba sitio web dinamico
    '''scraper.scraper_dynamic_page("https://finance.yahoo.com")
    attribute = scraper.get_attribute_by_tag("a", "href")
    print(len(attribute))
    print(attribute)'''
    
    #Prueba sitio web estatico
    #Obtener valor de atributo de una etiqueta
    '''scraper.scraper_static_page("https://www.dataquest.io")
    articles = scraper.get_attribute_all_tag('a', "href")
    print(len(articles))
    print(articles)'''

    #Ejecutar el metodo find_all del modulo BeautifulSoup
    '''scraper.scraper_static_page("https://www.dataquest.io")
    articles = scraper.bs_find_all('a')
    print(len(articles))
    print(articles)'''

    #Obtener el contendio de la etiqueta
    '''scraper.scraper_static_page("https://www.thoughtco.com/quotes-and-sayings-from-cervantes-3079523#:~:text=Cervantes%20Quotes%20About%20Living%20Wisely,reading%20much%20sharpens%20one's%20ingenuity.)")
    contents = scraper.get_content_tag("em")
    for content in contents:
        print(content)'''
    
    #Obtener el contendio de la etiqueta (mediante metodo explicito de BS)
    '''scraper.scraper_static_page("https://www.thoughtco.com/quotes-and-sayings-from-cervantes-3079523#:~:text=Cervantes%20Quotes%20About%20Living%20Wisely,reading%20much%20sharpens%20one's%20ingenuity.)")
    contents = scraper.bs_find_all_get_text("em")
    for content in contents:
        print(content)'''

    
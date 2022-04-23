class ScraperStaticPage():

    def __init__(self, page) -> None:
        self.page = page
        self.scraper_static_page()


    def scraper_static_page(self):
        #Recibe Url
        #Obtener pagina por medio de requests. 
            #Enviar el resultado al metodo __beautifulsoup_connect
        #No retorna ningun valor

        try:
            page_source = requests.get(self.page)
            self = BeautifulSoupPersonalized()
            self.__beautifulsoup_connect(page_source.text)
        except:
            print("Error al realizar el scraping sobre web estatica. \n Revise su URL o intente con modulo scraper-dynamic-page")
import requests
from beautiful_soup import BeautifulSoupPersonalized

class ScraperStaticPage(BeautifulSoupPersonalized):

    def __init__(self, page_url):
        
        page_result = self.scraper_static_page(page_url)
        super().__init__(page_result.text)
        
        #self.__beautifulsoup_connect(page_result)


    def scraper_static_page(self, page_url):
        #Recibe Url
        #Obtener pagina por medio de requests. 
            #Enviar el resultado al metodo __beautifulsoup_connect
        #No retorna ningun valor

        try:
            return requests.get(page_url)
        except:
            print("Error al realizar el scraping sobre web estatica. \n Revise su URL o intente con modulo scraper-dynamic-page")
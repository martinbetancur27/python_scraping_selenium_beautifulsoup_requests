import requests
from beautiful_soup import BeautifulSoupPersonalized
#beautiful_soup modulo del programa

class ScraperStaticPage(BeautifulSoupPersonalized):

    #Esta clase heredara los metodos de la clase BeautifulSoupPersonalized
            #Heredara los metodos para la busqueda
            
    def __init__(self, page_url):
        
        page_result = self.scraper_static_page(page_url)
        #super().__init__ Inicializar el constructor de la superclase
        super().__init__(page_result.text)


    def scraper_static_page(self, page_url):
        #Recibe Url
        #Obtener pagina por medio de requests.
        #retorna el resultado de la peticion http.

        try:
            return requests.get(page_url)
        except:
            print("Error al realizar el scraping sobre web estática. \n Revise su URL o intente con el método de página dinámica")
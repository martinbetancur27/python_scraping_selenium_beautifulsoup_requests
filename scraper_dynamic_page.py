#Modulo propio del programa
from beautiful_soup import BeautifulSoupPersonalized

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import time

class ScraperDynamicPage(BeautifulSoupPersonalized):

    def __init__(self, page_url):
        
        page_result = self.scraper_dynamic_page(page_url)
        super().__init__(page_result)

    
    def __connect_browser(self, page):
        #No recibe ningun parametro
        #Hace la conexion con el webdriver de Chrome.
        #No retorna ningun valor

        '''ChromeDriver es un ejecutable separado que Selenium WebDriver usa para controlar Chrome. 
        Lo mantiene el equipo de Chromium con la ayuda de los colaboradores de WebDriver.
        https://chromedriver.chromium.org/getting-started
        
        Selenium admite la automatización de todos los principales navegadores del mercado mediante el uso de WebDriver
        WebDriver es una API y un protocolo que define una interfaz independiente del idioma para controlar el 
        comportamiento de los navegadores web. Cada navegador está respaldado por una implementación específica de WebDriver, 
        llamada controlador. https://www.selenium.dev/documentation/webdriver/getting_started/'''
        try:
            #Ocultar el navegador
            self.options = ChromeOptions()
            self.options.headless = True

            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
            self.driver.get(page)
        except:
            print("Error al conectar el driver del navegador")


    def scraper_dynamic_page(self, page):
        #Recibe Url
        #Ejecutar metodo __connect_browser()
            #Obtener la pagina por medio del driver de Selenium. 
            #Hacer scroll 'infinito' y con tiempo de pausa para
            #permtir que se cargue todo el contenido. 
            #Sincrónicamente ejecuta JavaScript en la ventana/marco actual
            #obtenemos el código html interno del cuerpo. 
            #Enviar el resultado al metodo __beautifulsoup_connect
            #Sale del controlador y cierra todas las ventanas asociadas.
        #No retorna ningun valor
        try:
            self.__connect_browser(page)
            self.__slow_scroll()     
            body = self.driver.execute_script("return document.body")
            page_source = body.get_attribute('innerHTML') 
            self.driver.quit()
            return page_source
        except:
            print("Error al realizar el scraping sobre web dinamica. Revise su URL")

    
    def __slow_scroll(self):
        #No recibe parametro
        #Controlar el scroll de la pagina por medio una accion de Javascript y Selenium
        #No retorna ninguno valor
        try:

            #Deslizamiento pausado (1 segundo) para permitir que el contenido se cargue (sitios dinamicos).
            #Permite el scroll "infinito"
            ###### PRUEBAS CON EL SITIO: https://finance.yahoo.com
            # Este resultado trajo mas o menos 3 veces que el realizado con el metodo estatico.
            #TENER EN CUENTA: XPATH del navegador (CARGADO COMPLETAMENTE) trae mas datos sin embargo este metodo 
            #trae una cantidad relativamente cerca.
            
            #FUENTE DEL CODIGO: https://blogvisionarios.com/e-learning/articulos-data/web-scraping-de-paginas-dinamicas-con-selenium-python-y-beautifulsoup-en-azure-data-studio/
            print("Por favor esperar... La pagina puede ser muy extensa")
            self.driver.maximize_window()
            time.sleep(1)
            #We make a slow scroll to the end of the page
            iter=1
            while True:
                scrollHeight = self.driver.execute_script("return document.documentElement.scrollHeight")
                Height=250*iter
                self.driver.execute_script("window.scrollTo(0, " + str(Height) + ");")
                if Height > scrollHeight:
                    print('End of page')
                    break
                time.sleep(1)
                iter+=1
        except:
            print("Error al realizar el scroll dinamico")
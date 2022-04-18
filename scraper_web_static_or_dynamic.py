import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import time

class Scraper():

    def connect_browser(self):
        '''Ocultar el navegador (sin cabecera)'''
        self.options = ChromeOptions()
        self.options.headless = True

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        #El anterior comando se reemplazo por comando -> driver =  Chrome(executable_path='chromedriver.exe')


    def scraper_dynamic_page(self, page):

        self.connect_browser()
        self.driver.get(page)
        self.slow_scroll()

        #we get the internal html code of the body        
        body = self.driver.execute_script("return document.body")
        source = body.get_attribute('innerHTML') 
        self.soup = BeautifulSoup(source, "html.parser")

    
    def scraper_static_page(self, page):

        #self.connect_browser()
        page_scraping = requests.get(page)
        #self.driver.get(page)
        #self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.soup = BeautifulSoup(page_scraping.text, 'html.parser')
        

    def scraping_all_tag(self, tag):

        return self.soup.find_all(tag)
        #return self.soup.findAll(tag)
        

    def slow_scroll(self):

        #** Deslizamiento pausado (1 segundo) para permitir que el contenido se cargue (sitios dinamicos)
        #** El resultado trajo alrededor de 3 veces mas que el realizado con el metodo estatico. Quedo cerca al 
        # XPATH del navegador.
        #*FUENTE: https://blogvisionarios.com/e-learning/articulos-data/web-scraping-de-paginas-dinamicas-con-selenium-python-y-beautifulsoup-en-azure-data-studio/

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
    

    def get_attribute(self, scraping_tag, tag_attribute):
        list_attribute = []
        for elem in scraping_tag:
            if elem.has_attr(tag_attribute):
                list_attribute.append(elem[tag_attribute])
        
        return list_attribute
        

    def exit_browser(self):
        self.driver.quit()


if __name__ == "__main__":


    #Prueba sitio web estatico
    '''scraper = Scraper()
    scraper.scraper_static_page("https://www.dataquest.io")
    articles = scraper.scraping_all_tag('a')
    print(len(articles))
    attribute = scraper.get_attribute(articles, "href")
    print(attribute)'''

    #Prueba sitio web dinamico
    
    '''scraper = Scraper()
    scraper.scraper_dynamic_page("https://finance.yahoo.com")
    articles = scraper.scraping_all_tag('a')
    print(len(articles))
    attribute = scraper.get_attribute(articles, "href")
    print(attribute)
    scraper.exit_browser()'''
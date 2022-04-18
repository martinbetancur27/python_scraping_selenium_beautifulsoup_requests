import requests
from lxml import etree
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
        #El anterior comando se reemplazo por el comando -> driver =  Chrome(executable_path='chromedriver.exe')


    def scraper_dynamic_page(self, page):

        self.connect_browser()
        self.driver.get(page)
        self.slow_scroll()

        #we get the internal html code of the body        
        body = self.driver.execute_script("return document.body")
        page_source = body.get_attribute('innerHTML') 
        self.beautifulsoup_connect(page_source)

    
    def scraper_static_page(self, page):

        page_source = requests.get(page)
        self.beautifulsoup_connect(page_source.text)

    def beautifulsoup_connect(self, page_source):
        self.soup = BeautifulSoup(page_source, 'html.parser')


    def scraping_all_tag(self, tag):

        return self.soup.find_all(tag)
        

    def slow_scroll(self):

        #** Deslizamiento pausado (1 segundo) para permitir que el contenido se cargue (sitios dinamicos).
        #Permite el scroll "infinito"
        
        ###### PRUEBAS CON EL SITIO: https://finance.yahoo.com
        # Este resultado trajo mas o menos 3 veces que el realizado con el metodo estatico.
        #TENER EN CUENTA: XPATH del navegador (CARGADO COMPLETAMENTE) trae mas datos sin embargo este metodo 
        #trae una cantidad relativamente cerca.
        
        #FUENTE DEL CODIGO: https://blogvisionarios.com/e-learning/articulos-data/web-scraping-de-paginas-dinamicas-con-selenium-python-y-beautifulsoup-en-azure-data-studio/

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
    

    def get_by_attribute(self, scraping_tag, tag_attribute):
        list_attribute = []
        for elem in scraping_tag:
            if elem.has_attr(tag_attribute):
                list_attribute.append(elem[tag_attribute])
        
        return list_attribute


    def get_by_xpath(self, var_xpath):

        dom = etree.HTML(str(self.soup))
        return dom.xpath(var_xpath)


    def exit_browser(self):
        self.driver.quit()


#El siguiente codigo es implementado para probar logica del programa
if __name__ == "__main__":

    #Prueba sitio web estatico
    '''scraper = Scraper()
    scraper.scraper_static_page("https://www.dataquest.io")
    articles = scraper.scraping_all_tag('a')
    print(len(articles))
    attribute = scraper.get_by_attribute(articles, "href")
    print(attribute)'''

    #Prueba sitio web dinamico
    
    '''scraper = Scraper()
    scraper.scraper_dynamic_page("https://finance.yahoo.com")
    articles = scraper.scraping_all_tag('a')
    print(len(articles))
    attribute = scraper.get_by_attribute(articles, "href")
    scraper.exit_browser()'''
    
    #Prueba de expresion XPATH en sitio web dinamico
    '''scraper = Scraper()
    scraper.scraper_dynamic_page("https://finance.yahoo.com")
    attribute = scraper.get_by_xpath('//div[contains(@class,"C(#959595)")]/span[1][starts-with(.,"Bloomberg")]/../..//a/@href')
    print(len(attribute))
    print(attribute)

    scraper.exit_browser()'''
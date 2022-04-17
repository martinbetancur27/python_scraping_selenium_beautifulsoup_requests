
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions

import time

class Scraper():

    def __init__(self, page):
        self.page = page

    def connect_browser(self):
        '''se puede ocultar el navegador (sin cabecera)'''
        self.options = ChromeOptions()
        self.options.headless = True

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        #El siguiente comando se reemplazo por el anterior comando
        #driver =  Chrome(executable_path='chromedriver.exe')

    def scraper_page(self):

        self.connect_browser()
        self.driver.get(self.page)
        self.slow_scroll()

        #we get the internal html code of the body        
        body = self.driver.execute_script("return document.body")
        source = body.get_attribute('innerHTML') 
        self.soup = BeautifulSoup(source, "html.parser")
        

    def scraping_all_tag(self, tag):
        #******************** SCRAPING SELENIUM *********************
        #Scrapin con Selenium
        #trajo 210 pero en la web se traen 319.
        '''articles = driver.find_elements(By.TAG_NAME, 'a')
        print(len(articles))
        for elem in articles:
            print(elem.get_attribute("href"))'''

        #*********************** SCRAPING BEAUTIFULSOUP *********************
        #scraping con BS - No hay diferencia con Selenium. Trar una cantidad similar.
        '''soup = BeautifulSoup(driver.page_source, 'lxml')
        articles = soup.find_all('a')

        print(len(articles))
        for elem in articles:
            print(elem["href"])'''

        return self.soup.find_all(tag)
        

    def slow_scroll(self):

        #** Deslizamiento pausado (1 segundo) para permitir que el contenido se cargue (yahoo funciona asi)
        #** El resultado trajo alrededor de 3 veces mas contenido. Quedo cerca al XPATH del
        #** navegador. 
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
    

    def exit_browser(self):
        self.driver.quit()


if __name__ == "__main__":

    scraper = Scraper('https://finance.yahoo.com')

    scraper.scraper_page()
    articles = scraper.scraping_all_tag('a')

    print(len(articles))

    for elem in articles:
        print(elem["href"])
    
    scraper.exit_browser()

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions

'''se puede ocultar el navegador (sin cabecera)'''
options = ChromeOptions()
options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#El siguiente comando se reemplazo por el anterior comando
#driver =  Chrome(executable_path='chromedriver.exe')

driver.get('https://finance.yahoo.com')



#******************** SCRAPING SELENIUM *********************
#Scrapin con Selenium
#trajo 210 pero en la web se traen 319.
articles = driver.find_elements(By.TAG_NAME, 'a')
print(len(articles))
for elem in articles:
    print(elem.get_attribute("href"))

#*********************** SCRAPING BEAUTIFULSOUP *********************
#scraping con BS - No hay diferencia con Selenium. Trar una cantidad similar.
'''soup = BeautifulSoup(driver.page_source, 'lxml')
articles = soup.find_all('a')

print(len(articles))
for elem in articles:
    print(elem["href"])'''

driver.quit()
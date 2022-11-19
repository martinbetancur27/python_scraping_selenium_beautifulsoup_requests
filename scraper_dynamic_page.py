from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import time

class ScraperDynamicPage:

    def __init__(self, page_url):

        self.page_url = page_url
       
    
    def __connect_browser(self):
        
        #It makes the connection with the Chrome webdriver.
        #Return driver Selenium

        '''ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome.
        It is maintained by the Chromium team with the help of WebDriver contributors.
        https://chromedriver.chromium.org/getting-started
        
        Selenium supports automation of all major browsers on the market by using WebDriver.
        WebDriver is an API and protocol that defines a language-independent interface for controlling the behavior of web browsers. 
        Each browser is backed by a specific implementation of WebDriver, called controller. 
        https://www.selenium.dev/documentation/webdriver/getting_started/'''

        try:
            #Hide the browser
            my_options = ChromeOptions()
            my_options.headless = True
            #Hide unnecessary logs from the user
            my_options.add_argument("--log-level=3")

            #Each WebDriver instance provides automated control over a browser session.
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=my_options)
            driver.get(self.page_url)
            #if the above piece of code doesn't break set the connection to true
            self.__connect = True
            return driver

        except:
            print("Error connecting browser driver. Check the url\n")
            self.__connect = False


    def scraper_page(self):
        #Url (Constructor)
            #Make scroll 'infinite' and with pause time for
            #allow all content to be loaded.
            #Synchronously run JavaScript in the current window/frame
            # get the internal html code of the body.
            #Send the result to the __beautifulsoup_connect method
            #Exit the controller and close all associated windows.
         #Does not return any value
        try:
            self.__browser_driver_by_selenium = self.__connect_browser()

            if (self.__connect):
                self.__slow_scroll()     
                body = self.__browser_driver_by_selenium.execute_script("return document.body")
                page_source = body.get_attribute('innerHTML') 
                self.__browser_driver_by_selenium.quit()
                return page_source
        except:
            print("Error when performing scraping on dynamic web")
            return None

    
    def __slow_scroll(self):
        #Does not receive parameter
        #Control page scrolling through a Javascript and Selenium action
        #Does not return any value
        try:

            #Scroll paused (1 second) to allow content to load (dynamic sites).
            #Allow "infinite" scroll
            ###### TESTS WITH THE SITE: https://finance.yahoo.com
            # This result brought more or less 3 times than the one obtained with the static method.
            #PLEASE NOTE: Browser XPATH (FULLY LOADED) brings more data however this method
            #brings a relatively close amount.
            
            #CODE SOURCE: https://blogvisionarios.com/e-learning/articulos-data/web-scraping-de-paginas-dinamicas-con-selenium-python-y-beautifulsoup-en-azure-data-studio/
            print("Please wait... The page can be very long")
            self.__browser_driver_by_selenium.maximize_window()
            time.sleep(1)
            #We make a slow scroll to the end of the page
            iter = 1
            while True:
                scrollHeight = self.__browser_driver_by_selenium.execute_script("return document.documentElement.scrollHeight")
                Height = 250 * iter
                self.__browser_driver_by_selenium.execute_script("window.scrollTo(0, " + str(Height) + ");")
                if Height > scrollHeight:
                    print("Scroll finished, please wait")
                    break
                time.sleep(1)
                iter += 1
        except:
            print("Error when performing dynamic scroll")
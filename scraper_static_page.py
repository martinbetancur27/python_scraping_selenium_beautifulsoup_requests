import requests
from beautiful_soup import BeautifulSoupPersonalized
#beautiful_soup program module

class ScraperStaticPage(BeautifulSoupPersonalized):

    #This class inherits the methods of the BeautifulSoupPersonalized class.
            #Inherit methods for lookup
            
    def __init__(self, page_url):

        #connect: connection validation
        self.connect = False
        page_result = self.scraper_static_page(page_url)

        if(self.connect):
            #super().__init__ Initialize the constructor of the superclass
            super().__init__(page_result.text)


    def scraper_static_page(self, page_url):
        #Receive Url
        #Get page through requests.
        #returns the result of the http request.

        try:
            page = requests.get(page_url)
            #if the above piece of code doesn't break set the connection to true
            self.connect = True
            return page
            
        except:
            print("Error when performing scraping on static web.\nCheck your URL or try the dynamic page method\n")
            self.connect = False
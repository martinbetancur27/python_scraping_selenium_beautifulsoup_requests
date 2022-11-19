import requests

class ScraperStaticPage:
        
    def __init__(self, page_url):
        self.page = page_url
               

    def scraper_page(self):
        #Get page through requests.
        #returns the result of the http request.
        try:
            page = requests.get(self.page)
            return page.text
            
        except:
            print("Error when performing scraping on static web.\nCheck your URL or try the dynamic page method\n")
            return None
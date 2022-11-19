from scraper_static_page import ScraperStaticPage
from scraper_dynamic_page import ScraperDynamicPage
from beautiful_soup import BeautifulSoupPersonalized
import time


def search_options():

    try:
        #This dictionary has:
            #Key: number. Value: list (option to the user, search message, method that executes)
        options ={
            1: ["find_all", "Enter your search (without quotes): ",  "bs_find_all"],
            2: ["find", "Enter your search (without quotes): ",  "bs_find"],
            3: ["find_all_get_text", "Enter your search (without quotes): ", "bs_find_all_get_text"],
            4: ["Get tag (all)", "Enter the tag (without quotes): ", "get_all_tag"],
            5: ["Get tag attribute (all)", "Enter tag-attribute (without quotes and in that format. a-href): ", "get_attribute_by_tag"],
            6: ["Get by XPath", "Enter the Xpath expression (without quotes): ", "get_by_xpath"],
            7: ["Get tag content", "Enter the tag (without quotes): ", "get_content_tag"]
        }

        #Print options to user
        print("\n**** Search options ****")
        
        for key, value in options.items():
            #Print with better presentation.
                #{:<5} means left-aligned with a width of 5.
            print ("{:<5} {:<5}".format(key, value[0]))
        
        while True:
            print("From 1 to 3 correspond to the methods of BeautifulSoup")
            try:
                #prompt the user for the method they want to execute
                choice = int(input("Enter the number of the method you want to run: "))
            except:
                print("****** Please enter a valid number ******")
                #continue. continue the other cycle. The code after is not executed.
                continue

            if choice < 1 or choice > len(options):
                print("****** Invalid option ******")
                continue
            
            print("Choice: ", options.get(choice)[0])

            #ask the user the search they want to perform in the method
            search = input((options.get(choice)[1]))
            #get the method the user chose
            method = options.get(choice)[2]
            break

        #Return the method and search that the user selected
        return method, search

    except:
        print("Search options error")


def print_result(contents):

    print("\n** OUTCOME **\n")

    #Validate if the result is a list to give a more readable impression
    if isinstance(contents, list):
        for content in contents:
            print(content)
    else:
        print(contents)

    print("\n*** Search finished ***")

    #Wait 3 seconds
    time.sleep(3)


def static_page_scraper(page):

    try:
        print("Choice: static page... " + page)
        scraper_static_page = ScraperStaticPage(page)

        return scraper_static_page.scraper_page()

    except:
        print("Error performing static scraping")


def dynamic_page_scraper(page):

    try:
        print("Choice: dynamic page... " + page)
        print("\nPlease wait, the page can be very long")
        scraper_dynamic_page = ScraperDynamicPage(page)

        return scraper_dynamic_page.scraper_page()
        
    except:
        print("Error when performing dynamic scraping")


def custom_test():

    #The user will choose the page to scrape and the search methods
    try:
        while(True):
            page_url = input("Enter the URL: ")

            option_scrape = input("Please enter the number:\n1. Static page\n2. Dynamic page\n---> ")

            if(option_scrape == "1"):
                page_scraped = static_page_scraper(page_url)
                
            else:
                page_scraped = dynamic_page_scraper(page_url)
                
            if (page_scraped is None):
                print("Page Scraped Empty")
                option_empty = input("1. Enter URL\n2. Exit\n---> ")
                
                if (option_empty != "1"):
                    print("Choice: Exit")
                    break
            else:
                break

        return page_url, page_scraped

    except:
        print("Custom test failed")


def default_test():

    try:
        default_option = input("Please enter the number:\n1. Test static page\n2. Test dynamic page\n---> ")
                
        if default_option == "1":
            page = "https://hipertextual.com/"

            return page, static_page_scraper(page)
            
        else:
            page = "https://finance.yahoo.com"
            
            return page, dynamic_page_scraper(page)
    except:
        print("Default test failed")


def main():

    try:
        #input returns a string. I don't put int(input()) to avoid number checking. I get the same result
        #Number different from 1 will be taken as the other option
        option = input("Please enter the number:\n1. Default test (example url)\n2. Custom test (your url)\n---> ")

        if(option == "1"):
            page, page_scraped = default_test()
        else:
            page, page_scraped = custom_test()
        
        if (page_scraped is not None):
            
            search_with_beautiful_soap = BeautifulSoupPersonalized(page_scraped)

            while (True):
                #search_options return two results.
                method, search = search_options()

                #https://www.delftstack.com/howto/python/python-call-function-from-a-string/
                #Python feature. Ability to call a method with a string.
                #first parentheses (object, method name)
                #second parentheses (method parameter)
                contents = getattr(search_with_beautiful_soap, method)(search)

                print_result(contents)

                final_option = input("Please enter the number:\n1. Perform another search: " + page + "\n2. Exit\n---> ")

                if final_option == "1":
                    print("Choice: perform another search on: ", page)
                else:
                    print("Choice: Exit")
                    break
        else:
            print("Scraping is Empty")                    
    except:
        print("bug in the program. Please try again or later")


if __name__ == "__main__":

    main()
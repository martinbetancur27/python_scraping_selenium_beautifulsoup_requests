from scraper_static_page import ScraperStaticPage
from scraper_dynamic_page import ScraperDynamicPage
import time


def static_page(page):

    try:
        scraper = ScraperStaticPage(page)
        if(scraper.connect):
            perform_search(scraper, page)
        else:
            request_another_url()
    except:
        print("Error performing static scraping")


def dynamic_page(page):

    try:
        print("\nPlease wait, the page can be very long")
        scraper = ScraperDynamicPage(page)
        if(scraper.connect):
            perform_search(scraper, page)
        else:
            request_another_url()
    except:
        print("Error when performing dynamic scraping")


def request_another_url():

    try:
        option = input("1. Enter URL\n2. Exit\n---> ")
        if option == "1":
            custom_test()
        else:
            print("Choice: Exit")
    except:
        print("")
    

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


def perform_search(scraper, page):

    #Perform the search with methods of beautiful soup
    try:
        while (True):
            #search_options return two results.
            method, search = search_options()
            
            #https://www.delftstack.com/howto/python/python-call-function-from-a-string/
            
            #Python feature. Ability to call a method with a string.
                #first parentheses (object, method name)
                #second parentheses (method parameter)
            contents = getattr(scraper, method)(search) 
            
            print("\n** OUTCOME **\n")

            #Validate if the result is a list to give a more readable impression
            if isinstance(contents, list):
                for content in contents:
                    print(content)
            else:
                print(contents)

            print("\n*** Search finished ***")

            #Wait 3 seconds to offer the exit option
            time.sleep(3)
            final_option = input("Please enter the number:\n1. Perform another search\n2. Exit\n---> ")

            if final_option == "1":
                print("Choice: perform another search on: ", page)
            else:
                print("Choice: Exit")
                break
    except:
        print("Search error")


def custom_test():

    #The user will choose the page to scrape and the search methods
    try:
        page_url = input("Enter the URL: ")

        option_scrape = input("Please enter the number:\n1. Static page\n2. Dynamic page\n---> ")

        if(option_scrape == "1"):
            print("Choice: Static page")
            static_page(page_url)

        else:
            print("Choice: Dynamic page")
            dynamic_page(page_url)
    except:
        print("Custom test failed")


def main():

    try:
        #input returns a string. I don't put int(input()) to avoid number checking. I get the same result
        #Number different from 1 will be taken as the other option
        option = input("Please enter the number:\n1. Default test (example url)\n2. Custom test (your url)\n---> ")

        if(option == "1"):
            #Default Test: Presets
            default_option = input("Please enter the number:\n1. Test static page\n2. Test dynamic page\n---> ")
            
            if default_option == "1":
                print("Choice: static page... https://hipertextual.com/")
                static_page("https://hipertextual.com/")
                
            else:
                print("Choice: dynamic page... https://finance.yahoo.com")
                dynamic_page("https://finance.yahoo.com")
                
        else:
            custom_test()
    except:
        print("bug in the program. Please try again or later")


if __name__ == "__main__":

    main()
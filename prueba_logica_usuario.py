from inspect import isgenerator
from scraper_static_page import ScraperStaticPage
from scraper_dynamic_page import ScraperDynamicPage

eleccion_por_defecto = True

def static_page(page):

    scraper = ScraperStaticPage(page)
    metodo, busqueda = opciones_busqueda()
    
    contents = getattr(scraper, metodo)(busqueda) 
    
    print("\n** RESULTADO **\n")
    if(iter(contents)):
        for quote in contents:
            print(quote)
    else:
        print(contents)


def dynamic_page(page):

    scraper_yahoo = ScraperDynamicPage(page)
    links_yahoo_home = scraper_yahoo.get_attribute_by_tag("a", "href")

    for link in links_yahoo_home:
        print(link)


def ejecutar_metodo_busqueda(metodo, busqueda):
    pass

def opciones_busqueda():
    "(sin comillas)"
    opciones ={
        1: ["Ingrese su busqueda (sin comillas) ", "find_all", "find_all"],
        2: ["Ingrese su busqueda (sin comillas) ", "find", "find"],
        3: ["Ingrese su busqueda (sin comillas) ", "find_all_get_text", "find_all_get_text"],
        4: ["Ingrese la etiqueta (sin comillas) ", "Obtener etiqueta (todas)", "get_all_tag"],
        5: ["Ingrese la etiqueta (sin comillas) ", "Obtener atributo de etiqueta (todas)", "get_attribute_by_tag"],
        6: ["Ingrese la expresion Xpath (sin comillas) ", "Obtener por Xpath", "get_by_xpath"],
        7: ["Ingrese la etiqueta (sin comillas) ", "Obtener contenido de etiqueta", "get_content_tag"]
    }

    for key, value in opciones.items():
        print ("{:<5} {:<5}".format(key, value[1]))
    
    print("Del 1 al 3 corresponden a los metodos de BeautifulSoup")
    choice = float(input("\nSeleccione el metodo que desea ejecutar: "))
    print("Eleccion: ", opciones.get(choice)[1])
    busqueda = input((opciones.get(choice)[0]))
    metodo = opciones.get(choice)[2]

    return metodo, busqueda

def run():
    static_page("https://www.thoughtco.com/quotes-and-sayings-from-cervantes-3079523#:~:text=Cervantes%20Quotes%20About%20Living%20Wisely,reading%20much%20sharpens%20one's%20ingenuity.)")
    '''opcion = int(input("Por favor elija:\n1. Prueba por defecto\n2. Prueba personalizada"))

    if(opcion == 1):
        while(True):

            opcion_defecto = int(input("Por favor elija:\n1. Prueba pagina estatica\n2. Prueba pagina dinamica\n3. Salir"))
            
            if opcion_defecto == 1:
                url_page = "https://www.thoughtco.com/quotes-and-sayings-from-cervantes-3079523#:~:text=Cervantes%20Quotes%20About%20Living%20Wisely,reading%20much%20sharpens%20one's%20ingenuity.)"
                
                static_page()
            elif opcion_defecto == 2:
                dynamic_page("https://finance.yahoo.com")
            else:
                break'''

if __name__ == "__main__":

    run()

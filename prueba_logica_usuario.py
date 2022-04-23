from inspect import isgenerator
from scraper_static_page import ScraperStaticPage
from scraper_dynamic_page import ScraperDynamicPage

eleccion_por_defecto = True

def static_page(page):

    scraper = ScraperStaticPage(page)
    metodo, busqueda = opciones_busqueda()
    
    #https://www.delftstack.com/howto/python/python-call-function-from-a-string/
    #https://www.quora.com/Is-there-a-way-to-call-a-function-in-python-but-replace-the-name-of-a-function-with-a-defined-variable
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

    
    #Este diccionario tendra:
        #Clave: numero. Valor: lista (opcion al usuario, mensaje de busqueda, metodo que ejecuta)
    opciones ={
        1: ["find_all", "Ingrese su busqueda (sin comillas): ",  "bs_find_all"],
        2: ["find", "Ingrese su busqueda (sin comillas): ",  "bs_find"],
        3: ["find_all_get_text", "Ingrese su busqueda (sin comillas): ", "bs_find_all_get_text"],
        4: ["Obtener etiqueta (todas)", "Ingrese la etiqueta (sin comillas): ", "get_all_tag"],
        5: ["Obtener atributo de etiqueta (todas)", "Ingrese la etiqueta (sin comillas): ", "get_attribute_by_tag"],
        6: ["Obtener por Xpath", "Ingrese la expresion Xpath (sin comillas): ", "get_by_xpath"],
        7: ["Obtener contenido de etiqueta", "Ingrese la etiqueta (sin comillas): ", "get_content_tag"]
    }
    #Imprimir opciones al usuario
    for key, value in opciones.items():
        print ("{:<5} {:<5}".format(key, value[0]))
    
    while True:
        print("Del 1 al 3 corresponden a los metodos de BeautifulSoup")
        try:
            choice = float(input("Ingrese el numero del metodo que desea ejecutar: "))
        except:
            print("****** Por favor ingrese un numero valido ******")
            continue
        if choice < 0 or choice > len(opciones):
            print("****** Opcion no valida ******")
            continue
        
        print("Eleccion: ", opciones.get(choice)[0])
        busqueda = input((opciones.get(choice)[1]))
        metodo = opciones.get(choice)[2]
        break
    #Retornar el metodo y la busqueda que selecciono el usuario
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

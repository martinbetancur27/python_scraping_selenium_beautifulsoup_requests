from scraper_static_page import ScraperStaticPage
from scraper_dynamic_page import ScraperDynamicPage


def static_page(page):

    scraper = ScraperStaticPage(page)
    metodo, busqueda = opciones_busqueda()
    
    #https://www.delftstack.com/howto/python/python-call-function-from-a-string/
    #https://www.quora.com/Is-there-a-way-to-call-a-function-in-python-but-replace-the-name-of-a-function-with-a-defined-variable
    contents = getattr(scraper, metodo)(busqueda) 
    
    print("\n** RESULTADO **\n")

    #Validar si el resultado es una lista para dar una impresion mas legible
    if isinstance(contents, list):
        for content in contents:
            print(content)
    else:
        print(contents)


def dynamic_page(page):

    scraper = ScraperDynamicPage(page)
    metodo, busqueda = opciones_busqueda()

    contents = getattr(scraper, metodo)(busqueda) 

    #Validar si el resultado es una lista para dar una impresion mas legible
    if isinstance(contents, list):
        for content in contents:
            print(content)
    else:
        print(contents)


def opciones_busqueda():

    #Este diccionario tendra:
        #Clave: numero. Valor: lista (opcion al usuario, mensaje de busqueda, metodo que ejecuta)
    opciones ={
        1: ["find_all", "Ingrese su busqueda (sin comillas): ",  "bs_find_all"],
        2: ["find", "Ingrese su busqueda (sin comillas): ",  "bs_find"],
        3: ["find_all_get_text", "Ingrese su busqueda (sin comillas): ", "bs_find_all_get_text"],
        4: ["Obtener etiqueta (todas)", "Ingrese la etiqueta (sin comillas): ", "get_all_tag"],
        5: ["Obtener atributo de etiqueta (todas)", "Ingrese etiqueta-atributo (sin comillas y en ese formato): ", "get_attribute_by_tag"],
        6: ["Obtener por Xpath", "Ingrese la expresion Xpath (sin comillas): ", "get_by_xpath"],
        7: ["Obtener contenido de etiqueta", "Ingrese la etiqueta (sin comillas): ", "get_content_tag"]
    }

    print("\n**** Opciones de busqueda ****")
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

def prueba_personalizada():

    page_url = str(input("Ingrese la URL: "))

    opcion_scrape = int(input("Por favor ingrese el numero:\n1. Pagina estatica\n2. Pagina dinamica\n---> "))

    if(opcion_scrape == 1):
        print("Eleccion: pagina estatica")
        static_page(page_url)

    else:
        print("Eleccion: pagina dinamica")
        dynamic_page(page_url)

def run():
        
    
    opcion = int(input("Por favor ingrese el numero:\n1. Prueba por defecto (ejemplo)\n2. Prueba personalizada\n---> "))
    
    if(opcion == 1):

        opcion_defecto = int(input("Por favor ingrese el numero:\n1. Prueba pagina estatica\n2. Prueba pagina dinamica\n---> "))
        
        if opcion_defecto == 1:
            print("Eleccion: pagina estatica")
            static_page("https://www.thoughtco.com/quotes-and-sayings-from-cervantes-3079523#:~:text=Cervantes%20Quotes%20About%20Living%20Wisely,reading%20much%20sharpens%20one's%20ingenuity.)")
            
        else:
            print("Eleccion: pagina dinamica")
            dynamic_page("https://finance.yahoo.com")
            
    else:

        prueba_personalizada()
        
        

if __name__ == "__main__":

    run()

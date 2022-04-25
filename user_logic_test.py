from scraper_static_page import ScraperStaticPage
from scraper_dynamic_page import ScraperDynamicPage
import time

def static_page(page):

    try:
        scraper = ScraperStaticPage(page)
        realizar_busqueda(scraper, page)
    except:
        print("Error al realizar el scraping estático")

def dynamic_page(page):

    try:
        print("\nPor favor espere, la página puede ser muy extensa")
        scraper = ScraperDynamicPage(page)
        realizar_busqueda(scraper, page)
    except:
        print("Error al realizar scraping dinámico")


def opciones_busqueda():

    try:
        #Este diccionario tendra:
            #Clave: numero. Valor: lista (opcion al usuario, mensaje de busqueda, metodo que ejecuta)
        opciones ={
            1: ["find_all", "Ingrese su búsqueda (sin comillas): ",  "bs_find_all"],
            2: ["find", "Ingrese su búsqueda (sin comillas): ",  "bs_find"],
            3: ["find_all_get_text", "Ingrese su búsqueda (sin comillas): ", "bs_find_all_get_text"],
            4: ["Obtener etiqueta (todas)", "Ingrese la etiqueta (sin comillas): ", "get_all_tag"],
            5: ["Obtener atributo de etiqueta (todas)", "Ingrese etiqueta-atributo (sin comillas y en ese formato): ", "get_attribute_by_tag"],
            6: ["Obtener por Xpath", "Ingrese la expresión Xpath (sin comillas): ", "get_by_xpath"],
            7: ["Obtener contenido de etiqueta", "Ingrese la etiqueta (sin comillas): ", "get_content_tag"]
        }

        #Imprimir opciones al usuario
        print("\n**** Opciones de búsqueda ****")
        
        for key, value in opciones.items():
            #Imprimir con mejor presentacion.
                #{:<5} significa alineado a la izquierda con un ancho de 5.
            print ("{:<5} {:<5}".format(key, value[0]))
        
        while True:
            print("Del 1 al 3 corresponden a los métodos de BeautifulSoup")
            try:
                #preguntar al usuario el metodo que quiere ejecutar
                choice = int(input("Ingrese el número del método que desea ejecutar: "))
            except:
                print("****** Por favor ingrese un número valido ******")
                #continue. continuar el otro ciclo. No se ejecuta el codigo que esta despues.
                continue

            if choice < 1 or choice > len(opciones):
                print("****** Opcion no valida ******")
                continue
            
            print("Elección: ", opciones.get(choice)[0])

            #preguntar al usuario la busqueda que quiere realizar en el metodo
            busqueda = input((opciones.get(choice)[1]))
            #obtener el metodo que el usuario escogio
            metodo = opciones.get(choice)[2]
            break

        #Retornar el metodo y la busqueda que selecciono el usuario
        return metodo, busqueda

    except:
        print("Error en las opciones de búsqueda")


def realizar_busqueda(scraper, page):

    #Realiza la busqueda con metodos de beautiful soup
    try:
        while (True):
            #opciones_busqueda retorna dos resultados.
            metodo, busqueda = opciones_busqueda()
            
            #https://www.delftstack.com/howto/python/python-call-function-from-a-string/
            
            #Caracteristica de Python. Capacidad de llamar un metodo con un string.
                #primer parentesis (objeto, nombre del metodo)
                #segundo parentesis (parametro del metodo)
            contents = getattr(scraper, metodo)(busqueda) 
            
            print("\n** RESULTADO **\n")

            #Validar si el resultado es una lista para dar una impresion mas legible
            if isinstance(contents, list):
                for content in contents:
                    print(content)
            else:
                print(contents)

            print("\n*** Búsqueda terminada ***")

            #Esperar 3 segundos para ofrecer la opcion de salida
            time.sleep(3)
            opcion_final = input("Por favor ingrese el número:\n1. Realizar otra búsqueda\n2. Salir\n---> ")

            if opcion_final == "1":
                print("Elección: realizar otra búsqueda en: ", page)
            else:
                print("Elección: salir")
                break
    except:
        print("Error al realizar la búsqueda")

def prueba_personalizada():

    #El usuario elegira la pagina para hacer scraping y los metodos de busqueda
    try:
        page_url = input("Ingrese la URL: ")

        opcion_scrape = input("Por favor ingrese el número:\n1. Pagina estática\n2. Pagina dinámica\n---> ")

        if(opcion_scrape == "1"):
            print("Elección: pagina estática")
            static_page(page_url)

        else:
            print("Elección: pagina dinámica")
            dynamic_page(page_url)
    except:
        print("Error en la prueba personalizada")


def main():

    try:
        #input devuelve un string. No coloco int(input()) para evitar chequeo de numero. Obtengo el mismo resultado
        #Numero diferente de 1 se tomara como la otra opcion
        opcion = input("Por favor ingrese el número:\n1. Prueba por defecto (ejemplo)\n2. Prueba personalizada\n---> ")

        if(opcion == "1"):
            #Prueba por defecto: Valores pre-establecidos
            opcion_defecto = input("Por favor ingrese el número:\n1. Prueba página estática\n2. Prueba página dinámica\n---> ")
            
            if opcion_defecto == "1":
                print("Elección: pagina estática")
                static_page("https://hipertextual.com/")
                
            else:
                print("Elección: pagina dinámica")
                dynamic_page("https://finance.yahoo.com")
                
        else:
            prueba_personalizada()
    except:
        print("Error en el programa")

if __name__ == "__main__":

    main()
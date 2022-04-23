from bs4 import BeautifulSoup
from lxml import etree

class BeautifulSoupPersonalized():

    def __init__(self, page_source):
        
        self.__beautifulsoup_connect(page_source)
        

    def __beautifulsoup_connect(self, page_source):
        #Recibe como parametro la pagina obtenida por medio de requests o el driver de Selenium
        #Crea el objeto 'Beautiful Soup' de la pagina recibida
        #No retorna ningun valor.

        '''Ejecutar el documento HTML a través de Beautiful Soup nos da un objeto BeautifulSoup que 
        representa el documento como una estructura de datos anidados. 
        https://beautiful-soup-4.readthedocs.io/en/latest/
        
        (Con self.soup se tendran formas de navegar esa estructura de datos)'''

        try:
            self.soup = BeautifulSoup(page_source, 'html.parser')
        except:
            print("Error al conectar con BeutifulSoup")


    #los siguientes metodos son para llamar metodos de BeautifulSoup
    def bs_find_all(self, *args, **kwargs):
        try:
            return self.soup.find_all(*args, **kwargs)
        except:
            print("(bs_find_all) Error al realizar busqueda con el atributo ", args)
        

    def bs_find(self, *args, **kwargs):
        try:
            return self.soup.find(*args, **kwargs)
        except:
            print("(bs_find) Error al realizar busqueda con el atributo ", args)
    

    def bs_find_all_get_text(self, *args, **kwargs):
        try:
            texts = self.soup.find_all(*args, **kwargs)
            list_texts = []
            for text in texts:
                list_texts.append(text.get_text())

            return list_texts
        except:
            print("(bs_find_all_get_text) Error al realizar busqueda con el atributo ", args)

#Los siguientes metodos son para hacer la busqueda mas natural
    def get_all_tag(self, tag):
        #Recibir etiqueta
        #Filtrar por la etiqueta
        #Retornar busqueda
        try:
            return self.soup.find_all(tag)
        except:
            print("Error al realizar scraping con la etiqueta ", tag)


    def get_attribute_by_tag(self, search):
        #recibe etiqueta y atributo
        #Busca todas las etiquetas
            #Filtra por el atributo recibido
        #Retorna una lista con los atributos        
        try:
            #La logica de este programa es recibir dos parametros. 
                #El usuario los ingresa con esta logica: parametro1-parametro2
            search = search.split("-")
            tag = search[0]
            tag_attribute = search[1]

            scraping_tag = self.soup.find_all(tag)
            list_attribute = []
            
            for elem in scraping_tag:
                if elem.has_attr(tag_attribute):
                    list_attribute.append(elem[tag_attribute])
            
            return list_attribute
        except:
            print("Error al obtener el atributo ", tag_attribute)
    

    def get_by_xpath(self, var_xpath):
        #Recibe expresion Xpath
        #Utiliza la clase etree para convertir el HTML y poder filtrar por la expresion
        #Retorna la busqueda
        try:
            dom = etree.HTML(str(self.soup))
            return dom.xpath(var_xpath)
        except:
            print("Error al realizar busqueda XPATH ", var_xpath)
    

    def get_content_tag(self, tag):
        #Recibe etiqueta
        #Busca la etiqueta con el metodo de BeautifulSoup.
            #Captura el contenido de la etiqueta
        #Retorna lista con el contenido

        try:
            texts = self.soup.find_all(tag)
            list_texts = []
            for text in texts:
                list_texts.append(text.get_text())

            return list_texts
        except:
            print("Error al realizar busqueda de contenido en la etiqueta ", tag)
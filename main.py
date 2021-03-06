import requests, os
from bs4 import BeautifulSoup
#from elementos import ElementoHTML
#import writer, json



# Se crea una página de resumen por años.
URLSELECTORES = "https://www.w3.org/TR/css-2020/"


def limpiar(cadena):
    return " ".join(cadena.split())


def todos_los_elementos():

    page = requests.get(URLSELECTORES)
    soup = BeautifulSoup(page.content, 'html5lib')
 
    ## Selectores
    h3 = soup.find("h3", id="selectors")
    elementos = h3.find_next_sibling("div")
    lista = elementos.find_next("ul")
    selectores = lista.find_all("li")

    print ("Hay " + str(len(selectores)) + " CSS")

    for selector in selectores:
        s = limpiar(selector.text)
        s = s.replace("in css2","").replace("in selectors-3","")
        if (s!=""):
            print(s)

    ##Reglas

    

    '''
    ## Elementos y Atributos
    h3 = soup.find("h3", id="elements-3")    
    tabla_elementos = h3.find_next_sibling("table")
    cuerpo_elementos = tabla_elementos.find_next("tbody")
    elementos = cuerpo_elementos.find_all("tr")
    
    print ("Hay " + str(len(elementos)) + " HTML")
    for elemento in elementos:
        
        # Extraemos los datos
        nombre =  elemento.find("code").text
        atributos = limpiar(elemento.find_all("td")[4].text.replace("*","")).split(";")
        versiones = get_versiones(versiones_html,nombre)

        # Creamos el elemento HTML
        e = ElementoHTML()
        e.nombre = nombre
        
        for version in versiones:
            if 'X' in version:
                e.add_version(version.replace("X","xhtml "))
            else:
                e.add_version("html " + version)

        for atributo in atributos:
            if atributo != "globals":
                if not atributo.strip().startswith("on"):
                    e.add_atributo(atributo.strip())
                else:
                    e.add_evento(atributo.strip())
            else:
                e.activeGlobals()

        e.toString()

        writer.doc_elementoHTML(e)
        writer.doc_atributosHTML_generales()
    

    ## Eventos
    tabla_eventos = soup.find("table", id="ix-event-handlers")    
    cuerpo_elementos = tabla_eventos.find_next("tbody")
    eventos = cuerpo_elementos.find_all("th")
    
    print ("Hay " + str(len(eventos)) + " Eventos")

    lista_eventos = []

    for evento in eventos:        
        tipo_evento = limpiar(evento.find_next("td").text)
        if tipo_evento != "body":
            lista_eventos.append(limpiar(evento.text))
            print (limpiar(evento.text))

    writer.doc_eventosHTML_generales(lista_eventos)
    '''


# Inicio del Programa
print ("Analizando la documentación CSS")
todos_los_elementos()





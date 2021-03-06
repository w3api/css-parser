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

    print ("Hay " + str(len(selectores)) + " Selectores CSS")

    for selector in selectores:
        s = limpiar(selector.text)
        s = s.replace("in css2","").replace("in selectors-3","")
        if (s!=""):
            print(s)

    ##Reglas

    ## Propiedades
    h3 = soup.find("h3", id="properties")
    elementos = h3.find_next_sibling("div")
    lista = elementos.find_next("ul")
    propiedades = lista.find_all("li")

    print ("Hay " + str(len(propiedades)) + " Propiedades")

    for propiedad in propiedades:
        p = limpiar(propiedad.text)
        p = p.replace("in css-align-3","").replace("in css-flexbox-1","").replace("in css2","").replace("in css-speech-1","").replace("in css-multicol-1","")
        if (p!=""):
            print(p)
    

# Inicio del Programa
print ("Analizando la documentación CSS")
todos_los_elementos()





import requests, os
from bs4 import BeautifulSoup
from elementos import ElementoCSS
import writer

# Se crea una página de resumen por años.
URLBASE = "https://www.w3.org/TR/css-2020/"

def limpiar_parametros(str):
    cadena = str.replace("?","").replace("<","").replace(">","").replace("[","").replace("]","").replace("#","").replace("0,∞","").replace("{1,2}","").replace("{1,4}","").replace("&&","").replace("/","").replace("\'","").replace(",","").replace("+","").replace("*","").replace("’","").replace("‘","").replace("{23}","").replace("{03}","").replace("1∞","").replace("|","")
    return limpiar(cadena)

def limpiar(cadena):
    return " ".join(cadena.split())

def get_valores(url,propiedad):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')

    # La documentación moderna lo tiene en una tabla
    tabla = soup.find("table", {"data-link-for-hint":propiedad})
    if tabla:
        valor = tabla.find("td", {"class":"prod"})
        valor = limpiar(valor.text)
    else:
        # Lo buscamos por dfn con id="propdef-nombrepropiedad"
        dfn = soup.find("dfn", id="propdef-"+propiedad)
        if dfn:
            valor = dfn.find_next("td")
            valor = limpiar(valor.text)

            # En algunos casos no hay th-td, si no que es td-td
            if valor == "Value:":
                valor = dfn.find_next("td").find_next("td")
                valor = limpiar(valor.text)
            
        else:
            return ""

    return valor

def todos_los_elementos():

    page = requests.get(URLBASE)
    soup = BeautifulSoup(page.content, 'html5lib')

    ## Selectores
    h3 = soup.find("h3", id="selectors")
    elementos = h3.find_next_sibling("div")
    lista = elementos.find_next("ul")
    selectores = lista.find_all("li")
    selectoresDict = set()  

    print ("Hay " + str(len(selectores)) + " Selectores CSS")

    for selector in selectores:
        s = limpiar(selector.text)
        s = s.replace("in css2","").replace("in selectors-3","").strip()
        if (s!=""):
            nombre = s.replace(":","").replace("()","")
            
            if nombre not in selectoresDict:
                selectoresDict.add(nombre)
                e = ElementoCSS()
                e.nombre = nombre
                e.add_sintaxis(s)
                e.add_categoria("selector css")

                writer.doc_elementoCSS(e)

    ##Reglas
    h3 = soup.find("h3", id="at-rules")
    elementos = h3.find_next_sibling("div")
    lista = elementos.find_next("ul")
    reglas = lista.find_all("li")
    reglasDict = set()  

    print ("Hay " + str(len(reglas)) + " Reglas")

    for regla in reglas:
        r = limpiar(regla.text)
        r = r.replace("in css-conditional-3","").replace("in css2","").strip()
        if (r!=""):
            nombre = r.replace("@","").strip()
            
            if nombre not in reglasDict:
                reglasDict.add(nombre)
                e = ElementoCSS()
                e.nombre = nombre
                e.add_sintaxis(r)
                e.add_categoria("regla css")

                writer.doc_elementoCSS(e)
    
    ## Propiedades
    h3 = soup.find("h3", id="properties")
    elementos = h3.find_next_sibling("div")
    lista = elementos.find_next("ul")
    propiedades = lista.find_all("li")

    print ("Hay " + str(len(propiedades)) + " Propiedades")

    for propiedad in propiedades:
        link = propiedad.find("a").get("href")        
        p = limpiar(propiedad.text)
        p = p.replace("in css-align-3","").replace("in css-flexbox-1","").replace("in css2","").replace("in css-speech-1","").replace("in css-multicol-1","").strip()
        if (p!=""):
            # Recupero los valores
            valores = get_valores(link,p)
            parametros = limpiar_parametros(valores).split()

            e = ElementoCSS()
            e.nombre = p
            e.add_sintaxis(p + " : " + valores)
            e.add_categoria("propiedad css")
            for parametro in parametros:
                e.add_parametro(parametro)

            writer.doc_elementoCSS(e)
    

# Inicio del Programa
print ("Analizando la documentación CSS")
todos_los_elementos()

#print (get_valores("https://drafts.csswg.org/css-fonts-3/#propdef-font","font"))



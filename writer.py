from datetime import datetime
import os, html, json


__OUT__ = "/Users/victor/GitHub/w3api-dev/_posts/css/"
__OUTJSON__ = "/Users/victor/GitHub/w3api-dev/_data/CSS/"

def doc_JSON(elemento):

    basepath = elemento.nombre

    if not os.path.exists(__OUTJSON__ + elemento.nombre[0]):
        os.makedirs(__OUTJSON__ + elemento.nombre[0])

    # Clases como AbstractDocument.AttributeContext se generan en un directorio
    f = open(__OUTJSON__ + elemento.nombre[0] + "/" + basepath + ".json","w")

    data_json = {}
    data_json["description"] = ""
    data_json["code"] = ""
    data_json["ldc"] = []

    if elemento.valores:
        v = []
        for valor in elemento.valores:
            valor_json = {}
            valor_json["nombre"] = valor
            valor_json["description"] = ""
            v.append(valor_json)
        data_json["valores"] = v


    f.write(json.dumps(data_json,indent=4))
    f.close()

## Genera los ficheros desde una clase
def gen_cabecera(nombre,path,clave,tags):

    c = ["---" + "\n",
                "title: " + nombre + "\n",
                "permalink: " + path + "\n",
                "date: " + str(datetime.now()) + "\n",
                "key: " + clave + "\n",
                "category: css" + "\n",
                "tags: " + str(tags) + "\n",
                "sidebar: " + "\n",
                "  nav: css" + "\n",
                "---" + "\n\n"]
    return c

def gen_sintaxis(sintaxis):

    s = ["## Sintaxis\n",
          "~~~css\n"]
    for sin in sintaxis:
         s.append(sin + "\n")
    s.append("~~~\n\n")
    return s

def gen_valores(valores,clave):
    v = ["## Valores\n"]
    for valor in valores:
        v.append("* **" + valor + "**,  ")
        v.append("{% include w3api/value_description.html propiedad=" + clave + " valor=\"" + valor + "\" %}\n")
    v.append("\n")
    return v


def gen_ldc(clave):
    ldc = ["## Artículos\n",
           "<ul>\n",
            "{%- for _ldc in " + clave + ".ldc -%}\n",
            "   <li>\n",
                "       <a href=\"{{_ldc['url'] }}\">{{ _ldc['nombre'] }}</a>\n",
            "   </li>\n",
            "{%- endfor -%}\n",
          "</ul>\n"]
    return ldc

def gen_ejemplo(base):

    e = ["## Ejemplo\n"
         "~~~css\n",
         "{{ " + base + ".code}}\n",
         "~~~\n\n",
         ]
    return e

def gen_descripcion(base):
    d = ["## Descripción\n",
         "{{" + base + ".description }}\n\n"
         ]
    return d


def doc_elementoCSS(e):

    basepath = e.nombre

    if not os.path.exists(__OUT__ + e.nombre[0] + "/" + basepath + "/"):
        os.makedirs(__OUT__ + e.nombre[0] + "/" + basepath + "/")

    f = open(__OUT__ + e.nombre[0] + "/" + basepath + "/2021-01-01-" + e.nombre + ".md","w")
    clave = "CSS."+e.nombre[0]+"."+basepath
    jsonsource = "CSS."+e.nombre[0]+"."+basepath.replace(".","")  # Las base JSON compuestas se accede sin punto
    path = "/css/"+basepath.replace(".","/")+"/"

    tags = []
    for categoria in e.categorias:
        tags.append(categoria)

    for version in e.versiones:
        tags.append(version)

    cabecera = gen_cabecera(e.nombre,path,clave, tags)
    f.writelines(cabecera)

    descripcion = gen_descripcion("site.data." + jsonsource)
    f.writelines(descripcion)

    sintaxis = gen_sintaxis(e.sintaxis)
    f.writelines(sintaxis)

    valores = gen_valores(e.valores,"site.data." + jsonsource)
    f.writelines(valores)

    ejemplo = gen_ejemplo("site.data." + jsonsource)
    f.writelines(ejemplo)

    ldc = gen_ldc("site.data." + jsonsource)
    f.writelines(ldc)

    f.close()

    doc_JSON(e)
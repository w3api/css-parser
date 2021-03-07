class ElementoCSS:

    nombre = ""
    sintaxis = []
    categorias = []
    versiones = []
    valores = set()
    
    def __init__(self):
        self.nombre = ""
        self.sintaxis = []
        self.categorias = []
        self.versiones = []
        self.valores = set()

    def nombre(self,nombre):
        self.nombre = nombre
    
    def add_sintaxis(self,sintaxis):
        self.sintaxis.append(sintaxis)

    def add_categoria(self,categoria):
        self.categorias.append(categoria)

    def add_version(self,version):
        self.versiones.append(version)

    def add_valor(self,valor):
        self.valores.add(valor)


    def toString(self):
        print("Nombre: " + self.nombre)
        print("Sintaxis: ")
        for sintaxis in self.sintaxis:
            print(">> " + sintaxis)
        print("Categorias: ")
        for categoria in self.categorias:
            print(">> " + sintaxis)
        print("Valores: ")
        for valor in self.valores:
            print(">> " + valor)
        print("Versiones: ")
        for version in self.versiones:
            print(">> " + version)

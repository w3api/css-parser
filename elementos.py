class ElementoCSS:

    nombre = ""
    sintaxis = []
    categorias = []
    versiones = []
    
    def __init__(self):
        self.nombre = ""
        self.sintaxis = []
        self.categorias = []
        self.versiones = []
        

    def nombre(self,nombre):
        self.nombre = nombre
    
    def add_sintaxis(self,sintaxis):
        self.sintaxis.append(sintaxis)

    def add_categoria(self,categoria):
        self.categorias.append(categoria)

    def add_version(self,version):
        self.versiones.append(version)


    def toString(self):
        print("Nombre: " + self.nombre)
        print("Sintaxis: ")
        for sintaxis in self.sintaxis:
            print(">> " + sintaxis)
        for categoria in self.categorias:
            print(">> " + sintaxis)
        for version in self.versiones:
            print(">> " + version)
class ElementoCSS:

    nombre = ""
    sintaxis = []
    categorias = []
    versiones = []
    parametros = set()
    
    def __init__(self):
        self.nombre = ""
        self.sintaxis = []
        self.categorias = []
        self.versiones = []
        self.parametros = set()

    def nombre(self,nombre):
        self.nombre = nombre
    
    def add_sintaxis(self,sintaxis):
        self.sintaxis.append(sintaxis)

    def add_categoria(self,categoria):
        self.categorias.append(categoria)

    def add_version(self,version):
        self.versiones.append(version)

    def add_parametro(self,parametro):
        self.parametros.add(parametro)


    def toString(self):
        print("Nombre: " + self.nombre)
        print("Sintaxis: ")
        for sintaxis in self.sintaxis:
            print(">> " + sintaxis)
        print("Categorias: ")
        for categoria in self.categorias:
            print(">> " + sintaxis)
        print("Parametros: ")
        for parametro in self.parametros:
            print(">> " + parametro)
        print("Versiones: ")
        for version in self.versiones:
            print(">> " + version)

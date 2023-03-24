from dataclasses import dataclass

@dataclass

class Elemento:

    nombre: str

    def __eq__(self, otro_nombre):
        return self.nombre == otro_nombre

nombre_1 = Elemento("Alfa")
nombre_2 = Elemento("Beta")

print(nombre_1 == nombre_2)

class Conjunto:

    contador: int = 0

    def __init__(self, nombre, __id: contador):
        self.lista_objetos: list[Elemento] = []
        self.nombre: str = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, objeto: Elemento) -> bool:
        for i in self.lista_objetos:
            if i.nombre == objeto.nombre:
                return True
            return False

    def agregar_elemento(self,):










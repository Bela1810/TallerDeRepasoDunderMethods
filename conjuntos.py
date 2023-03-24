from dataclasses import dataclass
from typing import List

@dataclass

class Elemento:

    nombre: str

    def __eq__(self, otro_nombre):
        return self.nombre == otro_nombre

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

    def agregar_elemento(self, objeto: Elemento):
        if not self.contiene(objeto):
            self.lista_objetos.append(objeto)

    def unir(self, other_conjunto):
        for objeto in other_conjunto.lista_objetos:
            self.agregar_elemento(objeto)

    def __add__(self, other_conjunto):
        nuevo_conjunto = Conjunto(self.nombre + " UNION " + other_conjunto.nombre)
        for objeto in self.lista_objetos:
            nuevo_conjunto.agregar_elemento(objeto)
        for objeto in other_conjunto.lista_objetos:
            nuevo_conjunto.agregar_elemento(objeto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for objeto in conjunto1.lista_objetos:
            if conjunto2.contiene(objeto):
                nuevo_conjunto.agregar_elemento(objeto)
        return nuevo_conjunto

    def __str__(self):
        objetos_str = ", ".join([objeto.nombre for objeto in self.lista_objetos])
        return f"Conjunto {self.nombre}: ({objetos_str})"


elemento_1 = Elemento("Alfa")
elemento_2 = Elemento("Beta")
conjunto_1 = Conjunto("A")
conjunto_2 = Conjunto("B")











from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, otro):
        return self.nombre == otro.nombre

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_resultante = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        elementos_interseccion = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nuevo_conjunto = Conjunto(nombre_resultante)
        nuevo_conjunto.elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"

if __name__ == "__main__":
    elemento_1 = Elemento("A")
    elemento_2 = Elemento("B")
    conjunto_1 = Conjunto("Conjunto1")
    conjunto_2 = Conjunto("Conjunto2")

    conjunto_1.agregar_elemento(elemento_1)
    conjunto_2.agregar_elemento(elemento_2)

    conjunto_union = conjunto_1 + conjunto_2
    conjunto_interseccion = Conjunto.intersectar(conjunto_1, conjunto_2)

    print(conjunto_1)
    print(conjunto_2)
    print(conjunto_union)
    print(conjunto_interseccion)

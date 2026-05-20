from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def hasMore(self):
        pass

    @abstractmethod
    def getNext(self):
        pass

class IterableCollection(ABC):
    @abstractmethod
    def createIterator(self):
        pass

class Proyecto:
    def __init__(self, nombre, cupo):
        self.nombre = nombre
        self.cupo = cupo

    def __str__(self):
        return f"{self.nombre} (Cupo: {self.cupo})"

# ConcreteIterator
class ProyectoIterator(Iterator):
    def __init__(self, proyectos):
        self._proyectos = proyectos
        self._posicion = 0

    def hasMore(self):
        return self._posicion < len(self._proyectos)

    def getNext(self):
        if self.hasMore():
            proyecto = self._proyectos[self._posicion]
            self._posicion += 1
            return proyecto
        else:
            raise StopIteration("No hay más proyectos")

# ConcreteCollection
class ListaProyectos(IterableCollection):
    def __init__(self):
        self._proyectos = []

    def agregarProyecto(self, proyecto):
        self._proyectos.append(proyecto)

    def createIterator(self):
        return ProyectoIterator(self._proyectos)


class Coordinador:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrarProyectos(self, listaProyectos):
        print(f"\nProyectos disponibles para asignación:\n")

        iterador = listaProyectos.createIterator()

        while iterador.hasMore():
            proyecto = iterador.getNext()
            print(proyecto)
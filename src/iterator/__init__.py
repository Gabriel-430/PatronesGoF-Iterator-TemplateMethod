class Proyecto:
    def __init__(self, nombre, cupo):
        self.nombre = nombre
        self.cupo = cupo

    def __str__(self):
        return f"{self.nombre} (Cupo: {self.cupo})"


class ProyectoIterator:
    def __init__(self, proyectos):
        self._proyectos = proyectos
        self._posicion = 0

    def has_next(self):
        return self._posicion < len(self._proyectos)

    def next(self):
        if self.has_next():
            proyecto = self._proyectos[self._posicion]
            self._posicion += 1
            return proyecto
        else:
            raise StopIteration("No hay más proyectos")


class ListaProyectos:
    def __init__(self):
        self._proyectos = []

    def agregar_proyecto(self, proyecto):
        self._proyectos.append(proyecto)

    def crear_iterador(self):
        return ProyectoIterator(self._proyectos)


class Coordinador:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_proyectos(self, lista_proyectos):
        print(f"\nProyectos disponibles para asignación:\n")

        iterador = lista_proyectos.crear_iterador()

        while iterador.has_next():
            proyecto = iterador.next()
            print(proyecto)
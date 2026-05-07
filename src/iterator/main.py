from __init__ import Proyecto, ListaProyectos, Coordinador

def main():
    lista = ListaProyectos()
    lista.agregarProyecto(Proyecto("App Chedrahui", 2))
    lista.agregarProyecto(Proyecto("Proyecto Meta", 0))
    lista.agregarProyecto(Proyecto("Proyecto Banco", 3))

    coordinador = Coordinador("Dr. Angel")

    coordinador.mostrarProyectos(lista)


if __name__ == "__main__":
    main()  
    
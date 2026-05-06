from __init__ import Proyecto, ListaProyectos, Coordinador

def main():
    lista = ListaProyectos()
    lista.agregar_proyecto(Proyecto("App Chedrahui", 2))
    lista.agregar_proyecto(Proyecto("Proyecto Meta", 0))
    lista.agregar_proyecto(Proyecto("Proyecto Banco", 3))

    coordinador = Coordinador("Dr. Angel")

    coordinador.mostrar_proyectos(lista)


if __name__ == "__main__":
    main()  
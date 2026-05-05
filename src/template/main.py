from __init__ import ProcesadorCSV, ProcesadorPDF

def main():
    # Crear instancias de los procesadores específicos
    procesador_reportes = ProcesadorCSV()
    procesador_libros = ProcesadorPDF()

    # Ejecutar el método plantilla
    resultado_1 = procesador_reportes.procesar_archivo("ventas_anuales.csv")
    print(f"Resultado 1: {resultado_1}\n")

    resultado_2 = procesador_libros.procesar_archivo("manual_usuario.pdf")
    print(f"Resultado 2: {resultado_2}\n")
if __name__ == "__main__":
    main()
from __init__ import ProcesadorCSV, ProcesadorPDF

# Client
def main():
    procesador_reportes = ProcesadorCSV()
    procesador_libros = ProcesadorPDF()

    resultado_1 = procesador_reportes.procesar_archivo("ventas_anuales.csv")
    print(f"Resultado 1: {resultado_1}\n")

    resultado_2 = procesador_libros.procesar_archivo("manual_usuario.pdf")
    print(f"Resultado 2: {resultado_2}\n")


if __name__ == "__main__":
    main()
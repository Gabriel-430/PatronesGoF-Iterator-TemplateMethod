class ProcesadorDocumentos:
    def procesar_archivo(self, ruta_archivo):
        self.abrir_archivo(ruta_archivo)
        datos_sin_procesar = self.extraer_datos(ruta_archivo)
        resultado = self.analizar_datos(datos_sin_procesar)
        self.cerrar_archivo(ruta_archivo)
        
        return resultado

    def abrir_archivo(self, ruta_archivo):
        print(f"Abriendo el archivo '{ruta_archivo}'...")

    def analizar_datos(self, datos):
        print("Analizando y estructurando la información obtenida...")
        return f"Reporte final basado en: {datos}"

    def cerrar_archivo(self, ruta_archivo):
        print(f"Cerrando '{ruta_archivo}' y liberando recursos.")
        
    def extraer_datos(self, ruta_archivo):
        raise NotImplementedError("Método extraer_datos no implementado en la subclase")

class ProcesadorCSV(ProcesadorDocumentos):
    def extraer_datos(self, ruta_archivo):
        print("Extrayendo datos del archivo CSV...")
        return "[Datos del CSV]"


class ProcesadorPDF(ProcesadorDocumentos):
    def extraer_datos(self, ruta_archivo):
        print("Extrayendo texto e imágenes del PDF...")
        return "[Texto del PDF]"
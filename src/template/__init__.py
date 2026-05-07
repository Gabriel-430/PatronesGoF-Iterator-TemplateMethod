from abc import ABC, abstractmethod

# AbstractClass
class ProcesadorDocumentos(ABC):
    
    # Template Method
    def procesar_archivo(self, ruta_archivo):
        self.abrir_archivo(ruta_archivo)
        datos_sin_procesar = self.extraer_datos(ruta_archivo)
        
        if self.requiere_analisis():
            resultado = self.analizar_datos(datos_sin_procesar)
        else:
            resultado = f"Contenido extraido: {datos_sin_procesar}"
            
        self.cerrar_archivo(ruta_archivo)
        return resultado

    # Operación Concreta
    def abrir_archivo(self, ruta_archivo):
        print(f"Abriendo el archivo '{ruta_archivo}'...")

    # Operación Concreta
    def analizar_datos(self, datos):
        print("Analizando y estructurando la información obtenida...")
        return f"Reporte final basado en: {datos}"

    # Operación Concreta
    def cerrar_archivo(self, ruta_archivo):
        print(f"Cerrando '{ruta_archivo}' y liberando recursos.")
        
    # Operación Primitiva
    @abstractmethod 
    def extraer_datos(self, ruta_archivo):
        pass
    
    # Operación Concreta
    def requiere_analisis(self):
        return True


# ConcreteClass
class ProcesadorCSV(ProcesadorDocumentos):
    
    # Implementación de la operación primitiva
    def extraer_datos(self, ruta_archivo):
        print("Extrayendo datos del archivo CSV...")
        return "[Datos del CSV]"


# ConcreteClass
class ProcesadorPDF(ProcesadorDocumentos):
    
    # Implementación de la operación primitiva  
    def extraer_datos(self, ruta_archivo):
        print("Extrayendo texto del PDF...")
        return "[Texto del PDF]"
    
    # Sobrescritura de la Operación Concreta
    def requiere_analisis(self):
        return False
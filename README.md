# Exposición de Patrones de Diseño (GoF)
**Autores:** Emiliano Morales Baizabal y Gabriel Hernández Martínez

# PatronesGoF-Iterator-TemplateMethod
Implementación de los patrones de diseño Iterator y Template Method en Python.

## 1. Patrones Implementados
En este proyecto se implementan dos patrones de comportamiento:
* **Iterator (Iterador)**
* **Template Method (Método Plantilla)**

## 2. ¿Qué problema resuelve cada ejemplo?
* **Iterator:** El patrón **Iterator** en este ejemplo resuelve el problema de recorrer y mostrar los proyectos disponibles en un sistema de prácticas profesionales, junto con su cupo actual  y sin depender de cómo están almacenados internamente, permitiendo iterar sobre la colección de proyectos de manera uniforme y controlada.
* **Template Method:** En este ejemplo se resuelve el problema de procesar diferentes tipos de documentos en un sistema, definiendo los pasos generales desde el inicio y sin repetir código para abrir o cerrar los archivos, permitiendo que cada formato de archivo extraiga su información sin alterar el flujo del programa.

## 3. Herramientas y Lenguaje
* **Lenguaje:** Python 3.14
* **Gestor de dependencias:** Este proyecto no utiliza dependencias. Se necesita tener Python instalado
* **IDE recomendado:** Visual Studio Code

## 4. Requisitos e Instalación de dependencias
Para instalar python debes ir a la página oficial (https://www.python.org/downloads/) y hacer click en Download Python 


## 5. Cómo ejecutar los ejemplos
Para poder ejecutar los ejemplos, antes es necesario clonar el repositorio usando el siguiente comando:
```bash
git clone https://github.com/Gabriel-430/PatronesGoF-Iterator-TemplateMethod.git
cd PatronesGoF-Iterator-TemplateMethod
```
El código está separado en dos paquetes principales. Para ver la demostración de cada patrón:

* **Para ejecutar Iterator:**
*Desde la terminal en la carpeta principal del proyecto:*
```bash
cd src
cd iterator
python main.py
```

*Desde el explorador de archivos*
Ejecuta la clase principal ubicada en `"PatronesGoF-Iterator-TemplateMethod\src\iterator\main.py"`.
*Salida esperada:* 
```
Proyectos disponibles para asignación:
App Chedrahui (Cupo: 2)
Proyecto Meta (Cupo: 0)
Proyecto Banco (Cupo: 3).
```


* **Para ejecutar Template Method:**
*Desde la terminal en la carpeta principal del proyecto:*
```bash
cd src
cd template_method
python main.py
```
*Desde el explorador de archivos*
Ejecuta la clase principal ubicada en `"PatronesGoF-Iterator-TemplateMethod\src\template_method\main.py"`.
*Salida esperada:*
```
Abriendo el archivo 'ventas_anuales.csv'...
Extrayendo datos del archivo CSV...
Analizando y estructurando la información obtenida...
Cerrando 'ventas_anuales.csv' y liberando recursos.
Resultado 1: Reporte final basado en: [Datos del CSV]

Abriendo el archivo 'manual_usuario.pdf'...
Extrayendo texto del PDF...
Cerrando 'manual_usuario.pdf' y liberando recursos.
Resultado 2: Contenido extraido: [Texto del PDF]
```

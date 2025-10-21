Ejercicio de Funciones Intermedias 1
Este proyecto es un script de Python (funciones_intermedias_1.py) diseñado para practicar la manipulación y recorrido de estructuras de datos complejas, específicamente listas y diccionarios anidados.

El script se divide en cuatro tareas principales:

Actualización directa de valores en listas y diccionarios.

Una función para iterar sobre una lista de diccionarios e imprimir todos sus pares clave-valor.

Una función para iterar sobre una lista de diccionarios e imprimir solo el valor de una clave específica.

Una función para iterar sobre un diccionario que contiene listas como valores.

Contenido del Archivo
1. Actualización de Valores
Esta sección del script realiza modificaciones directas en variables predefinidas para demostrar cómo acceder y cambiar datos anidados.

matriz: Se cambia el primer elemento de la segunda lista ([1][0]) de 3 a 6.

cantantes: Se cambia el valor de la clave "nombre" en el primer diccionario de la lista ([0]) a "Enrique Martin Morales".

ciudades: Se cambia el tercer elemento ([2]) de la lista asociada a la clave "México" por "Monterrey".

coordenadas: Se cambia el valor de la clave "latitud" en el primer diccionario de la lista ([0]) a 9.9355431.

2. Función iterarDiccionario(lista)
Esta función demuestra cómo recorrer una lista que contiene múltiples diccionarios.

Propósito: Recibir una lista de diccionarios e imprimir cada par clave-valor de cada diccionario en un formato legible.

Parámetros:

lista (list): Una lista donde cada elemento es un diccionario.

Salida (a consola): Imprime una línea por cada diccionario, formateada como: llave1 - valor1, llave2 - valor2, ...

Ejemplo de Uso:

Python

cantantes_ejemplo = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

iterarDiccionario(cantantes_ejemplo)
Salida del Ejemplo:

nombre - Ricky Martin, pais - Puerto Rico
nombre - Chayanne, pais - Puerto Rico
3. Función iterarDiccionario2(llave, lista)
Esta función se enfoca en extraer un dato específico de cada diccionario dentro de una lista.

Propósito: Recibir una clave específica (string) y una lista de diccionarios. La función debe imprimir únicamente el valor de esa clave para cada diccionario en la lista.

Parámetros:

llave (str): El nombre de la clave cuyo valor se desea extraer.

lista (list): Una lista de diccionarios.

Salida (a consola): Imprime el valor correspondiente a la llave de cada diccionario, uno por línea.

Ejemplo de Uso:

Python

# Usando la misma lista 'cantantes_ejemplo'
iterarDiccionario2("nombre", cantantes_ejemplo)

print("---")

iterarDiccionario2("pais", cantantes_ejemplo)
Salida del Ejemplo:

Ricky Martin
Chayanne
---
Puerto Rico
Puerto Rico
4. Función imprimirInformacion(diccionario)
Esta función demuestra cómo manejar un diccionario cuyos valores no son simples, sino que son listas.

Propósito: Recibir un diccionario donde los valores son listas. La función debe imprimir el nombre de cada clave, el tamaño de su lista (cuántos elementos tiene), y luego cada uno de los elementos de esa lista.

Parámetros:

diccionario (dict): Un diccionario (ej: {"key1": [val1, val2], "key2": [valA, valB]}).

Salida (a consola): Imprime un bloque formateado para cada clave en el diccionario.

Ejemplo de Uso:

Python

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago"],
   "comidas": ["gallo pinto", "casado", "tamales"]
}

imprimirInformacion(costa_rica)
Salida del Ejemplo:

3 CIUDADES
San José
Limón
Cartago

3 COMIDAS
gallo pinto
casado
tamales

Cómo Ejecutar el Archivo
Asegúrate de tener Python 3 instalado.

Guarda el código en un archivo llamado funciones_intermedias_1.py.

Abre una terminal o línea de comandos.

Navega al directorio donde guardaste el archivo.

Ejecuta el siguiente comando:

Bash

python3 funciones_intermedias_1.py

El script imprimirá los resultados de todas las tareas y ejecuciones de funciones en la consola.
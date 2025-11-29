# funciones_intermedias_1.py

# --- 1. Actualizar valores en diccionarios y listas ---

print("--- Tarea 1: Actualizaciones ---")

# Datos iniciales
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 1.1 Cambia el valor de 3 en matriz por 6
matriz[1][0] = 6
print(f"Matriz actualizada: {matriz}")

# 1.2 Cambia el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(f"Cantantes actualizados: {cantantes}")

# 1.3 En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
print(f"Ciudades actualizadas: {ciudades}")

# 1.4 En las coordenadas, cambia el valor de “latitud”
coordenadas[0]["latitud"] = 9.9355431
print(f"Coordenadas actualizadas: {coordenadas}")

print("\n" + "="*30 + "\n")


# --- 2. Iterar a través de una lista de diccionarios ---

def iterarDiccionario(lista):
    """
    Recibe una lista de diccionarios e imprime cada par llave-valor
    en un formato "llave - valor, llave2 - valor2".
    """
    # Itera sobre cada diccionario en la lista
    for diccionario in lista:
        # Lista temporal para almacenar las partes (ej: "nombre - Ricky Martin")
        partes_string = []
        # Itera sobre cada par (llave, valor) en el diccionario
        for llave, valor in diccionario.items():
            partes_string.append(f"{llave} - {valor}")
        
        # Une todas las partes con ", " y lo imprime
        print(", ".join(partes_string))

# Datos de ejemplo para la Tarea 2 y 3
cantantes_ejemplo = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print("--- Tarea 2: iterarDiccionario ---")
iterarDiccionario(cantantes_ejemplo)

print("\n" + "="*30 + "\n")


# --- 3. Obtener valores de una lista de diccionarios ---

def iterarDiccionario2(llave, lista):
    """
    Recibe una llave (string) y una lista de diccionarios.
    Imprime el valor de esa llave para cada diccionario en la lista.
    """
    # Itera sobre cada diccionario en la lista
    for diccionario in lista:
        # Comprueba si la llave existe antes de intentar acceder a ella
        if llave in diccionario:
            print(diccionario[llave])
        else:
            print(f"Advertencia: La llave '{llave}' no existe en un diccionario.")

print("--- Tarea 3: iterarDiccionario2 (nombre) ---")
iterarDiccionario2("nombre", cantantes_ejemplo)

print("\n--- Tarea 3: iterarDiccionario2 (pais) ---")
iterarDiccionario2("pais", cantantes_ejemplo)

print("\n" + "="*30 + "\n")


# --- 4. Iterar a través de un diccionario con valores de lista ---

def imprimirInformacion(diccionario):
    """
    Recibe un diccionario donde los valores son listas.
    Imprime el nombre de cada clave, el tamaño de su lista,
    y luego los valores de la lista.
    """
    # Itera sobre cada par (llave, valor_lista) en el diccionario
    for llave, valor_lista in diccionario.items():
        # Imprime el encabezado (ej: "4 CIUDADES")
        print(f"{len(valor_lista)} {llave.upper()}")
        
        # Itera sobre cada item en la lista de valores
        for item in valor_lista:
            print(item)
        
        # Agrega un salto de línea para separar las categorías
        print() 

# Datos de ejemplo para la Tarea 4
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("--- Tarea 4: imprimirInformacion ---")
imprimirInformacion(costa_rica)
"""
SOLUCIONES - LECCIÓN 7: COMPREHENSIONS Y ESTRUCTURAS AVANZADAS
==============================================================

Estas son las soluciones completas de los ejercicios.
Compara tu código con estas soluciones para aprender.
"""

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 1: List Comprehensions Básicas
# ═══════════════════════════════════════════════════════════════

# Lista de cubos (x**3) de números del 1 al 10
lista_cubos = [x**3 for x in range(1, 11)]

# Lista con el doble de cada número
lista_dobles = [x*2 for x in [5, 10, 15, 20]]

# Convierte todos los nombres a mayúsculas
nombres = ["ana", "luis", "maría", "pedro"]
lista_mayusculas = [nombre.upper() for nombre in nombres]

# Pruebas
print("--- Ejercicio 1: List Comprehensions Básicas ---")
print(f"Cubos 1-10: {lista_cubos}")
print(f"Dobles: {lista_dobles}")
print(f"Mayúsculas: {lista_mayusculas}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 2: List Comprehensions con Condiciones
# ═══════════════════════════════════════════════════════════════

# Solo números múltiplos de 3 del 1 al 20
multiplos_de_3 = [x for x in range(1, 21) if x % 3 == 0]

# Solo palabras con más de 5 letras
palabras = ["sol", "python", "gato", "programación", "luz", "desarrollo"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]

# Solo números positivos
numeros = [-5, 3, -2, 8, 0, -1, 7, 4]
numeros_positivos = [n for n in numeros if n > 0]

# Clasificación de números
numeros2 = [5, -3, 0, 8, -1]
clasificacion = ["positivo" if x > 0 else ("negativo" if x < 0 else "cero") for x in numeros2]

# Pruebas
print("\n--- Ejercicio 2: Comprehensions con Condiciones ---")
print(f"Múltiplos de 3: {multiplos_de_3}")
print(f"Palabras largas: {palabras_largas}")
print(f"Números positivos: {numeros_positivos}")
print(f"Clasificación: {clasificacion}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 3: Dict y Set Comprehensions
# ═══════════════════════════════════════════════════════════════

# Diccionario {número: cuadrado}
dict_cuadrados = {x: x**2 for x in range(1, 6)}

# Diccionario {palabra: longitud}
palabras = ["Python", "es", "genial"]
dict_longitudes = {palabra: len(palabra) for palabra in palabras}

# Diccionario solo con estudiantes aprobados
estudiantes = {"Ana": 85, "Luis": 45, "María": 70, "Pedro": 55, "Laura": 90}
dict_aprobados = {nombre: nota for nombre, nota in estudiantes.items() if nota >= 60}

# Conjunto con restos al dividir entre 4
set_restos = {x % 4 for x in range(21)}

# Conjunto con vocales únicas
frase = "Aprender Python es divertido"
set_vocales = {letra.lower() for letra in frase if letra.lower() in "aeiou"}

# Pruebas
print("\n--- Ejercicio 3: Dict y Set Comprehensions ---")
print(f"Cuadrados: {dict_cuadrados}")
print(f"Longitudes: {dict_longitudes}")
print(f"Aprobados: {dict_aprobados}")
print(f"Restos: {set_restos}")
print(f"Vocales: {set_vocales}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 4: zip y enumerate
# ═══════════════════════════════════════════════════════════════

# Combina listas con zip
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]
lista_tuplas = list(zip(nombres, edades, ciudades))

# Diccionario con zip
dict_personas = dict(zip(nombres, edades))

# Lista numerada con enumerate
frutas = ["manzana", "pera", "uva", "sandía"]
lista_numerada = list(enumerate(frutas, start=1))

# Pruebas
print("\n--- Ejercicio 4: zip y enumerate ---")
print(f"Tuplas combinadas: {lista_tuplas}")
print(f"Dict personas: {dict_personas}")
print(f"Lista numerada: {lista_numerada}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 5: any, all, filter, map con lambda
# ═══════════════════════════════════════════════════════════════

# any: verificar si hay algún negativo
numeros = [5, 8, -3, 12, 7]
hay_negativo = any(x < 0 for x in numeros)

# all: verificar si todos son mayores a 10
numeros2 = [15, 22, 18, 30]
todos_mayores = all(x > 10 for x in numeros2)

# filter: solo impares
numeros3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solo_impares = list(filter(lambda x: x % 2 != 0, numeros3))

# map: convertir a Celsius
fahrenheit = [32, 68, 86, 104]
celsius = list(map(lambda f: (f - 32) * 5/9, fahrenheit))

# filter + map: cuadrados de pares
numeros4 = [1, 2, 3, 4, 5, 6, 7, 8]
cuadrados_pares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros4)))

# Pruebas
print("\n--- Ejercicio 5: any, all, filter, map ---")
print(f"¿Hay algún negativo? {hay_negativo}")
print(f"¿Todos mayores a 10? {todos_mayores}")
print(f"Solo impares: {solo_impares}")
print(f"Celsius: {celsius}")
print(f"Cuadrados de pares: {cuadrados_pares}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 6: sorted con key personalizado
# ═══════════════════════════════════════════════════════════════

# Ordenar palabras por longitud
palabras = ["Python", "es", "un", "lenguaje", "poderoso"]
palabras_ordenadas = sorted(palabras, key=len)

# Ordenar productos por precio
productos = [
    {"nombre": "Laptop", "precio": 1000},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 75}
]
productos_ordenados = sorted(productos, key=lambda p: p["precio"])

# Ordenar estudiantes por nota (descendente)
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 92},
    {"nombre": "María", "nota": 78}
]
estudiantes_ordenados = sorted(estudiantes, key=lambda e: e["nota"], reverse=True)

# Pruebas
print("\n--- Ejercicio 6: sorted con key ---")
print(f"Palabras por longitud: {palabras_ordenadas}")
print(f"Productos por precio: {productos_ordenados}")
print(f"Estudiantes por nota (desc):")
for est in estudiantes_ordenados:
    print(f"  {est['nombre']}: {est['nota']}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 7: Caso Práctico - Análisis de Ventas
# ═══════════════════════════════════════════════════════════════

ventas = [
    {"producto": "Laptop", "cantidad": 5, "precio": 1000},
    {"producto": "Mouse", "cantidad": 20, "precio": 25},
    {"producto": "Teclado", "cantidad": 10, "precio": 75},
    {"producto": "Monitor", "cantidad": 8, "precio": 300},
    {"producto": "USB", "cantidad": 50, "precio": 10}
]

# Diccionario {producto: total}
dict_totales = {v["producto"]: v["cantidad"] * v["precio"] for v in ventas}

# Lista de ventas con total > 600
ventas_altas = [v for v in ventas if v["cantidad"] * v["precio"] > 600]

# Suma total de todas las ventas
total_vendido = sum(v["cantidad"] * v["precio"] for v in ventas)

# Producto con mayor total
producto_mas_vendido = max(ventas, key=lambda v: v["cantidad"] * v["precio"])

# Resumen usando zip
nombres_productos = [v["producto"] for v in ventas]
totales = [v["cantidad"] * v["precio"] for v in ventas]
productos_resumen = dict(zip(nombres_productos, totales))

# Pruebas
print("\n--- Ejercicio 7: Análisis de Ventas ---")
print(f"Totales por producto: {dict_totales}")
print(f"Ventas altas (>600): {[v['producto'] for v in ventas_altas]}")
print(f"Total vendido: ${total_vendido}")
print(f"Producto más vendido: {producto_mas_vendido['producto']} (${producto_mas_vendido['cantidad'] * producto_mas_vendido['precio']})")
print(f"Resumen: {productos_resumen}")

print("\n=== FIN DE LAS SOLUCIONES ===")

# -----------------------------------------------
# 📝 NOTAS IMPORTANTES
# -----------------------------------------------
"""
1. LIST COMPREHENSIONS:
   - Sintaxis básica: [expresion for item in iterable]
   - Con filtro: [expresion for item in iterable if condicion]
   - Con if/else: [x if condicion else y for item in iterable]
   - Más rápidas y legibles que bucles for tradicionales

2. DICT COMPREHENSIONS:
   - Sintaxis: {clave: valor for item in iterable}
   - Útil para transformar diccionarios
   - Filtrar con if: {k: v for k, v in dict.items() if condicion}

3. SET COMPREHENSIONS:
   - Sintaxis: {expresion for item in iterable}
   - Automáticamente elimina duplicados
   - Útil para obtener valores únicos

4. GENERATOR EXPRESSIONS:
   - Sintaxis: (expresion for item in iterable)
   - Ahorra memoria, genera valores on-demand
   - Úsalo con sum(), max(), min(), any(), all()

5. FUNCIONES ÚTILES:
   - zip: combina iterables elemento por elemento
   - enumerate: devuelve índice y valor
   - filter: filtra elementos que cumplen condición
   - map: aplica función a todos los elementos
   - sorted: ordena con criterio personalizado
   - any: True si al menos uno es True
   - all: True si todos son True

6. LAMBDA:
   - Funciones anónimas de una línea
   - Úsalas con filter, map, sorted
   - Sintaxis: lambda args: expresion

7. CUANDO USAR CADA UNA:
   - List comprehension: cuando necesitas la lista completa
   - Generator expression: cuando quieres iterar una vez o calcular agregado (sum, max)
   - Dict comprehension: transformar/filtrar diccionarios
   - Set comprehension: cuando necesitas valores únicos

8. BUENAS PRÁCTICAS:
   - No abuses de comprehensions anidadas (difícil de leer)
   - Si tiene más de 2 líneas, usa bucle for tradicional
   - Usa nombres de variables descriptivos
   - Prioriza legibilidad sobre brevedad extrema
"""

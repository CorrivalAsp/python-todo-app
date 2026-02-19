"""
EJERCICIOS - LECCIÓN 7: COMPREHENSIONS Y ESTRUCTURAS AVANZADAS
==============================================================

En estos ejercicios practicarás:
- List, dict y set comprehensions
- Generator expressions
- zip, enumerate, any, all
- filter, map con lambda
- sorted con key personalizado
- Métodos avanzados de diccionarios

Recuerda:
- Lee las instrucciones de cada ejercicio
- Completa los TODOs
- Ejecuta el archivo para probar tus soluciones
- Compara con solutions_07.py si te atascas
"""

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 1: List Comprehensions Básicas
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Usa list comprehensions para crear listas

# TODO: Crea lista_cubos
# - Lista de cubos (x**3) de números del 1 al 10
# - Resultado: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
lista_cubos= [ x ** 3   for x in range(1,11)]

# TODO: Crea lista_dobles
# - Lista con el doble de cada número en [5, 10, 15, 20]
# - Resultado: [10, 20, 30, 40]
lista_dobles = [ x * 2 for x in [5, 10, 15, 20]]

# TODO: Crea lista_mayusculas
# - Convierte todos los nombres a mayúsculas
nombres = ["ana", "luis", "maría", "pedro"]
# - Resultado: ["ANA", "LUIS", "MARÍA", "PEDRO"]
lista_mayusculas = [nombre.upper() for nombre in nombres]

# Pruebas (NO MODIFICAR)
print("--- Ejercicio 1: List Comprehensions Básicas ---")
print(f"Cubos 1-10: {lista_cubos}")
print(f"Dobles: {lista_dobles}")
print(f"Mayúsculas: {lista_mayusculas}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 2: List Comprehensions con Condiciones
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Usa list comprehensions con filtros (if)

# TODO: Crea multiplos_de_3
# - Solo números múltiplos de 3 del 1 al 20
# - Pista: x % 3 == 0
# - Resultado: [3, 6, 9, 12, 15, 18]
multiplos_de_3 = [ x for x in range(1, 21) if x % 3 == 0]

# TODO: Crea palabras_largas
# - Solo palabras con más de 5 letras
palabras = ["sol", "python", "gato", "programación", "luz", "desarrollo"]
# - Resultado: ["python", "programación", "desarrollo"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]

# TODO: Crea numeros_positivos
# - Solo números positivos (mayores a 0)
numeros = [-5, 3, -2, 8, 0, -1, 7, 4]
# - Resultado: [3, 8, 7, 4]
numeros_positivos = [numero for numero in numeros if numero > 0]

# TODO: Crea clasificacion
# - Convierte cada número en "positivo", "negativo" o "cero"
# - Usa operador ternario: "positivo" if x > 0 else ("negativo" if x < 0 else "cero")
numeros2 = [5, -3, 0, 8, -1]
# - Resultado: ["positivo", "negativo", "cero", "positivo", "negativo"]

clasificacion = ['positivo' if numero > 0 else ('negativo' if numero < 0 else 'cero') for numero in numeros2]
# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 2: Comprehensions con Condiciones ---")
print(f"Múltiplos de 3: {multiplos_de_3}")
print(f"Palabras largas: {palabras_largas}")
print(f"Números positivos: {numeros_positivos}")
print(f"Clasificación: {clasificacion}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 3: Dict y Set Comprehensions
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Crea diccionarios y conjuntos con comprehensions

# TODO: Crea dict_cuadrados
# - Diccionario {número: cuadrado} para números 1-5
# - Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dict_cuadrados = {numero : numero ** 2 for numero in range (1, 6)}

# TODO: Crea dict_longitudes
# - Diccionario {palabra: longitud}
palabras = ["Python", "es", "genial"]
# - Resultado: {"Python": 6, "es": 2, "genial": 6}
dict_longitudes = {palabra: len(palabra) for palabra in palabras}

# TODO: Crea dict_aprobados
# - Diccionario solo con estudiantes que tienen nota >= 60
estudiantes = {"Ana": 85, "Luis": 45, "María": 70, "Pedro": 55, "Laura": 90}
# - Resultado: {"Ana": 85, "María": 70, "Laura": 90}
dict_aprobados = {nombre: nota for nombre, nota in estudiantes.items() if nota >= 60}

# TODO: Crea set_restos
# - Conjunto con restos al dividir 0-20 entre 4
# - Pista: {x % 4 for x in range(21)}
# - Resultado: {0, 1, 2, 3}
set_restos = { x % 4 for x in range(0, 21)}

# TODO: Crea set_vocales
# - Conjunto con vocales únicas en la frase (en minúsculas)
frase = "Aprender Python es divertido"
# - Pista: {letra.lower() for letra in frase if letra.lower() in "aeiou"}
# - Resultado: {'a', 'e', 'i', 'o'}
set_vocales = {letra.lower() for letra in frase if letra.lower() in 'aeiou'}

# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 3: Dict y Set Comprehensions ---")
print(f"Cuadrados: {dict_cuadrados}")
print(f"Longitudes: {dict_longitudes}")
print(f"Aprobados: {dict_aprobados}")
print(f"Restos: {set_restos}")
print(f"Vocales: {set_vocales}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 4: zip y enumerate
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Usa zip y enumerate

# TODO: Crea lista_tuplas usando zip
# - Combina nombres, edades y ciudades en tuplas
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]
# - Pista: list(zip(nombres, edades, ciudades))
# - Resultado: [("Ana", 25, "Madrid"), ("Luis", 30, "Barcelona"), ("María", 28, "Valencia")]
lista_tuplas = list(zip(nombres, edades, ciudades))

# TODO: Crea dict_personas usando zip
# - Diccionario {nombre: edad}
# - Pista: dict(zip(nombres, edades))
# - Resultado: {"Ana": 25, "Luis": 30, "María": 28}

dict_personas = dict(zip(nombres, edades))

# TODO: Crea lista_numerada usando enumerate
# - Lista de tuplas (índice+1, fruta)
frutas = ["manzana", "pera", "uva", "sandía"]
# - Pista: list(enumerate(frutas, start=1))
# - Resultado: [(1, "manzana"), (2, "pera"), (3, "uva"), (4, "sandía")]

lista_numerada = list(enumerate(frutas, start= 1))
# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 4: zip y enumerate ---")
print(f"Tuplas combinadas: {lista_tuplas}")
print(f"Dict personas: {dict_personas}")
print(f"Lista numerada: {lista_numerada}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 5: any, all, filter, map con lambda
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Usa any, all, filter, map con funciones lambda

# TODO: Usa any para verificar si hay algún negativo
numeros = [5, 8, -3, 12, 7]
# - Pista: any(x < 0 for x in numeros)
hay_negativo = any(x < 0 for x in numeros )

# TODO: Usa all para verificar si todos son mayores a 10
numeros2 = [15, 22, 18, 30]
# - Pista: all(x > 10 for x in numeros2)
todos_mayores = all(x>10 for x in numeros2)

# TODO: Usa filter con lambda para obtener solo impares
numeros3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# - Pista: list(filter(lambda x: x % 2 != 0, numeros3))
solo_impares = list(filter(lambda x: x % 2 != 0, numeros3))

# TODO: Usa map con lambda para convertir a Celsius
# - Fórmula: celsius = (fahrenheit - 32) * 5/9
fahrenheit = [32, 68, 86, 104]
# - Pista: list(map(lambda f: (f - 32) * 5/9, fahrenheit))
celsius = list(map(lambda f: (f - 32) * 5/9, fahrenheit))

# TODO: Usa filter y map para obtener cuadrados de pares
# - Primero filtra pares, luego eleva al cuadrado
numeros4 = [1, 2, 3, 4, 5, 6, 7, 8]
# - Pista: list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros4)))
cuadrados_pares = list(map(lambda x: x**2, filter(lambda x: x% 2 == 0, numeros4)))

# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 5: any, all, filter, map ---")
print(f"¿Hay algún negativo? {hay_negativo}")
print(f"¿Todos mayores a 10? {todos_mayores}")
print(f"Solo impares: {solo_impares}")
print(f"Celsius: {celsius}")
print(f"Cuadrados de pares: {cuadrados_pares}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 6: sorted con key personalizado
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Usa sorted con lambda como key

# TODO: Ordena palabras por longitud
palabras = ["Python", "es", "un", "lenguaje", "poderoso"]
# - Pista: sorted(palabras, key=len)
palabras_ordenadas = sorted(palabras, key=len)

# TODO: Ordena productos por precio
productos = [
    {"nombre": "Laptop", "precio": 1000},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 75}
]
# - Pista: sorted(productos, key=lambda p: p["precio"])
productos_ordenados = sorted (productos, key = lambda p: p['precio'])

# TODO: Ordena estudiantes por nota (descendente)
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 92},
    {"nombre": "María", "nota": 78}
]
# - Pista: sorted(estudiantes, key=lambda e: e["nota"], reverse=True)

estudiantes_ordenados = sorted(estudiantes, key = lambda e: e['nota'], reverse = True)
# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 6: sorted con key ---")
print(f"Palabras por longitud: {palabras_ordenadas}")
print(f"Productos por precio: {productos_ordenados}")
print(f"Estudiantes por nota (desc):")
for est in estudiantes_ordenados:
    print(f"  {est['nombre']}: {est['nota']}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 7: Caso Práctico - Análisis de Ventas
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Analiza datos de ventas usando comprehensions

ventas = [
    {"producto": "Laptop", "cantidad": 5, "precio": 1000},
    {"producto": "Mouse", "cantidad": 20, "precio": 25},
    {"producto": "Teclado", "cantidad": 10, "precio": 75},
    {"producto": "Monitor", "cantidad": 8, "precio": 300},
    {"producto": "USB", "cantidad": 50, "precio": 10}
]

# TODO: Crea dict_totales
# - Diccionario {producto: cantidad * precio}
# - Usa dict comprehension
# - Resultado: {"Laptop": 5000, "Mouse": 500, "Teclado": 750, "Monitor": 2400, "USB": 500}

dict_totales = {v['producto']: v['cantidad'] * v['precio'] for v in ventas}
# TODO: Crea ventas_altas
# - Lista de productos con total > 600
# - Usa list comprehension con if
# - Pista: [{...} for v in ventas if v["cantidad"] * v["precio"] > 600]
# - Resultado: Lista de dicts de Laptop, Teclado, Monitor
ventas_altas = [v for v in ventas if v['cantidad'] * v['precio']>600]

# TODO: Calcula total_vendido
# - Suma de todos los totales (cantidad * precio)
# - Usa sum con generator expression
# - Pista: sum(v["cantidad"] * v["precio"] for v in ventas)
# - Resultado: 9150
total_vendido = sum(v['cantidad'] * v['precio'] for v in ventas)

# TODO: Encuentra producto_mas_vendido
# - Producto con mayor cantidad * precio
# - Usa max con key
# - Pista: max(ventas, key=lambda v: v["cantidad"] * v["precio"])
# - Devuelve el diccionario completo

producto_mas_vendido = max (ventas, key=lambda v: v['cantidad'] * v['precio'])
# TODO: Crea productos_resumen usando zip y dict comprehension
# - Lista de nombres de productos
# - Lista de totales
# - Combina en diccionario {nombre: total}
nombres_productos = [v["producto"] for v in ventas]
totales = [v["cantidad"] * v["precio"] for v in ventas]
# - Pista: dict(zip(nombres_productos, totales))
productos_resumen = dict(zip(nombres_productos, totales))


# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 7: Análisis de Ventas ---")
print(f"Totales por producto: {dict_totales}")
print(f"Ventas altas (>600): {[v['producto'] for v in ventas_altas]}")
print(f"Total vendido: ${total_vendido}")
print(f"Producto más vendido: {producto_mas_vendido['producto']} (${producto_mas_vendido['cantidad'] * producto_mas_vendido['precio']})")
print(f"Resumen: {productos_resumen}")

print("\n=== FIN DE LOS EJERCICIOS ===")

# -----------------------------------------------
# 🏆 CRITERIOS DE ÉXITO
# -----------------------------------------------
# Para considerar estos ejercicios completados:
# 1. Usas list comprehensions correctamente
# 2. Creas dicts y sets con comprehensions
# 3. Aplicas filtros con if en comprehensions
# 4. Usas zip y enumerate apropiadamente
# 5. Trabajas con filter, map y lambda
# 6. Ordenas con sorted y key personalizado
# 7. Combinas múltiples conceptos en casos prácticos
#
# Ejecuta: python exercises_07.py

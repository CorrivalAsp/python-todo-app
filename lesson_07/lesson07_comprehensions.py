"""
LECCIÓN 7: COMPREHENSIONS Y ESTRUCTURAS DE DATOS AVANZADAS
==========================================================

En esta lección aprenderás:
- List comprehensions (listas por comprensión)
- Dict comprehensions (diccionarios por comprensión)
- Set comprehensions (conjuntos por comprensión)
- Generator expressions (expresiones generadoras)
- Funciones útiles: zip, enumerate, any, all, filter, map
- Funciones lambda
- Métodos avanzados de diccionarios

Conceptos que ya debes conocer de lecciones anteriores:
listas, diccionarios, funciones, for loops, if/else
"""

# ═══════════════════════════════════════════════════════════════
# CONCEPTOS PREVIOS
# ═══════════════════════════════════════════════════════════════

"""
Antes de comenzar, necesitas entender estos conceptos nuevos:

1. List Comprehension
   - Forma concisa de crear listas desde iterables
   - Sintaxis: [expresion for item in iterable if condicion]
   - Ejemplo: [x**2 for x in range(5)] → [0, 1, 4, 9, 16]
   - Más rápido y legible que usar bucles for tradicionales

2. Dict Comprehension
   - Crea diccionarios de forma concisa
   - Sintaxis: {clave: valor for item in iterable if condicion}
   - Ejemplo: {x: x**2 for x in range(3)} → {0: 0, 1: 1, 2: 4}

3. Set Comprehension
   - Crea conjuntos (sin duplicados) de forma concisa
   - Sintaxis: {expresion for item in iterable if condicion}
   - Ejemplo: {x % 3 for x in range(10)} → {0, 1, 2}

4. Generator Expression
   - Similar a list comprehension pero genera valores on-demand
   - Sintaxis: (expresion for item in iterable if condicion)
   - Más eficiente en memoria que list comprehension
   - Se consume una sola vez

5. zip(lista1, lista2, ...)
   - Combina múltiples iterables elemento por elemento
   - Devuelve tuplas con elementos emparejados
   - Ejemplo: zip([1,2], ['a','b']) → [(1,'a'), (2,'b')]

6. enumerate(iterable, start=0)
   - Devuelve índice y valor al iterar
   - Ejemplo: enumerate(['a','b']) → [(0,'a'), (1,'b')]
   - Ya visto en lección anterior, aquí se refuerza

7. any(iterable)
   - Devuelve True si AL MENOS UN elemento es verdadero
   - any([False, True, False]) → True
   - any([False, False]) → False

8. all(iterable)
   - Devuelve True si TODOS los elementos son verdaderos
   - all([True, True, True]) → True
   - all([True, False, True]) → False

9. filter(funcion, iterable)
   - Filtra elementos que cumplen una condición
   - Devuelve un iterador
   - Ejemplo: filter(lambda x: x > 5, [3,6,2,8]) → [6, 8]

10. map(funcion, iterable)
    - Aplica una función a cada elemento
    - Devuelve un iterador
    - Ejemplo: map(lambda x: x*2, [1,2,3]) → [2, 4, 6]

11. lambda arguments: expression
    - Función anónima de una sola línea
    - Ejemplo: lambda x: x**2 es equivalente a def cuadrado(x): return x**2
    - Útil para funciones simples en filter, map, sorted

12. sorted(iterable, key=funcion, reverse=False)
    - Ordena elementos usando una función de clave
    - Ejemplo: sorted(["abc", "a", "abcd"], key=len) → ["a", "abc", "abcd"]
    - key determina por qué criterio ordenar

13. dict.get(clave, default=None)
    - Obtiene valor de diccionario sin error si no existe
    - Ejemplo: {"a": 1}.get("b", 0) → 0
    - Mejor que dict[clave] cuando la clave puede no existir

14. dict.setdefault(clave, default)
    - Obtiene valor, si no existe lo crea con default
    - Ejemplo: d = {}; d.setdefault("a", []).append(1)
    - Útil para diccionarios con listas/conjuntos como valores

15. Operador ternario (if/else en una línea)
    - Sintaxis: valor_si_true if condicion else valor_si_false
    - Ejemplo: "par" if x % 2 == 0 else "impar"
    - Usado dentro de comprehensions
"""

# ═══════════════════════════════════════════════════════════════
# PARTE 1: LIST COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════

print("=" * 60)
print("PARTE 1: List Comprehensions")
print("=" * 60)

# --- Forma tradicional vs Comprehension ---
print("\n--- Comparación: For tradicional vs Comprehension ---")

# Forma tradicional: crear lista de cuadrados
cuadrados_tradicional = []
for x in range(5):
    cuadrados_tradicional.append(x ** 2)
print(f"For tradicional: {cuadrados_tradicional}")

# Con list comprehension (más conciso)
cuadrados_comprehension = [x ** 2 for x in range(5)]
print(f"Comprehension:   {cuadrados_comprehension}")

# --- Comprehension con condición ---
print("\n--- List Comprehension con if (filtro) ---")

# Solo números pares
pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares 0-9: {pares}")

# Solo números mayores a 5
mayores = [x for x in range(15) if x > 5]
print(f"Mayores a 5: {mayores}")

# --- Comprehension con if/else (operador ternario) ---
print("\n--- List Comprehension con if/else ---")

# Convertir números a "par" o "impar"
clasificacion = ["par" if x % 2 == 0 else "impar" for x in range(6)]
print(f"Clasificación: {clasificacion}")

# Duplicar pares, triplicar impares
transformados = [x*2 if x % 2 == 0 else x*3 for x in range(6)]
print(f"Transformados: {transformados}")

# --- Comprehension con strings ---
print("\n--- List Comprehension con strings ---")

nombres = ["Ana", "Pedro", "María", "Juan"]

# Convertir a mayúsculas
mayusculas = [nombre.upper() for nombre in nombres]
print(f"Mayúsculas: {mayusculas}")

# Filtrar nombres largos (más de 4 letras)
largos = [nombre for nombre in nombres if len(nombre) > 4]
print(f"Nombres largos: {largos}")

# Obtener primeras letras
iniciales = [nombre[0] for nombre in nombres]
print(f"Iniciales: {iniciales}")

# --- Comprehension anidada (listas de listas) ---
print("\n--- List Comprehension anidada ---")

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Aplanar matriz (convertir a lista simple)
plana = [numero for fila in matriz for numero in fila]
print(f"Matriz: {matriz}")
print(f"Aplanada: {plana}")

# ═══════════════════════════════════════════════════════════════
# PARTE 2: DICT Y SET COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PARTE 2: Dict y Set Comprehensions")
print("=" * 60)

# --- Dict Comprehension básica ---
print("\n--- Dict Comprehension ---")

# Crear diccionario número: cuadrado
cuadrados_dict = {x: x**2 for x in range(6)}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

# Invertir un diccionario (valor: clave)
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(f"Original: {original}")
print(f"Invertido: {invertido}")

# --- Dict Comprehension con condición ---
print("\n--- Dict Comprehension con filtro ---")

# Solo números pares
pares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Solo pares: {pares_dict}")

# Nombres y longitudes (solo nombres largos)
nombres = ["Ana", "Pedro", "María", "Juan"]
nombres_largos = {nombre: len(nombre) for nombre in nombres if len(nombre) > 4}
print(f"Nombres largos con longitud: {nombres_largos}")

# --- Set Comprehension ---
print("\n--- Set Comprehension (sin duplicados) ---")

# Restos al dividir entre 3 (automáticamente elimina duplicados)
restos = {x % 3 for x in range(15)}
print(f"Restos al dividir entre 3: {restos}")  # {0, 1, 2}

# Primeras letras únicas
nombres = ["Ana", "Antonio", "Pedro", "Patricia"]
iniciales_unicas = {nombre[0] for nombre in nombres}
print(f"Iniciales únicas: {iniciales_unicas}")  # {'A', 'P'}

# ═══════════════════════════════════════════════════════════════
# PARTE 3: GENERATOR EXPRESSIONS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PARTE 3: Generator Expressions")
print("=" * 60)

print("\n--- List vs Generator ---")

# List comprehension (crea lista en memoria)
lista_cuadrados = [x**2 for x in range(5)]
print(f"List comprehension: {lista_cuadrados}")
print(f"Tipo: {type(lista_cuadrados)}")

# Generator expression (genera valores on-demand)
gen_cuadrados = (x**2 for x in range(5))
print(f"Generator: {gen_cuadrados}")
print(f"Tipo: {type(gen_cuadrados)}")

# Consumir generator con list()
print(f"Convertir a lista: {list(gen_cuadrados)}")
# Una vez consumido, está vacío
print(f"Segunda vez (vacío): {list(gen_cuadrados)}")

print("\n--- Usar generator con sum(), max(), min() ---")

# Generators son eficientes para cálculos sin guardar en memoria
gen_numeros = (x**2 for x in range(10))
suma = sum(gen_numeros)
print(f"Suma de cuadrados 0-9: {suma}")

# Otro generator para max
gen_numeros2 = (x**2 for x in range(10))
maximo = max(gen_numeros2)
print(f"Máximo: {maximo}")

# ═══════════════════════════════════════════════════════════════
# PARTE 4: FUNCIONES ÚTILES (zip, enumerate, any, all, filter, map)
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PARTE 4: Funciones Útiles")
print("=" * 60)

# --- zip() ---
print("\n--- zip: combinar iterables ---")

nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
ciudades = ["Madrid", "Barcelona", "Valencia"]

# Combinar en tuplas
combinado = list(zip(nombres, edades, ciudades))
print(f"Nombres: {nombres}")
print(f"Edades: {edades}")
print(f"Ciudades: {ciudades}")
print(f"Combinado: {combinado}")

# Crear diccionario con zip
usuarios = dict(zip(nombres, edades))
print(f"Diccionario nombres:edades {usuarios}")

# --- enumerate() ---
print("\n--- enumerate: índice + valor ---")

frutas = ["manzana", "pera", "uva"]

# Forma tradicional
print("Índices tradicionales:")
for i in range(len(frutas)):
    print(f"  {i}: {frutas[i]}")

# Con enumerate (más Pythonic)
print("Con enumerate:")
for indice, fruta in enumerate(frutas):
    print(f"  {indice}: {fruta}")

# enumerate con start personalizado
print("enumerate con start=1:")
for numero, fruta in enumerate(frutas, start=1):
    print(f"  #{numero}: {fruta}")

# --- any() y all() ---
print("\n--- any() y all() ---")

# any: ¿al menos uno es True?
numeros = [2, 4, 5, 8]
tiene_impar = any(x % 2 != 0 for x in numeros)
print(f"Números: {numeros}")
print(f"¿Tiene algún impar? {tiene_impar}")  # True

# all: ¿todos son True?
todos_pares = all(x % 2 == 0 for x in numeros)
print(f"¿Todos son pares? {todos_pares}")  # False

numeros_pares = [2, 4, 6, 8]
todos_pares2 = all(x % 2 == 0 for x in numeros_pares)
print(f"Números: {numeros_pares}")
print(f"¿Todos son pares? {todos_pares2}")  # True

# --- filter() ---
print("\n--- filter: filtrar elementos ---")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función para filtrar
def es_par(x):
    return x % 2 == 0

pares = list(filter(es_par, numeros))
print(f"Números: {numeros}")
print(f"Solo pares: {pares}")

# También funciona con lambda (veremos más adelante)
mayores_5 = list(filter(lambda x: x > 5, numeros))
print(f"Mayores a 5: {mayores_5}")

# --- map() ---
print("\n--- map: aplicar función a todos ---")

numeros = [1, 2, 3, 4, 5]

# Función para aplicar
def duplicar(x):
    return x * 2

duplicados = list(map(duplicar, numeros))
print(f"Originales: {numeros}")
print(f"Duplicados: {duplicados}")

# Convertir strings a enteros
numeros_str = ["10", "20", "30"]
numeros_int = list(map(int, numeros_str))
print(f"Strings: {numeros_str}")
print(f"Enteros: {numeros_int}")

# ═══════════════════════════════════════════════════════════════
# PARTE 5: FUNCIONES LAMBDA Y SORTED
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PARTE 5: Funciones Lambda y Sorted")
print("=" * 60)

# --- Lambda básica ---
print("\n--- Funciones Lambda ---")

# Función tradicional
def cuadrado(x):
    return x ** 2

# Equivalente con lambda
cuadrado_lambda = lambda x: x ** 2

print(f"Función tradicional cuadrado(5): {cuadrado(5)}")
print(f"Lambda cuadrado_lambda(5): {cuadrado_lambda(5)}")

# Lambda con múltiples argumentos
suma = lambda a, b: a + b
print(f"Lambda suma(3, 4): {suma(3, 4)}")

# Lambda con condicional
es_mayor = lambda x, y: x if x > y else y
print(f"Mayor entre 5 y 8: {es_mayor(5, 8)}")

# --- Lambda con filter y map ---
print("\n--- Lambda con filter y map ---")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar impares con lambda
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(f"Impares: {impares}")

# Triplicar con lambda
triplicados = list(map(lambda x: x * 3, numeros))
print(f"Triplicados: {triplicados}")

# --- sorted con key ---
print("\n--- sorted() con key ---")

# Ordenar strings por longitud
palabras = ["Python", "es", "genial", "y", "poderoso"]
por_longitud = sorted(palabras, key=len)
print(f"Original: {palabras}")
print(f"Ordenado por longitud: {por_longitud}")

# Ordenar diccionarios por valor
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "María", "edad": 28}
]

por_edad = sorted(personas, key=lambda p: p["edad"])
print(f"\nPersonas ordenadas por edad:")
for p in por_edad:
    print(f"  {p['nombre']}: {p['edad']} años")

# Ordenar en reversa
por_edad_desc = sorted(personas, key=lambda p: p["edad"], reverse=True)
print(f"Personas ordenadas por edad (descendente):")
for p in por_edad_desc:
    print(f"  {p['nombre']}: {p['edad']} años")

# ═══════════════════════════════════════════════════════════════
# PARTE 6: MÉTODOS AVANZADOS DE DICCIONARIOS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PARTE 6: Métodos Avanzados de Diccionarios")
print("=" * 60)

# --- .get() con default ---
print("\n--- dict.get() ---")

config = {"host": "localhost", "port": 8000}

# Sin .get() - lanza error si no existe
try:
    timeout = config["timeout"]
except KeyError:
    print("Error: 'timeout' no existe en config")

# Con .get() - devuelve None o default
timeout = config.get("timeout")
print(f"timeout con .get(): {timeout}")

# Con default personalizado
timeout = config.get("timeout", 30)
print(f"timeout con default: {timeout}")

print(f"host: {config.get('host', 'unknown')}")

# --- .setdefault() ---
print("\n--- dict.setdefault() ---")

# Útil para diccionarios con listas
grupos = {}

# Sin setdefault (forma tradicional)
if "A" not in grupos:
    grupos["A"] = []
grupos["A"].append("Ana")

# Con setdefault (más conciso)
grupos.setdefault("B", []).append("Luis")
grupos.setdefault("B", []).append("Laura")
grupos.setdefault("A", []).append("Antonio")

print(f"Grupos: {grupos}")

# Ejemplo: contar frecuencias con setdefault
texto = "abracadabra"
frecuencias = {}
for letra in texto:
    frecuencias[letra] = frecuencias.get(letra, 0) + 1

print(f"\nFrecuencias en '{texto}': {frecuencias}")

# --- .items(), .keys(), .values() (repaso) ---
print("\n--- .items(), .keys(), .values() ---")

usuario = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

print("Iterando con .items():")
for clave, valor in usuario.items():
    print(f"  {clave}: {valor}")

print(f"Solo claves: {list(usuario.keys())}")
print(f"Solo valores: {list(usuario.values())}")

# ═══════════════════════════════════════════════════════════════
# RESUMEN
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("RESUMEN DE LA LECCIÓN")
print("=" * 60)

print("""
✅ List Comprehension:
   [expresion for item in iterable if condicion]
   Más conciso que bucles for tradicionales

✅ Dict Comprehension:
   {clave: valor for item in iterable if condicion}
   Crea diccionarios eficientemente

✅ Set Comprehension:
   {expresion for item in iterable if condicion}
   Sin duplicados automáticamente

✅ Generator Expression:
   (expresion for item in iterable)
   Ahorra memoria, genera on-demand

✅ zip(), enumerate(), any(), all():
   Herramientas para trabajar con iterables

✅ filter() y map():
   Filtrar y transformar colecciones

✅ Lambda:
   Funciones anónimas de una línea

✅ sorted(key=...):
   Ordenar con criterio personalizado

✅ dict.get() y .setdefault():
   Manejo seguro de diccionarios
""")

print("\n" + "=" * 60)
print("Ahora estás listo para los ejercicios!")
print("Ejecuta: python exercises_07.py")
print("=" * 60)

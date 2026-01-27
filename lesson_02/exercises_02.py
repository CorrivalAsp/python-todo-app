# 🎯 EJERCICIOS LECCIÓN 2 - Funciones
# ==========================================
# Completa cada ejercicio creando las funciones solicitadas.

print("=== INICIANDO EJERCICIOS LECCIÓN 2 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Tu primera función
# -----------------------------------------------
# Instrucciones: Crea una función que salude a una persona
# y diga su lenguaje de programación favorito

# TODO: Define la función presentarse()
# - Debe recibir dos parámetros: nombre y lenguaje
# - Debe imprimir: "Hola, soy [nombre] y estoy aprendiendo [lenguaje]"
def presentarse(nombre, lenguaje):
    print(f'Hola, soy {nombre} y estoy aprendiendo {lenguaje}')

# Prueba tu función (NO MODIFICAR)

"""Presenta a una persona y su lenguaje de programación."""
print("--- Ejercicio 1: Función de presentación ---")
presentarse("Jhon", "Python")
presentarse("Ana", "JavaScript")
print()

# -----------------------------------------------
# EJERCICIO 2: Función con return
# -----------------------------------------------
# Instrucciones: Crea una función que calcule el área de un rectángulo

# TODO: Define la función calcular_area()
# - Debe recibir dos parámetros: base y altura
# - Debe DEVOLVER (return) el área (base * altura)

def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base: Base del rectángulo
        altura: Altura del rectángulo
    
    Returns:
        Área del rectángulo (base * altura)
    """
    return base * altura


print("--- Ejercicio 2: Calcular área ---")
area1 = calcular_area(5, 10)
area2 = calcular_area(7, 3)
print(f"Área de rectángulo 1 (5×10): {area1}")
print(f"Área de rectángulo 2 (7×3): {area2}")
print()
    
# -----------------------------------------------
# EJERCICIO 3: Calculadora de tiempo de estudio
# -----------------------------------------------
# Instrucciones: Crea funciones para calcular horas de estudio

# TODO: Define la función calcular_horas_mensuales()
# - Recibe: horas_por_dia
# - Devuelve: horas_por_dia * 30
def calcular_horas_mensuales(horas_por_dia):
    """Calcula horas de estudio mensuales."""
    return horas_por_dia * 30


# TODO: Define la función calcular_horas_anuales()
# - Recibe: horas_por_dia
# - Devuelve: horas_por_dia * 365
def calcular_horas_anuales(horas_por_dia):
    """Calcula horas de estudio anuales."""
    return horas_por_dia * 365

# Prueba tus funciones (NO MODIFICAR)

print("--- Ejercicio 3: Calculadora de tiempo ---")
horas_dia = 2
mensual = calcular_horas_mensuales(horas_dia)
anual = calcular_horas_anuales(horas_dia)
print(f"Si estudias {horas_dia} horas por día:")
print(f"  - Al mes: {mensual} horas")
print(f"  - Al año: {anual} horas")
print()

# -----------------------------------------------
# EJERCICIO 4: Gestor de tareas (To-Do App básica)
# -----------------------------------------------
# Instrucciones: Crea funciones para manejar una lista de tareas

# Lista de tareas (NO MODIFICAR)
mis_tareas = []

# TODO: Define la función agregar_tarea()
# - Recibe: tarea (string)
# - Agrega la tarea a la lista mis_tareas
# - Imprime: "✅ Tarea agregada: [tarea]"

def agregar_tarea(tarea):
    mis_tareas.append(tarea)
    print(f"✅ Tarea agregada: {tarea}")


# TODO: Define la función mostrar_todas_las_tareas()
# - No recibe parámetros
# - Si mis_tareas está vacía, imprime: "No hay tareas"
# - Si no, imprime cada tarea con su número (usa enumerate)
def mostrar_todas_las_tareas():
   
    if  len(mis_tareas)==0:
            print("No hay tareas")
    else:
        for numero, tarea in enumerate(mis_tareas, start= 1):
            print(f"# {numero}. {tarea}")

# TODO: Define la función total_tareas()
# - No recibe parámetros
# - Devuelve la cantidad de tareas (usa len())
def total_tareas():
    return len(mis_tareas)

# Prueba tus funciones (NO MODIFICAR)
print("--- Ejercicio 4: To-Do App ---")
agregar_tarea("Completar lección 2")
agregar_tarea("Practicar funciones")
agregar_tarea("Hacer commit en Git")
print()
mostrar_todas_las_tareas()
print(f"\nTotal: {total_tareas()} tareas")
print()

# -----------------------------------------------
# EJERCICIO 5: DESAFÍO - Función de búsqueda
# -----------------------------------------------
# Instrucciones: Crea una función que busque una tarea específica

# TODO: Define la función buscar_tarea()
# - Recibe: texto_busqueda (string)
# - Busca si alguna tarea contiene ese texto (usa 'in')
# - Devuelve True si la encuentra, False si no
# Pista: recorre mis_tareas con un for
def buscar_tarea(texto_busqueda):
    for i in mis_tareas:
        if texto_busqueda in i:
            return True
    return False


# Prueba tu función (NO MODIFICAR)
print("--- Ejercicio 5: Búsqueda ---")
encontrada1 = buscar_tarea("lección")
encontrada2 = buscar_tarea("dormir")
print(f"¿Hay tarea con 'lección'? {encontrada1}")
print(f"¿Hay tarea con 'dormir'? {encontrada2}")
print()

# -----------------------------------------------
# EJERCICIO 6: BONUS - Función con valor por defecto
# -----------------------------------------------
# Instrucciones: Crea una función para calcular el precio con descuento

# TODO: Define la función calcular_precio_final()
# - Recibe: precio, descuento (por defecto 0)
# - Devuelve: precio - (precio * descuento / 100)
# Ejemplo: precio=100, descuento=20 → resultado=80
def calcular_precio_final(precio, descuento = 0):
    return precio - (precio * descuento / 100)

# Prueba tu función (NO MODIFICAR)
print("--- Ejercicio 6: Calculadora de precios ---")
precio1 = calcular_precio_final(100, 20)  # 20% descuento
precio2 = calcular_precio_final(100)      # sin descuento
print(f"Precio con 20% descuento: ${precio1}")
print(f"Precio sin descuento: ${precio2}")
print()

# -----------------------------------------------
# EJERCICIO 7: SUPER DESAFÍO - Eliminar tarea
# -----------------------------------------------
# Instrucciones: Crea una función que elimine una tarea por su número

# TODO: Define la función eliminar_tarea()
# - Recibe: numero (int) - la posición de la tarea (empezando en 1)
# - Elimina la tarea de mis_tareas usando .pop(indice)
# - Recuerda: las listas empiezan en 0, pero mostramos desde 1
# - Imprime: "❌ Tarea eliminada: [tarea]"
# - Si el número es inválido, imprime: "Error: número inválido"

def eliminar_tarea(numero):
    if 1<= numero <= len(mis_tareas):
        tarea_eliminada= mis_tareas.pop(numero-1)
        print(f'❌ Tarea eliminada: {tarea_eliminada}')
    else:
        print("Número invalido")
    return mis_tareas

# Prueba tu función (NO MODIFICAR)
print("--- Ejercicio 7: Eliminar tareas ---")
print("Tareas antes de eliminar:")
mostrar_todas_las_tareas()
print()
eliminar_tarea(2)  # Elimina la segunda tarea
print("\nTareas después de eliminar:")
mostrar_todas_las_tareas()

print("\n=== FIN DE LOS EJERCICIOS ===")

# -----------------------------------------------
# 🏆 CRITERIOS DE ÉXITO
# -----------------------------------------------
# Para considerar estos ejercicios completados:
# 1. Todas las funciones están definidas
# 2. El programa se ejecuta sin errores
# 3. Las funciones hacen lo que se pide (verifica el output)
# 4. Usas return cuando se solicita devolver un valor
# 5. Usas print cuando se solicita mostrar algo
#
# Ejecuta: python exercises_02.py

# ✅ SOLUCIONES LECCIÓN 2 - Funciones
# ==========================================
# ⚠️ IMPORTANTE: Intenta resolver exercises_02.py ANTES de ver estas soluciones

print("=== SOLUCIONES EJERCICIOS LECCIÓN 2 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Tu primera función
# -----------------------------------------------

def presentarse(nombre, lenguaje):
    """Presenta a una persona y su lenguaje de programación."""
    print(f"Hola, soy {nombre} y estoy aprendiendo {lenguaje}")

print("--- Ejercicio 1: Función de presentación ---")
presentarse("Jhon", "Python")
presentarse("Ana", "JavaScript")
print()

# -----------------------------------------------
# EJERCICIO 2: Función con return
# -----------------------------------------------

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

def calcular_horas_mensuales(horas_por_dia):
    """Calcula horas de estudio mensuales."""
    return horas_por_dia * 30

def calcular_horas_anuales(horas_por_dia):
    """Calcula horas de estudio anuales."""
    return horas_por_dia * 365

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

mis_tareas = []

def agregar_tarea(tarea):
    """Agrega una tarea a la lista."""
    mis_tareas.append(tarea)
    print(f"✅ Tarea agregada: {tarea}")

def mostrar_todas_las_tareas():
    """Muestra todas las tareas de la lista."""
    if len(mis_tareas) == 0:
        print("No hay tareas")
    else:
        for numero, tarea in enumerate(mis_tareas, start=1):
            print(f"{numero}. {tarea}")

def total_tareas():
    """Devuelve el número total de tareas."""
    return len(mis_tareas)

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

def buscar_tarea(texto_busqueda):
    """
    Busca si alguna tarea contiene el texto especificado.
    
    Args:
        texto_busqueda: Texto a buscar
    
    Returns:
        True si encuentra el texto, False si no
    """
    for tarea in mis_tareas:
        if texto_busqueda.lower() in tarea.lower():
            return True
    return False

print("--- Ejercicio 5: Búsqueda ---")
encontrada1 = buscar_tarea("lección")
encontrada2 = buscar_tarea("dormir")
print(f"¿Hay tarea con 'lección'? {encontrada1}")
print(f"¿Hay tarea con 'dormir'? {encontrada2}")
print()

# -----------------------------------------------
# EJERCICIO 6: BONUS - Función con valor por defecto
# -----------------------------------------------

def calcular_precio_final(precio, descuento=0):
    """
    Calcula el precio final después de aplicar descuento.
    
    Args:
        precio: Precio original
        descuento: Porcentaje de descuento (0-100), por defecto 0
    
    Returns:
        Precio final con descuento aplicado
    """
    return precio - (precio * descuento / 100)

print("--- Ejercicio 6: Calculadora de precios ---")
precio1 = calcular_precio_final(100, 20)
precio2 = calcular_precio_final(100)
print(f"Precio con 20% descuento: ${precio1}")
print(f"Precio sin descuento: ${precio2}")
print()

# -----------------------------------------------
# EJERCICIO 7: SUPER DESAFÍO - Eliminar tarea
# -----------------------------------------------

def eliminar_tarea(numero):
    """
    Elimina una tarea por su número.
    
    Args:
        numero: Número de la tarea (empezando en 1)
    """
    if 1 <= numero <= len(mis_tareas):
        tarea_eliminada = mis_tareas.pop(numero - 1)  # Convertir a índice 0
        print(f"❌ Tarea eliminada: {tarea_eliminada}")
    else:
        print("Error: número inválido")

print("--- Ejercicio 7: Eliminar tareas ---")
print("Tareas antes de eliminar:")
mostrar_todas_las_tareas()
print()
eliminar_tarea(2)
print("\nTareas después de eliminar:")
mostrar_todas_las_tareas()

print("\n=== FIN DE LAS SOLUCIONES ===")

# -----------------------------------------------
# 💡 NOTAS IMPORTANTES SOBRE LAS SOLUCIONES
# -----------------------------------------------
#
# 1. Funciones sin return (Ejercicio 1, 4):
#    - Solo ejecutan acciones (print)
#    - No devuelven ningún valor
#
# 2. Funciones con return (Ejercicio 2, 3, 5, 6):
#    - Devuelven un valor que puedes guardar en una variable
#    - return termina la ejecución de la función
#
# 3. Valores por defecto (Ejercicio 6):
#    - Se especifican en la definición: def funcion(param=valor)
#    - Son opcionales al llamar la función
#
# 4. Búsqueda con 'in' (Ejercicio 5):
#    - "texto" in "texto más largo" → True
#    - .lower() hace la búsqueda case-insensitive
#
# 5. Validación de índices (Ejercicio 7):
#    - Siempre valida antes de usar .pop()
#    - 1 <= numero <= len(lista) verifica rango válido
#    - Resta 1 al convertir de número de usuario a índice

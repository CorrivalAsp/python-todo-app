# Lección 2 - Funciones y Organización del Código
# Fecha: 27 de enero 2026

print("=== LECCIÓN 2: FUNCIONES ===\n")

# -----------------------------------------------
# PARTE 1: ¿Por qué usar funciones?
# -----------------------------------------------

# SIN FUNCIONES (código repetitivo y desorganizado)
print("--- Sin funciones ---")
nombre1 = "Ana"
nombre2 = "Carlos"
print(f"¡Hola, {nombre1}! Bienvenido a Python")
print(f"¡Hola, {nombre2}! Bienvenido a Python")
print()

# CON FUNCIONES (código organizado y reutilizable)
print("--- Con funciones ---")

def saludar(nombre):
    """Saluda a una persona por su nombre."""
    print(f"¡Hola, {nombre}! Bienvenido a Python")

saludar("Ana")
saludar("Carlos")
saludar("María")
print()

# -----------------------------------------------
# PARTE 2: Anatomía de una función
# -----------------------------------------------

def nombre_de_funcion(parametro1, parametro2):
    """
    Esto es un docstring - explica qué hace la función.
    
    Args:
        parametro1: descripción del primer parámetro
        parametro2: descripción del segundo parámetro
    
    Returns:
        Lo que devuelve la función
    """
    # Aquí va el código de la función
    resultado = parametro1 + parametro2
    return resultado  # Devuelve el resultado

# -----------------------------------------------
# PARTE 3: Funciones con return
# -----------------------------------------------

def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

def multiplicar(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b

# Usar las funciones
resultado_suma = sumar(5, 3)
resultado_multiplicacion = multiplicar(4, 7)

print("--- Funciones con return ---")
print(f"5 + 3 = {resultado_suma}")
print(f"4 × 7 = {resultado_multiplicacion}")
print()

# -----------------------------------------------
# PARTE 4: Funciones para nuestra To-Do App
# -----------------------------------------------

# Lista global de tareas
tareas = []

def agregar_tarea(descripcion):
    """
    Agrega una nueva tarea a la lista.
    
    Args:
        descripcion (str): Texto de la tarea a agregar
    """
    tareas.append(descripcion)
    print(f"✅ Tarea agregada: {descripcion}")

def mostrar_tareas():
    """Muestra todas las tareas de la lista."""
    if len(tareas) == 0:
        print("📭 No hay tareas pendientes")
    else:
        print(f"📝 Tienes {len(tareas)} tarea(s):")
        for numero, tarea in enumerate(tareas, start=1):
            print(f"  {numero}. {tarea}")

def contar_tareas():
    """
    Cuenta cuántas tareas hay en la lista.
    
    Returns:
        int: Número total de tareas
    """
    return len(tareas)

# -----------------------------------------------
# PARTE 5: Usar las funciones de la To-Do App
# -----------------------------------------------

print("--- Mi To-Do App con funciones ---")

# Agregar tareas
agregar_tarea("Aprender funciones en Python")
agregar_tarea("Hacer ejercicios de la lección 2")
agregar_tarea("Revisar mi código en GitHub")

print()

# Mostrar tareas
mostrar_tareas()

print()

# Contar tareas
total = contar_tareas()
print(f"Total de tareas: {total}")

print()

# -----------------------------------------------
# PARTE 6: Funciones con valores por defecto
# -----------------------------------------------

def crear_usuario(nombre, rol="estudiante"):
    """
    Crea un usuario con nombre y rol.
    
    Args:
        nombre (str): Nombre del usuario
        rol (str): Rol del usuario (por defecto: "estudiante")
    
    Returns:
        dict: Diccionario con la información del usuario
    """
    return {
        "nombre": nombre,
        "rol": rol
    }

print("--- Valores por defecto ---")
usuario1 = crear_usuario("Ana")  # usa rol por defecto
usuario2 = crear_usuario("Carlos", "profesor")  # especifica el rol

print(f"Usuario 1: {usuario1}")
print(f"Usuario 2: {usuario2}")

print()

# -----------------------------------------------
# PARTE 7: Funciones que devuelven múltiples valores
# -----------------------------------------------

def obtener_estadisticas(numeros):
    """
    Calcula estadísticas de una lista de números.
    
    Args:
        numeros (list): Lista de números
    
    Returns:
        tuple: (suma, promedio, máximo, mínimo)
    """
    suma = sum(numeros)
    promedio = suma / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return suma, promedio, maximo, minimo

calificaciones = [85, 92, 78, 95, 88]
total, prom, mejor, peor = obtener_estadisticas(calificaciones)

print("--- Múltiples valores de retorno ---")
print(f"Calificaciones: {calificaciones}")
print(f"Total: {total}")
print(f"Promedio: {prom}")
print(f"Mejor nota: {mejor}")
print(f"Peor nota: {peor}")

print("\n=== FIN DE LA LECCIÓN 2 ===")

# -----------------------------------------------
# 💡 CONCEPTOS IMPORTANTES
# -----------------------------------------------
# 
# 1. def nombre_funcion(parametros):
#    - Define una nueva función
#
# 2. return valor
#    - Devuelve un valor y termina la función
#
# 3. Docstring ("""texto""")
#    - Documenta qué hace la función
#    - Primera línea después de def
#
# 4. Parámetros vs Argumentos
#    - Parámetros: variables en la definición (def funcion(parametro))
#    - Argumentos: valores que pasas al llamar (funcion(argumento))
#
# 5. Scope (alcance)
#    - Variables dentro de funciones solo existen ahí
#    - Variables globales existen en todo el programa

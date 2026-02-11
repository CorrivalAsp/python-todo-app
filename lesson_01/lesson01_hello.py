# Lección 1 - Mi primer programa en Python
# Fecha: 27 de enero 2026

print("=== LECCIÓN 1: FUNDAMENTOS DE PYTHON ===\n")

# -----------------------------------------------
# CONCEPTOS PREVIOS: Lo que aprenderás
# -----------------------------------------------
print("--- Conceptos Previos ---\n")

# 1. len() - Cuenta elementos en una lista
print("1. len() - Longitud de listas:")
numeros = [10, 20, 30]
print(f"   Lista: {numeros}")
print(f"   Longitud: {len(numeros)} elementos\n")

# 2. .append() - Agrega elementos al final de una lista
print("2. .append() - Agregar a listas:")
frutas = ["manzana", "pera"]
print(f"   Lista inicial: {frutas}")
frutas.append("naranja")
print(f"   Después de append: {frutas}\n")

# 3. Índices [0], [1], [2] - Acceder a elementos
print("3. Índices - Acceder a elementos:")
colores = ["rojo", "verde", "azul"]
print(f"   Lista: {colores}")
print(f"   [0] = {colores[0]} (primer elemento)")
print(f"   [1] = {colores[1]} (segundo elemento)")
print(f"   [2] = {colores[2]} (tercer elemento)\n")

# 4. for ... in - Recorrer listas
print("4. for...in - Recorrer listas:")
animales = ["perro", "gato", "pájaro"]
print(f"   Lista: {animales}")
print("   Recorriendo:")
for animal in animales:
    print(f"   - {animal}")

print("\n" + "="*50 + "\n")

# -----------------------------------------------
# INICIANDO EJERCICIOS
# -----------------------------------------------

# Esto es un comentario - Python ignora estas líneas
# Los comentarios explican qué hace el código

# 1. Imprimir un mensaje en pantalla
print("¡Hola, mundo!")
print("Este es mi primer programa en Python")

# 2. Variables - contenedores para guardar información
nombre = "Jhon Murillo"
edad = 31
es_estudiante = False

# 3. Mostrar las variables
print("Mi nombre es:", nombre)
print("Tengo", edad, "años")

# 4. Una lista simple - para guardar varias tareas
tareas = ["Aprender Python", "Crear mi proyecto", "Practicar diario", 'crear mi portafolio', 'aprender FastAPI', 'fortalecer mis habilidades']

# 5. Mostrar las tareas
print("\nMis tareas:")
print(tareas[0])  # Primera tarea (las listas empiezan en 0)
print(tareas[1])  # Segunda tarea
print(tareas[2])  # Tercera tarea
print(tareas[4])

# 6. Agregar una nueva tarea
tareas.append("Dominar FastAPI")
print("\nTarea nueva agregada!")
print("Total de tareas:", len(tareas))

# 7. Mostrar todas las tareas con un bucle
print("\nTodas mis tareas:")
for tarea in tareas:
    print("- " + tarea)

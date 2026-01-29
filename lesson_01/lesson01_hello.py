# Lección 1 - Mi primer programa en Python
# Fecha: 27 de enero 2026

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

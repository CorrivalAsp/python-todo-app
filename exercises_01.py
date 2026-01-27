# 🎯 EJERCICIOS LECCIÓN 1 - Fundamentos de Python
# ==========================================
# Completa cada ejercicio siguiendo las instrucciones.
# Ejecuta el archivo después de completar cada sección para verificar.

print("=== INICIANDO EJERCICIOS LECCIÓN 1 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Variables personales
# -----------------------------------------------
# Instrucciones: Crea 4 variables con tu información personal
# TODO: Completa las siguientes variables con tus datos reales

nombre_completo = "Jhon Edward Murillo Valdés"  # Tu nombre completo
ciudad = "Bogotá"  # Tu ciudad
lenguaje_favorito = "Python"  # Lenguaje que quieres dominar (ej: "Python")
horas_estudio_semanal = 3  # Horas que dedicarás por semana

# Muestra tus datos (NO MODIFICAR esta parte)
print("📋 Mi información:")
print(f"Me llamo {nombre_completo}, vivo en {ciudad}")
print(f"Quiero dominar {lenguaje_favorito} y estudiaré {horas_estudio_semanal} horas por semana")
print()

# -----------------------------------------------
# EJERCICIO 2: Calculadora de metas
# -----------------------------------------------
# Instrucciones: Calcula cuántas horas estudiarás en total
# TODO: Completa las operaciones matemáticas

semanas_en_un_mes = 4  # ¿Cuántas semanas tiene un mes? (aprox.)
horas_totales_mes = horas_estudio_semanal * semanas_en_un_mes  # Multiplica horas_estudio_semanal * semanas_en_un_mes

print("📊 Cálculo de tiempo:")
print(f"En un mes estudiaré {horas_totales_mes} horas de Python")
print()

# -----------------------------------------------
# EJERCICIO 3: Lista de objetivos
# -----------------------------------------------
# Instrucciones: Crea una lista con tus 3 objetivos principales
# TODO: Completa la lista con tus objetivos reales

mis_objetivos = ['Conseguir trabajo como programador', 'Crear un portafolio profesional', 'Desarrollar una API con FastAPI'
    # Agrega aquí tus 3 objetivos (ejemplo: "Conseguir trabajo como programador")
]

# TODO: Agrega un cuarto objetivo usando .append()
mis_objetivos.append('Contribuir a proyectos open source')

print("🎯 Mis objetivos de aprendizaje:")
# TODO: Usa un bucle for para mostrar cada objetivo con un número
# Pista: usa enumerate() o un contador manual
# Formato esperado:
# 1. Objetivo uno
# 2. Objetivo dos
# etc.
for numero, i in enumerate(mis_objetivos):
    print(f"#{numero+1}. {i}")

# -----------------------------------------------
# EJERCICIO 4: Gestor de proyectos simple
# -----------------------------------------------
# Instrucciones: Crea una lista de proyectos que quieres construir
# TODO: Completa el código

proyectos = ["To-Do App"]  # Ya tienes uno, agrega 2 más

# TODO: Agrega tu segundo proyecto usando .append()
proyectos.append('blog personas FASTAPI')

# TODO: Agrega tu tercer proyecto usando .append()
proyectos.append('API de gestión de inventario')

# Muestra información sobre tus proyectos
print("💼 Mis proyectos futuros:")
print(f"Total de proyectos planeados: {len(proyectos)}")
print(f"Primer proyecto: {proyectos[0]}")
# TODO: Muestra el último proyecto usando índice negativo (proyectos[-1])
print(f'Ultimo proyecto: {proyectos[-1]}')

print()

# -----------------------------------------------
# EJERCICIO 5: DESAFÍO - Organizador de tareas diarias
# -----------------------------------------------
# Instrucciones: Crea listas para organizar tu día
# TODO: Completa las tres listas

tareas_manana = ['Conectarme a la VPN del trabajo', 'Revisar emails', 'Leer documentación Python']  # Ej: "Revisar emails", "Leer documentación Python"
tareas_tarde = ['revisar contenido python', '´practicar ejercicios python', 'Almorzar']   # Ej: "Hacer ejercicios", "Ver tutorial"
tareas_noche = ['Repasar conceptos', 'Practicar código', 'Documentar aprendizajes']   # Ej: "Repasar conceptos", "Practicar código"

# TODO: Combina todas las tareas en una sola lista llamada 'todas_tareas'
# Pista: puedes usar + para unir listas
todas_tareas = tareas_manana + tareas_tarde + tareas_noche

print("📅 Mi planificación del día:")
print(f"Mañana: {tareas_manana}")
print(f"Tarde: {tareas_tarde}")
print(f"Noche: {tareas_noche}")
print(f"\nTotal de tareas del día: {len(todas_tareas)}")
print()

# -----------------------------------------------
# EJERCICIO 6: BONUS - Verificador de progreso
# -----------------------------------------------
# Instrucciones: Crea variables booleanas para trackear tu progreso
# TODO: Completa las variables

instale_python = True  # ¿Ya instalaste Python? (True/False)
cree_venv = True      # ¿Ya creaste el entorno virtual? (True/False)
ejecute_primer_programa = True  # ¿Ya ejecutaste lesson01_hello.py? (True/False)

# Contador de tareas completadas (NO MODIFICAR)
tareas_completadas = sum([instale_python, cree_venv, ejecute_primer_programa])

print("✅ Progreso de configuración:")
print(f"Python instalado: {instale_python}")
print(f"Entorno virtual creado: {cree_venv}")
print(f"Primer programa ejecutado: {ejecute_primer_programa}")
print(f"\nTareas completadas: {tareas_completadas}/3")

if tareas_completadas == 3:
    print("🎉 ¡Felicidades! Completaste la configuración inicial")
else:
    print("💪 Sigue adelante, ya casi terminas la configuración")

print("\n=== FIN DE LOS EJERCICIOS ===")

# -----------------------------------------------
# 🏆 CRITERIOS DE ÉXITO
# -----------------------------------------------
# Para considerar estos ejercicios completados:
# 1. El programa debe ejecutarse sin errores
# 2. Todas las variables deben tener valores (no vacíos ni 0)
# 3. Las listas deben tener al menos los elementos solicitados
# 4. El output debe mostrar tu información correctamente
#
# Ejecuta: python exercises_01.py
# Si ves errores, léelos cuidadosamente e intenta corregirlos

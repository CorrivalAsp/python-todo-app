# ✅ SOLUCIONES LECCIÓN 1
# ==========================================
# ⚠️ IMPORTANTE: Intenta resolver exercises_01.py ANTES de ver estas soluciones
# Aprendes más cuando luchas con el problema por ti mismo

print("=== SOLUCIONES EJERCICIOS LECCIÓN 1 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Variables personales
# -----------------------------------------------
nombre_completo = "Juan Pérez"
ciudad = "Madrid"
lenguaje_favorito = "Python"
horas_estudio_semanal = 10

print("📋 Mi información:")
print(f"Me llamo {nombre_completo}, vivo en {ciudad}")
print(f"Quiero dominar {lenguaje_favorito} y estudiaré {horas_estudio_semanal} horas por semana")
print()

# -----------------------------------------------
# EJERCICIO 2: Calculadora de metas
# -----------------------------------------------
semanas_en_un_mes = 4
horas_totales_mes = horas_estudio_semanal * semanas_en_un_mes

print("📊 Cálculo de tiempo:")
print(f"En un mes estudiaré {horas_totales_mes} horas de Python")
print()

# -----------------------------------------------
# EJERCICIO 3: Lista de objetivos
# -----------------------------------------------
mis_objetivos = [
    "Conseguir trabajo como programador",
    "Crear mi portafolio profesional",
    "Contribuir a proyectos open source"
]

mis_objetivos.append("Aprender FastAPI y crear APIs")

print("🎯 Mis objetivos de aprendizaje:")
for i, objetivo in enumerate(mis_objetivos, start=1):
    print(f"{i}. {objetivo}")
print()

# -----------------------------------------------
# EJERCICIO 4: Gestor de proyectos simple
# -----------------------------------------------
proyectos = ["To-Do App"]
proyectos.append("Blog personal con FastAPI")
proyectos.append("API de gestión de inventario")

print("💼 Mis proyectos futuros:")
print(f"Total de proyectos planeados: {len(proyectos)}")
print(f"Primer proyecto: {proyectos[0]}")
print(f"Último proyecto: {proyectos[-1]}")
print()

# -----------------------------------------------
# EJERCICIO 5: DESAFÍO - Organizador de tareas diarias
# -----------------------------------------------
tareas_manana = ["Revisar emails", "Leer documentación Python", "Desayunar saludable"]
tareas_tarde = ["Hacer ejercicios de código", "Ver tutorial de FastAPI", "Almorzar"]
tareas_noche = ["Repasar conceptos del día", "Practicar código", "Documentar aprendizajes"]

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
instale_python = True
cree_venv = True
ejecute_primer_programa = True

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

print("\n=== FIN DE LAS SOLUCIONES ===")

# -----------------------------------------------
# 💡 NOTAS IMPORTANTES SOBRE LAS SOLUCIONES
# -----------------------------------------------
# 
# 1. enumerate(lista, start=1): 
#    - Te da tanto el índice como el valor de cada elemento
#    - start=1 hace que empiece en 1 en vez de 0
#
# 2. Índices negativos (proyectos[-1]):
#    - -1 accede al último elemento
#    - -2 accede al penúltimo, etc.
#
# 3. Concatenación de listas (lista1 + lista2):
#    - Crea una nueva lista combinando ambas
#    - No modifica las listas originales
#
# 4. sum() con booleanos:
#    - True cuenta como 1
#    - False cuenta como 0
#    - Útil para contar condiciones verdaderas

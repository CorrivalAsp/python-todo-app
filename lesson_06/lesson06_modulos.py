"""
LECCIÓN 6: MÓDULOS Y ORGANIZACIÓN DE CÓDIGO
===========================================

En esta lección aprenderás:
- Importar módulos de la biblioteca estándar
- Crear tus propios módulos
- Entender __name__ == "__main__"
- Organizar código en paquetes
- Refactorizar proyectos en múltiples archivos

Conceptos que ya debes conocer de lecciones anteriores:
funciones, clases, manejo de archivos, JSON
"""

# ═══════════════════════════════════════════════════════════════
# CONCEPTOS PREVIOS
# ═══════════════════════════════════════════════════════════════

"""
Antes de comenzar, necesitas entender estos conceptos nuevos:

1. import
   - Palabra clave para importar módulos
   - Ejemplo: import math
   - Te da acceso a funcionalidades de otros archivos/librerías

2. from ... import ...
   - Importa elementos específicos de un módulo
   - Ejemplo: from math import sqrt, pi
   - Solo importa lo que necesitas

3. as (alias)
   - Renombra módulos/funciones al importar
   - Ejemplo: import datetime as dt
   - Útil para nombres largos

4. __name__
   - Variable especial que Python crea automáticamente
   - Contiene el nombre del módulo actual
   - Si el archivo se ejecuta directamente, __name__ == "__main__"

5. __init__.py
   - Archivo especial que marca una carpeta como paquete Python
   - Puede estar vacío o contener código de inicialización
   - Necesario para importar módulos de subcarpetas (antes de Python 3.3)

6. sys.path
   - Lista de rutas donde Python busca módulos
   - Puedes modificarla para agregar rutas personalizadas
   - from sys import path

7. __all__
   - Lista de nombres públicos que un módulo exporta
   - Controla qué se importa con "from modulo import *"
   - Ejemplo: __all__ = ["funcion1", "clase1"]

8. Módulo vs Paquete
   - Módulo: Un archivo .py con código Python
   - Paquete: Una carpeta con __init__.py y varios módulos

9. datetime(año, mes, día)
   - Constructor para crear fechas desde componentes individuales
   - Ejemplo: datetime(2026, 12, 25) crea fecha de Navidad
   - Orden importante: año primero, luego mes, luego día

10. datetime.strptime(texto, formato)
    - Convierte un string a objeto datetime
    - Ejemplo: datetime.strptime("15/03/2026", "%d/%m/%Y")
    - Formato: %d=día, %m=mes, %Y=año (4 dígitos)

11. .days (atributo de timedelta)
    - Extrae el número de días de una diferencia de fechas
    - Ejemplo: (fecha2 - fecha1).days
    - Devuelve un entero (puede ser negativo si fecha2 es anterior)
"""

# ═══════════════════════════════════════════════════════════════
# PARTE 1: IMPORTAR MÓDULOS DE LA BIBLIOTECA ESTÁNDAR
# ═══════════════════════════════════════════════════════════════

print("=" * 50)
print("PARTE 1: Importar Módulos Estándar")
print("=" * 50)

# Python incluye muchos módulos útiles en su biblioteca estándar
# No necesitas instalar nada adicional

# --- Ejemplo 1: Módulo math ---
import math

print("\n--- math: operaciones matemáticas ---")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Redondeo hacia arriba de 3.2: {math.ceil(3.2)}")
print(f"Redondeo hacia abajo de 3.8: {math.floor(3.8)}")

# --- Ejemplo 2: Importar funciones específicas ---
from math import sqrt, pi, pow

print("\n--- Importación específica ---")
print(f"sqrt(25) = {sqrt(25)}")  # No necesitamos math.sqrt()
print(f"pi = {pi}")
print(f"pow(2, 3) = {pow(2, 3)}")  # 2 elevado a 3

# --- Ejemplo 3: Módulo datetime ---
from datetime import datetime, timedelta

print("\n--- datetime: fechas y horas ---")
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")
print(f"Año: {ahora.year}, Mes: {ahora.month}, Día: {ahora.day}")

# Crear fecha desde componentes individuales
navidad = datetime(2026, 12, 25)  # año, mes, día
print(f"Navidad 2026: {navidad}")

# Convertir string a datetime
fecha_texto = "15/03/2026"
fecha_obj = datetime.strptime(fecha_texto, "%d/%m/%Y")
print(f"String '{fecha_texto}' convertido a datetime: {fecha_obj}")

# Calcular diferencia entre fechas
diferencia = navidad - ahora
print(f"Días hasta Navidad: {diferencia.days}")

# Sumar 7 días
una_semana = timedelta(days=7)
futuro = ahora + una_semana
print(f"En una semana será: {futuro.strftime('%Y-%m-%d')}")

# --- Ejemplo 4: Módulo random ---
import random

print("\n--- random: números aleatorios ---")
print(f"Número aleatorio entre 1 y 10: {random.randint(1, 10)}")
print(f"Número flotante entre 0 y 1: {random.random()}")

frutas = ["manzana", "pera", "uva", "sandía"]
print(f"Fruta aleatoria: {random.choice(frutas)}")

# --- Ejemplo 5: Módulo os ---
import os

print("\n--- os: interacción con el sistema operativo ---")
print(f"Directorio actual: {os.getcwd()}")
print(f"Archivos en el directorio: {os.listdir('.')[:5]}")  # Primeros 5

# --- Ejemplo 6: Alias con 'as' ---
import datetime as dt

print("\n--- Usar alias ---")
hoy = dt.datetime.now()
print(f"Usando alias 'dt': {hoy.strftime('%d/%m/%Y')}")

# ═══════════════════════════════════════════════════════════════
# PARTE 2: CREAR TUS PROPIOS MÓDULOS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("PARTE 2: Crear Módulos Propios")
print("=" * 50)

"""
Un módulo es simplemente un archivo .py con funciones y clases.
Puedes importarlo desde otros archivos.

Ejemplo de estructura:
proyecto/
├── main.py
├── utilidades.py
└── modelos.py

En main.py puedes hacer:
    from utilidades import saludar
    from modelos import Usuario
"""

# Vamos a crear un módulo de ejemplo
# (Normalmente esto estaría en un archivo separado)

print("""
Archivo: matematicas.py
-----------------------
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

PI = 3.14159
""")

print("""
Archivo: main.py
----------------
from matematicas import suma, resta, PI

resultado = suma(5, 3)
print(f"5 + 3 = {resultado}")

print(f"PI = {PI}")
""")

# ═══════════════════════════════════════════════════════════════
# PARTE 3: __name__ == "__main__"
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("PARTE 3: __name__ == '__main__'")
print("=" * 50)

"""
Cuando Python ejecuta un archivo, asigna valores especiales:

1. Si ejecutas el archivo directamente:
   __name__ = "__main__"

2. Si importas el archivo desde otro:
   __name__ = "nombre_del_archivo"

Esto te permite tener código que solo se ejecute cuando el archivo
es el principal, no cuando es importado.
"""

print(f"\nValor actual de __name__: {__name__}")

# Patrón común en Python:
def funcion_principal():
    """Código que quieres ejecutar solo cuando el archivo es principal"""
    print("Esta función solo se ejecuta si este es el archivo principal")

if __name__ == "__main__":
    funcion_principal()
    print("Este código solo se ejecuta cuando ejecutas este archivo directamente")
    print("No se ejecuta cuando importas este módulo desde otro archivo")

"""
Ejemplo práctico:

Archivo: calculadora.py
-----------------------
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# Código de prueba (solo se ejecuta si lo corres directamente)
if __name__ == "__main__":
    print("Probando calculadora...")
    print(f"10 + 5 = {sumar(10, 5)}")
    print(f"10 - 5 = {restar(10, 5)}")

Ahora puedes:
1. Ejecutar calculadora.py directamente → Las pruebas se ejecutan
2. Importar calculadora.py → Solo importas las funciones, no las pruebas
"""

# ═══════════════════════════════════════════════════════════════
# PARTE 4: PAQUETES Y ESTRUCTURA DE PROYECTOS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("PARTE 4: Paquetes")
print("=" * 50)

"""
Un paquete es una carpeta que contiene módulos y un archivo __init__.py

Estructura de ejemplo para una aplicación To-Do:

todo_app/
├── main.py
├── config.py
└── app/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   ├── tarea.py
    │   └── usuario.py
    ├── services/
    │   ├── __init__.py
    │   └── gestor_tareas.py
    └── utils/
        ├── __init__.py
        └── validaciones.py

Importaciones desde main.py:
    from app.models.tarea import Tarea
    from app.models.usuario import Usuario
    from app.services.gestor_tareas import GestorTareas
    from app.utils.validaciones import validar_email
"""

print("""
Ventajas de organizar en paquetes:
✅ Código más organizado y mantenible
✅ Evita conflictos de nombres
✅ Facilita el trabajo en equipo
✅ Permite reutilizar código
✅ Mejora la escalabilidad del proyecto
""")

# ═══════════════════════════════════════════════════════════════
# PARTE 5: EJEMPLO PRÁCTICO - REFACTORIZAR GESTOR DE TAREAS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("PARTE 5: Ejemplo Práctico")
print("=" * 50)

"""
Vamos a organizar el GestorTareas de la lección 5 en módulos:

Estructura antes (todo en un archivo):
gestor_tareas.py
└── class GestorTareas:
        def __init__(self, archivo)
        def cargar(self)
        def guardar(self)
        def agregar(self, tarea)
        def listar(self)
        def completar(self, id)

Estructura después (modular):
proyecto/
├── main.py
├── models/
│   ├── __init__.py
│   └── tarea.py          # class Tarea
└── services/
    ├── __init__.py
    └── gestor.py         # class GestorTareas
"""

# Archivo: models/tarea.py
print("\n--- models/tarea.py ---")
print("""
class Tarea:
    def __init__(self, id, titulo, completada=False):
        self.id = id
        self.titulo = titulo
        self.completada = completada
    
    def completar(self):
        self.completada = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "completada": self.completada
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["titulo"], data["completada"])
""")

# Archivo: services/gestor.py
print("\n--- services/gestor.py ---")
print("""
import json
from models.tarea import Tarea

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar()
    
    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [Tarea.from_dict(t) for t in datos]
        except FileNotFoundError:
            return []
    
    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            datos = [t.to_dict() for t in self.tareas]
            json.dump(datos, f, indent=2, ensure_ascii=False)
    
    def agregar(self, titulo):
        nuevo_id = max([t.id for t in self.tareas], default=0) + 1
        tarea = Tarea(nuevo_id, titulo)
        self.tareas.append(tarea)
        self.guardar()
        return tarea
""")

# Archivo: main.py
print("\n--- main.py ---")
print("""
from services.gestor import GestorTareas

def main():
    gestor = GestorTareas()
    
    # Agregar tareas
    gestor.agregar("Aprender módulos en Python")
    gestor.agregar("Refactorizar mi código")
    
    # Listar tareas
    for tarea in gestor.tareas:
        estado = "✅" if tarea.completada else "⬜"
        print(f"{estado} {tarea.titulo}")

if __name__ == "__main__":
    main()
""")

print("""
Ventajas de esta estructura:
✅ Separación de responsabilidades
✅ Cada archivo tiene un propósito claro
✅ Fácil de probar y mantener
✅ Modelo (Tarea) separado de la lógica (GestorTareas)
✅ main.py es simple y limpio
""")

# ═══════════════════════════════════════════════════════════════
# RESUMEN
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 50)
print("RESUMEN DE LA LECCIÓN")
print("=" * 50)

print("""
✅ Importar módulos:
   - import modulo
   - from modulo import funcion
   - import modulo as alias

✅ Biblioteca estándar:
   - math, datetime, random, os, json

✅ Crear módulos propios:
   - Archivo .py con funciones/clases
   - Se puede importar desde otros archivos

✅ __name__ == "__main__":
   - Ejecutar código solo cuando el archivo es principal
   - Útil para pruebas y scripts

✅ Paquetes:
   - Carpetas con __init__.py
   - Organizan módulos relacionados
   - Uso: from paquete.modulo import Clase

✅ Buenas prácticas:
   - Un archivo, una responsabilidad
   - Separar modelos de lógica
   - Usar __init__.py para inicialización
   - main.py como punto de entrada
""")

print("\n" + "=" * 50)
print("Ahora estás listo para los ejercicios!")
print("Ejecuta: python exercises_06.py")
print("=" * 50)

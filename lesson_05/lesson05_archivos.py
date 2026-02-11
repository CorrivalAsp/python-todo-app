# Lección 5 - Manejo de Archivos, Excepciones y JSON
# Fecha: 31 de enero 2026

print("=== LECCIÓN 5: ARCHIVOS, EXCEPCIONES Y JSON ===\n")

# -----------------------------------------------
# CONCEPTOS PREVIOS: Métodos que usaremos
# -----------------------------------------------
print("--- Conceptos Previos ---")

# 1. open() - Abre archivos
# Modos: 'r' = leer, 'w' = escribir, 'a' = agregar

# 2. close() - Cierra archivos (importante para liberar recursos)

# 3. with - Context manager (cierra automáticamente)

# 4. strip() - Elimina espacios y saltos de línea
texto = "  Hola  \n"
limpio = texto.strip()
print(f"'{texto}' -> strip() -> '{limpio}'")

# 5. ensure_ascii - Parámetro para JSON con tildes y ñ
print("\n5. ensure_ascii en JSON:")
print("   ensure_ascii=True (por defecto): convierte ñ, tildes a códigos")
print("   ensure_ascii=False: mantiene ñ, tildes como están")
import json
palabra_con_tilde = {"palabra": "Año"}
print(f"   Con True: {json.dumps(palabra_con_tilde)}")  # \u00f1
print(f"   Con False: {json.dumps(palabra_con_tilde, ensure_ascii=False)}")  # ñ

# 6. indent - Parámetro para formato legible en JSON
print("\n6. indent en JSON:")
datos = {"nombre": "Ana", "edad": 25}
print("   Sin indent:")
print(f"   {json.dumps(datos)}")
print("   Con indent=2:")
print(json.dumps(datos, indent=2))

# 7. .readlines() - Lee todas las líneas de un archivo como lista
print("\n7. .readlines() - Leer líneas como lista:")
print("   Devuelve: ['línea1\\n', 'línea2\\n', 'línea3\\n']")

# 8. .join() - Une elementos de lista en un string
print("\n8. .join() - Unir lista:")
palabras = ["Hola", "mundo", "Python"]
print(f"   Lista: {palabras}")
print(f"   ' '.join(): '{' '.join(palabras)}'")
print(f"   ', '.join(): '{', '.join(palabras)}'")

# 9. as e en except - Captura el objeto error
print("\n9. 'as e' en except:")
print("   except ValueError as e:")
print("   Permite acceder al mensaje de error")

# 10. json.dumps() - Convierte Python a JSON (string)
# 11. json.loads() - Convierte JSON (string) a Python

print("\n" + "="*50 + "\n")

# -----------------------------------------------
# PARTE 0: DICCIONARIOS (Prerequisito para JSON)
# -----------------------------------------------

print("--- Parte 0: Diccionarios ---")
print("Los diccionarios guardan pares clave-valor\n")

# Crear un diccionario
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá"
}
print(f"1. Diccionario creado: {persona}")

# Acceder a valores por clave
print(f"\n2. Acceder a valores:")
print(f"   Nombre: {persona['nombre']}")
print(f"   Edad: {persona['edad']}")
print(f"   Ciudad: {persona['ciudad']}")

# Agregar nueva clave
print(f"\n3. Agregar nueva clave:")
persona["profesion"] = "Desarrolladora"
print(f"   {persona}")

# Modificar valor existente
print(f"\n4. Modificar valor:")
persona["edad"] = 26
print(f"   Nueva edad: {persona['edad']}")

# Verificar si una clave existe
print(f"\n5. Verificar si clave existe:")
if "nombre" in persona:
    print(f"   ✅ 'nombre' existe")
if "apellido" in persona:
    print(f"   'apellido' existe")
else:
    print(f"   ❌ 'apellido' NO existe")

# Iterar sobre diccionario
print(f"\n6. Recorrer diccionario:")
for clave, valor in persona.items():
    print(f"   {clave}: {valor}")

# Diccionario con lista
print(f"\n7. Diccionario con lista (valores complejos):")
estudiante = {
    "nombre": "Carlos",
    "edad": 22,
    "materias": ["Python", "Matemáticas", "Física"]
}
print(f"   Estudiante: {estudiante}")
print(f"   Primera materia: {estudiante['materias'][0]}")

# Lista de diccionarios
print(f"\n8. Lista de diccionarios:")
contactos = [
    {"nombre": "Ana", "telefono": "3001234567"},
    {"nombre": "Carlos", "telefono": "3109876543"},
    {"nombre": "María", "telefono": "3207654321"}
]
print(f"   Total contactos: {len(contactos)}")
for contacto in contactos:
    print(f"   - {contacto['nombre']}: {contacto['telefono']}")

print("\n💡 Resumen:")
print("   - Diccionario: { 'clave': 'valor' }")
print("   - Acceso: diccionario['clave']")
print("   - Agregar/Modificar: diccionario['clave'] = valor")
print("   - Verificar: 'clave' in diccionario")
print()

# -----------------------------------------------
# PARTE 1: LECTURA Y ESCRITURA DE ARCHIVOS
# -----------------------------------------------

print("--- Parte 1: Archivos Básicos ---")

# ESCRIBIR en un archivo
print("1. Escribiendo archivo...")
archivo = open("mi_archivo.txt", "w")  # 'w' = write (escribir)
archivo.write("Hola, este es mi primer archivo\n")
archivo.write("Segunda línea de texto\n")
archivo.write("Tercera línea\n")
archivo.close()  # IMPORTANTE: Siempre cerrar
print("   ✅ Archivo 'mi_archivo.txt' creado")

# LEER un archivo
print("\n2. Leyendo archivo...")
archivo = open("mi_archivo.txt", "r")  # 'r' = read (leer)
contenido = archivo.read()  # Lee todo el archivo
archivo.close()
print("   Contenido:")
print(contenido)

# LEER línea por línea
print("3. Leyendo línea por línea...")
archivo = open("mi_archivo.txt", "r")
for linea in archivo:
    print(f"   Línea: {linea.strip()}")  # strip() quita \n
archivo.close()

# AGREGAR al archivo (sin borrar contenido existente)
print("\n4. Agregando contenido...")
archivo = open("mi_archivo.txt", "a")  # 'a' = append (agregar)
archivo.write("Cuarta línea agregada\n")
archivo.close()
print("   ✅ Línea agregada")

print()

# -----------------------------------------------
# PARTE 2: CONTEXT MANAGERS (with)
# -----------------------------------------------

print("--- Parte 2: Context Managers (with) ---")
print("El 'with' cierra automáticamente el archivo\n")

# ✅ FORMA CORRECTA: Usando 'with'
with open("archivo_con_with.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
    # No necesitas archivo.close() - se cierra automáticamente

print("1. Archivo creado con 'with'")

# Leer con 'with'
with open("archivo_con_with.txt", "r") as archivo:
    contenido = archivo.read()
    print("2. Contenido leído:")
    print(f"   {contenido}")

# Leer líneas como lista
with open("archivo_con_with.txt", "r") as archivo:
    lineas = archivo.readlines()  # Devuelve lista de líneas
    print("3. Líneas como lista:")
    for i, linea in enumerate(lineas, 1):
        print(f"   Línea {i}: {linea.strip()}")

print()

# -----------------------------------------------
# PARTE 3: MANEJO DE EXCEPCIONES (try/except)
# -----------------------------------------------

print("--- Parte 3: Manejo de Excepciones ---")

# ❌ Sin manejo de errores
print("1. Sin try/except (puede causar error):")
try:
    archivo = open("archivo_que_no_existe.txt", "r")
except FileNotFoundError:
    print("   ❌ Error: El archivo no existe")

# ✅ Con manejo de errores
print("\n2. Con try/except:")
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("   ⚠️ El archivo no se encontró, creándolo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Archivo creado automáticamente\n")
    print("   ✅ Archivo creado")

# try/except/else/finally
print("\n3. try/except/else/finally completo:")
try:
    numero = int("42")  # Esto funciona
    print(f"   Número convertido: {numero}")
except ValueError:
    print("   ❌ Error: No es un número válido")
else:
    print("   ✅ Conversión exitosa (else se ejecuta si NO hay error)")
finally:
    print("   🔄 Finally siempre se ejecuta (error o no)")

# Ejemplo con error
print("\n4. Ejemplo con error:")
try:
    numero = int("abc")  # Esto falla
    print(f"   Número: {numero}")
except ValueError as e:
    print(f"   ❌ Error capturado: {e}")
else:
    print("   Este mensaje NO se mostrará")
finally:
    print("   🔄 Finally se ejecuta igual")

print()

# -----------------------------------------------
# PARTE 4: TRABAJO CON JSON
# -----------------------------------------------

print("--- Parte 4: Trabajo con JSON ---")

import json

# Python → JSON (serialización)
print("1. Convirtiendo Python a JSON:")
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Bogotá",
    "habilidades": ["Python", "JavaScript", "SQL"]
}

# json.dumps() - Convierte diccionario a string JSON
json_string = json.dumps(persona, indent=2)  # indent=2 para formato legible
print("   Diccionario Python:")
print(f"   {persona}")
print("\n   JSON string:")
print(json_string)

# Guardar JSON en archivo
print("\n2. Guardando JSON en archivo:")
with open("persona.json", "w", encoding="utf-8") as archivo:
    json.dump(persona, archivo, indent=2, ensure_ascii=False)
print("   ✅ Archivo 'persona.json' creado")

# Leer JSON desde archivo
print("\n3. Leyendo JSON desde archivo:")
with open("persona.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)  # Convierte JSON a diccionario Python
    print(f"   Nombre: {datos['nombre']}")
    print(f"   Edad: {datos['edad']}")
    print(f"   Habilidades: {', '.join(datos['habilidades'])}")

# JSON string → Python (deserialización)
print("\n4. Convirtiendo JSON string a Python:")
json_texto = '{"producto": "Laptop", "precio": 1200, "stock": 5}'
producto = json.loads(json_texto)  # Convierte string JSON a diccionario
print(f"   Producto: {producto['producto']}")
print(f"   Precio: ${producto['precio']}")

print()

# -----------------------------------------------
# PARTE 5: EJEMPLO PRÁCTICO - Sistema de Tareas
# -----------------------------------------------

print("--- Parte 5: Sistema de Tareas con Persistencia ---")

class GestorTareas:
    """Sistema de tareas que guarda en archivo JSON."""
    
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()
    
    def cargar_tareas(self):
        """Carga tareas desde archivo JSON."""
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"   ℹ️ Archivo '{self.archivo}' no existe, creando lista vacía")
            return []
        except json.JSONDecodeError:
            print(f"   ⚠️ Error al leer JSON, creando lista vacía")
            return []
    
    def guardar_tareas(self):
        """Guarda tareas en archivo JSON."""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.tareas, f, indent=2, ensure_ascii=False)
            print(f"   ✅ Tareas guardadas en '{self.archivo}'")
        except Exception as e:
            print(f"   ❌ Error al guardar: {e}")
    
    def agregar(self, titulo, descripcion=""):
        """Agrega una nueva tarea."""
        tarea = {
            "id": len(self.tareas) + 1,
            "titulo": titulo,
            "descripcion": descripcion,
            "completada": False
        }
        self.tareas.append(tarea)
        self.guardar_tareas()
        print(f"   ✅ Tarea '{titulo}' agregada")
    
    def listar(self):
        """Muestra todas las tareas."""
        if not self.tareas:
            print("   📝 No hay tareas")
            return
        
        print(f"   📝 Total de tareas: {len(self.tareas)}")
        for tarea in self.tareas:
            estado = "✅" if tarea["completada"] else "⬜"
            print(f"   {estado} [{tarea['id']}] {tarea['titulo']}")
            if tarea["descripcion"]:
                print(f"      └─ {tarea['descripcion']}")
    
    def completar(self, id_tarea):
        """Marca una tarea como completada."""
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                self.guardar_tareas()
                print(f"   ✅ Tarea {id_tarea} marcada como completada")
                return
        print(f"   ❌ Tarea {id_tarea} no encontrada")

# Usar el sistema
print("\n🚀 Probando el sistema de tareas:\n")
gestor = GestorTareas()

print("1. Agregando tareas:")
gestor.agregar("Estudiar Python", "Lección 5: Archivos y JSON")
gestor.agregar("Hacer ejercicios", "Completar todos los ejercicios")
gestor.agregar("Hacer commit", "Guardar cambios en Git")

print("\n2. Listando tareas:")
gestor.listar()

print("\n3. Completando primera tarea:")
gestor.completar(1)

print("\n4. Listando tareas actualizadas:")
gestor.listar()

print("\n" + "="*50)
print("🎯 CONCEPTOS APRENDIDOS:")
print("  1. ✅ Leer/escribir archivos (open, read, write)")
print("  2. ✅ Context managers (with)")
print("  3. ✅ Manejo de excepciones (try/except/finally)")
print("  4. ✅ Trabajo con JSON (dumps, loads, dump, load)")
print("  5. ✅ Aplicación práctica: Sistema con persistencia")
print("="*50)

# 🎯 SOLUCIONES LECCIÓN 5 - Archivos, Excepciones y JSON
# ==========================================

print("=== SOLUCIONES LECCIÓN 5 ===\n")

import json

# -----------------------------------------------
# EJERCICIO 1: Escritura y Lectura Básica
# -----------------------------------------------

def escribir_mensaje(archivo, mensaje):
    """Escribe un mensaje en un archivo."""
    archivo_obj = open(archivo, "w")
    archivo_obj.write(mensaje)
    archivo_obj.close()
    print(f"Mensaje guardado en {archivo}")

def leer_mensaje(archivo):
    """Lee el contenido de un archivo."""
    archivo_obj = open(archivo, "r")
    contenido = archivo_obj.read()
    archivo_obj.close()
    return contenido

# Pruebas
print("--- Ejercicio 1: Lectura y Escritura Básica ---")
escribir_mensaje("mensaje.txt", "Hola desde Python!")
contenido = leer_mensaje("mensaje.txt")
print(f"Contenido leído: {contenido}")
print()

# -----------------------------------------------
# EJERCICIO 2: Uso de Context Manager (with)
# -----------------------------------------------

def escribir_con_with(archivo, mensaje):
    """Escribe un mensaje usando context manager."""
    with open(archivo, "w") as f:
        f.write(mensaje)
    print("✅ Mensaje guardado con 'with'")

def leer_con_with(archivo):
    """Lee un archivo usando context manager."""
    with open(archivo, "r") as f:
        contenido = f.read()
    return contenido

# Pruebas
print("--- Ejercicio 2: Context Manager ---")
escribir_con_with("mensaje_with.txt", "Usando context manager")
contenido = leer_con_with("mensaje_with.txt")
print(f"Contenido: {contenido}")
print()

# -----------------------------------------------
# EJERCICIO 3: Manejo de Excepciones
# -----------------------------------------------

def leer_seguro(archivo):
    """Lee un archivo con manejo de errores."""
    try:
        with open(archivo, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Archivo no encontrado"

# Pruebas
print("--- Ejercicio 3: Manejo de Excepciones ---")
resultado1 = leer_seguro("mensaje_with.txt")
print(f"Archivo existente: {resultado1}")
resultado2 = leer_seguro("no_existe.txt")
print(f"Archivo inexistente: {resultado2}")
print()

# -----------------------------------------------
# EJERCICIO 4: Agregar Líneas a un Archivo
# -----------------------------------------------

def agregar_linea(archivo, linea):
    """Agrega una línea al final del archivo."""
    with open(archivo, "a") as f:
        f.write(linea + "\n")
    print("Línea agregada")

def leer_lineas(archivo):
    """Lee todas las líneas de un archivo."""
    with open(archivo, "r") as f:
        return f.readlines()

# Pruebas
print("--- Ejercicio 4: Agregar Líneas ---")
agregar_linea("log.txt", "Primera entrada")
agregar_linea("log.txt", "Segunda entrada")
agregar_linea("log.txt", "Tercera entrada")
lineas = leer_lineas("log.txt")
print(f"Total de líneas: {len(lineas)}")
for i, linea in enumerate(lineas, 1):
    print(f"  {i}. {linea.strip()}")
print()

# -----------------------------------------------
# EJERCICIO 5: Conversión Python ↔ JSON
# -----------------------------------------------

def diccionario_a_json(diccionario):
    """Convierte un diccionario a JSON string."""
    return json.dumps(diccionario, indent=2)

def json_a_diccionario(json_string):
    """Convierte un JSON string a diccionario."""
    return json.loads(json_string)

# Pruebas
print("--- Ejercicio 5: Conversión Python ↔ JSON ---")
persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Medellín"}
json_str = diccionario_a_json(persona)
print("JSON generado:")
print(json_str)

datos = json_a_diccionario(json_str)
print(f"\nDiccionario recuperado: {datos}")
print(f"Nombre: {datos['nombre']}, Edad: {datos['edad']}")
print()

# -----------------------------------------------
# EJERCICIO 6: Guardar y Cargar JSON
# -----------------------------------------------

def guardar_json(archivo, datos):
    """Guarda datos en un archivo JSON."""
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    print(f"Datos guardados en {archivo}")

def cargar_json(archivo):
    """Carga datos desde un archivo JSON."""
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Pruebas
print("--- Ejercicio 6: Guardar y Cargar JSON ---")
estudiante = {
    "nombre": "María",
    "edad": 22,
    "carrera": "Ingeniería",
    "materias": ["Python", "Matemáticas", "Física"]
}
guardar_json("estudiante.json", estudiante)
datos_cargados = cargar_json("estudiante.json")
print(f"Estudiante: {datos_cargados['nombre']}")
print(f"Materias: {', '.join(datos_cargados['materias'])}")

datos_vacios = cargar_json("inexistente.json")
print(f"Archivo inexistente devuelve: {datos_vacios}")
print()

# -----------------------------------------------
# EJERCICIO 7: DESAFÍO - Agenda de Contactos
# -----------------------------------------------

class Agenda:
    """Agenda de contactos con persistencia en JSON."""
    
    def __init__(self, archivo="contactos.json"):
        """Inicializa la agenda y carga contactos."""
        self.archivo = archivo
        self.contactos = self.cargar()
    
    def cargar(self):
        """Carga contactos desde archivo JSON."""
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def guardar(self):
        """Guarda contactos en archivo JSON."""
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.contactos, f, indent=2, ensure_ascii=False)
    
    def agregar(self, nombre, telefono, email):
        """Agrega un nuevo contacto."""
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        }
        self.contactos.append(contacto)
        self.guardar()
        print(f"✅ Contacto {nombre} agregado")
    
    def listar(self):
        """Lista todos los contactos."""
        if not self.contactos:
            print("📇 No hay contactos")
            return
        
        for contacto in self.contactos:
            print(f"👤 {contacto['nombre']} - Tel: {contacto['telefono']} - Email: {contacto['email']}")
    
    def buscar(self, nombre):
        """Busca un contacto por nombre."""
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre.lower():
                return contacto
        return None

# Pruebas
print("--- Ejercicio 7: Agenda de Contactos ---")
agenda = Agenda("mi_agenda.json")

print("1. Agregando contactos:")
agenda.agregar("Ana García", "3001234567", "ana@email.com")
agenda.agregar("Carlos López", "3109876543", "carlos@email.com")
agenda.agregar("María Pérez", "3207654321", "maria@email.com")

print("\n2. Listando contactos:")
agenda.listar()

print("\n3. Buscando contacto:")
contacto = agenda.buscar("carlos lópez")
if contacto:
    print(f"Encontrado: {contacto['nombre']} - {contacto['telefono']}")
else:
    print("No encontrado")

print("\n4. Verificando persistencia (creando nueva instancia):")
agenda2 = Agenda("mi_agenda.json")
print(f"Contactos cargados: {len(agenda2.contactos)}")
agenda2.listar()

print("\n=== FIN DE LAS SOLUCIONES ===")

# -----------------------------------------------
# 💡 EXPLICACIONES CLAVE
# -----------------------------------------------
"""
1. MODOS DE APERTURA:
   - 'r' (read): Leer archivo (debe existir)
   - 'w' (write): Escribir (crea o sobrescribe)
   - 'a' (append): Agregar al final (no borra)

2. CONTEXT MANAGER (with):
   - Cierra automáticamente el archivo
   - Maneja errores mejor
   - SIEMPRE preferir 'with' sobre open/close manual

3. TRY/EXCEPT:
   - try: código que puede fallar
   - except: qué hacer si falla
   - else: se ejecuta si NO hay error
   - finally: SIEMPRE se ejecuta

4. JSON:
   - json.dumps(): dict → string
   - json.loads(): string → dict
   - json.dump(): dict → archivo
   - json.load(): archivo → dict

5. ENCODING:
   - encoding="utf-8": para caracteres especiales (ñ, tildes)
   - ensure_ascii=False: mantiene caracteres UTF-8

6. PERSISTENCIA:
   - Guardar datos en archivos para no perderlos
   - Cargar datos al iniciar la aplicación
   - Patrón común en aplicaciones reales
"""

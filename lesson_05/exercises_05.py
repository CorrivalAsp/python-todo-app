# 🎯 EJERCICIOS LECCIÓN 5 - Archivos, Excepciones y JSON
# ==========================================
# Completa cada ejercicio usando archivos, try/except y JSON

print("=== INICIANDO EJERCICIOS LECCIÓN 5 ===\n")

import json

# -----------------------------------------------
# EJERCICIO 1: Escritura y Lectura Básica
# -----------------------------------------------
# Instrucciones: Crea funciones para escribir y leer archivos

# TODO: Define la función escribir_mensaje(archivo, mensaje)
# - Abre el archivo en modo 'w'
# - Escribe el mensaje
# - Cierra el archivo
# - Imprime: "Mensaje guardado en [archivo]"

def escribir_mensaje(archivo, mensaje):
    "Función donde se crea el archivo txt y guarda un mensaje"
    archivo = open(archivo,"w")
    archivo.write(mensaje)
    archivo.close()
    print(f'Mensaje guardado en [archivo]')
    

# TODO: Define la función leer_mensaje(archivo)
# - Abre el archivo en modo 'r'
# - Lee el contenido
# - Cierra el archivo
# - Devuelve el contenido
def leer_mensaje(archivo):
    "Funcion en donde se lee el contenido del archivo txt"
    archivo = open (archivo,"r")
    mensaje = archivo.read()
    archivo.close()
    return mensaje

# Pruebas (NO MODIFICAR)
print("--- Ejercicio 1: Lectura y Escritura Básica ---")
escribir_mensaje("mensaje.txt", "Hola desde Python!")
contenido = leer_mensaje("mensaje.txt")
print(f"Contenido leído: {contenido}")
print()

# -----------------------------------------------
# EJERCICIO 2: Uso de Context Manager (with)
# -----------------------------------------------
# Instrucciones: Reescribe las funciones usando 'with'

# TODO: Define la función escribir_con_with(archivo, mensaje)
# - Usa 'with open()' en modo 'w'
# - Escribe el mensaje
# - Imprime: "✅ Mensaje guardado con 'with'"

def escribir_con_with(archivo, mensaje):
    "Funcion donde se crea el archivo txt con with"
    with open("mensaje_with.txt", "w") as archivo:
        archivo.write(mensaje)
        print(f"✅ Mensaje guardado con 'with'")

# TODO: Define la función leer_con_with(archivo)
# - Usa 'with open()' en modo 'r'
# - Lee y devuelve el contenido
def leer_con_with(archivo):
    "Funcion que lee el mensaje con with y devuelve el contenido"
    with open("mensaje_with.txt", "r") as archivo:
        contenido = archivo.read()
        return f'{contenido}'


# Pruebas (NO MODIFICAR)
print("--- Ejercicio 2: Context Manager ---")
escribir_con_with("mensaje_with.txt", "Usando context manager")
contenido = leer_con_with("mensaje_with.txt")
print(f"Contenido: {contenido}")
print()

# -----------------------------------------------
# EJERCICIO 3: Manejo de Excepciones
# -----------------------------------------------
# Instrucciones: Lee un archivo con manejo de errores

# TODO: Define la función leer_seguro(archivo)
# - Usa try/except con FileNotFoundError
# - Si el archivo existe: devuelve el contenido
# - Si NO existe: devuelve "Archivo no encontrado"
# - Usa 'with' para abrir el archivo
def leer_seguro(archivo):
    "Método que lee un archivo txt con exepcion de error"
    try:
        with open(archivo,"r") as archivo:
           mensaje = archivo.read()
           archivo.close()
           return f'{mensaje}'
    except FileNotFoundError:
        return f"Archivo no encontrado"

# Pruebas (NO MODIFICAR)
print("--- Ejercicio 3: Manejo de Excepciones ---")
resultado1 = leer_seguro("mensaje_with.txt")  # Existe
print(f"Archivo existente: {resultado1}")
resultado2 = leer_seguro("no_existe.txt")  # No existe
print(f"Archivo inexistente: {resultado2}")
print()

# -----------------------------------------------
# EJERCICIO 4: Agregar Líneas a un Archivo
# -----------------------------------------------
# Instrucciones: Agrega contenido sin borrar lo existente

# TODO: Define la función agregar_linea(archivo, linea)
# - Usa 'with open()' en modo 'a' (append)
# - Agrega la línea al archivo
# - Asegúrate de agregar '\n' al final
# - Imprime: "Línea agregada"
def agregar_linea(archivo, linea):
    "Funcion que agrega nuevas lineas al archivo ya creado"
    with open(archivo, 'a') as archive:
        archive.write(f'{linea} \n')
        print(f'Línea agregada')

# TODO: Define la función leer_lineas(archivo)
# - Usa 'with open()' en modo 'r'
# - Lee todas las líneas con readlines()
# - Devuelve la lista de líneas
def leer_lineas(archivo):
    "Funcion que devuelve en lista el contenido del txt"
    with open(archivo, 'r') as archive:
        lineas = archive.readlines()
        return lineas

# Pruebas (NO MODIFICAR)
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
# Instrucciones: Trabaja con diccionarios y JSON

# TODO: Define la función diccionario_a_json(diccionario)
# - Usa json.dumps() para convertir a JSON string
# - Usa indent=2 para formato legible
# - Devuelve el string JSON
def diccionario_a_json(diccionario):
    "funcion que devuelve un diccionario a tipo JSON"
    json_str= json.dumps(diccionario, indent= 2, ensure_ascii=False)
    return json_str
# TODO: Define la función json_a_diccionario(json_string)
# - Usa json.loads() para convertir a diccionario
# - Devuelve el diccionario
def json_a_diccionario(json_string):
    "funcion que devuelve un JSON a un diccionario"
    datos = json.loads(json_string)
    return datos

# Pruebas (NO MODIFICAR)
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
# Instrucciones: Guarda diccionarios en archivos JSON

# TODO: Define la función guardar_json(archivo, datos)
# - Usa 'with open()' en modo 'w' con encoding="utf-8"
# - Usa json.dump() para guardar datos
# - Usa indent=2 y ensure_ascii=False
# - Imprime: "Datos guardados en [archivo]"
def guardar_json(archivo, datos):
    "Funcion que guarda un diccionario con informacion en tipo JSON"
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
        print(f"Datos guardados en {archivo}")


# TODO: Define la función cargar_json(archivo)
# - Usa try/except con FileNotFoundError
# - Si existe: carga con json.load() y devuelve datos
# - Si no existe: devuelve diccionario vacío {}
# - Usa encoding="utf-8"
def cargar_json(archivo):
    "Función que carga el archivo json y lee el diccionario"
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'No existe el diccionario, creandolo...')
        return {}

# Pruebas (NO MODIFICAR)
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

# Intentar cargar archivo inexistente
datos_vacios = cargar_json("inexistente.json")
print(f"Archivo inexistente devuelve: {datos_vacios}")
print()

# -----------------------------------------------
# EJERCICIO 7: DESAFÍO - Agenda de Contactos
# -----------------------------------------------
# Instrucciones: Crea una clase Agenda que guarde contactos en JSON

# TODO: Define la clase Agenda
# - Constructor: __init__(self, archivo="contactos.json")
#   * self.archivo = archivo
#   * self.contactos = self.cargar() (llama al método cargar)
class Agenda:
    def __init__(self, archivo='contactos.json'):
        "Constructor que inicia el argumento de archivo y utiliza el método de cargar"
        self.archivo = archivo
        self.contactos= self.cargar()

# - Método cargar(self):
#   * Usa try/except con FileNotFoundError
#   * Si existe: carga y devuelve lista de contactos
#   * Si no existe: devuelve lista vacía []
    def cargar(self):
        "Método que carga el archivo json y lo lee"
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"No esxiste la fila, creandola...")
            return []


# - Método guardar(self):
#   * Guarda self.contactos en self.archivo
#   * Usa json.dump con indent=2
    def guardar(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.contactos, f, indent=2, ensure_ascii= False)
        except Exception as e:
            print(f"   ❌ Error al guardar contacto: {e}")

# - Método agregar(self, nombre, telefono, email):
#   * Crea diccionario: {"nombre": nombre, "telefono": telefono, "email": email}
#   * Agrega a self.contactos
#   * Llama a self.guardar()
#   * Imprime: "✅ Contacto [nombre] agregado"
    def agregar (self, nombre, telefono, email):
        "método que agrega un contacto al diccionario"
        contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
        self.contactos.append(contacto)
        self.guardar()
        print(f'✅ Contacto {nombre} agregado')
        

# - Método listar(self):
#   * Si está vacía: imprime "📇 No hay contactos"
#   * Si no: imprime cada contacto en formato:
#     "👤 [nombre] - Tel: [telefono] - Email: [email]"
    def listar(self):
        "método que muestra los contactos disponibles"
        if not self.contactos:
            print(f'📇 No hay contactos')
            return
        print(f'Contactos Disponibles: {len(self.contactos)}')
        for contacto in self.contactos:
            print(f'Nombre: [{contacto["nombre"]}], Tel: [{contacto['telefono']}], Email: [{contacto['email']}]')
# - Método buscar(self, nombre):
#   * Busca contacto por nombre (case-insensitive)
#   * Si encuentra: devuelve el diccionario del contacto
#   * Si no: devuelve None
    def buscar(self, nombre):
        "Método que busca el contacto por su nombre"
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre.lower():
                return contacto
        return None




# Pruebas (NO MODIFICAR)
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

print("\n=== FIN DE LOS EJERCICIOS ===")

# -----------------------------------------------
# 🏆 CRITERIOS DE ÉXITO
# -----------------------------------------------
# Para considerar estos ejercicios completados:
# 1. Usas open() y close() correctamente
# 2. Usas 'with' para context managers
# 3. Manejas excepciones con try/except
# 4. Trabajas con JSON (dumps, loads, dump, load)
# 5. Tu clase Agenda guarda y carga datos correctamente
#
# Ejecuta: python exercises_05.py

"""
EJERCICIOS - LECCIÓN 6: MÓDULOS Y ORGANIZACIÓN DE CÓDIGO
========================================================

En estos ejercicios practicarás:
- Importar y usar módulos de la biblioteca estándar
- Crear tus propios módulos
- Usar __name__ == "__main__"
- Organizar código en estructura modular

Recuerda:
- Lee las instrucciones de cada ejercicio
- Completa los TODOs
- Ejecuta el archivo para probar tus soluciones
- Compara con solutions_06.py si te atascas
"""

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 1: Usar módulos de la biblioteca estándar
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Usa módulos estándar para completar estas funciones

# TODO: Importa los módulos necesarios arriba
# import ...
import json
import math
from datetime import datetime
import random

# TODO: Crea función calcular_raiz_cuadrada(numero)
# - Usa math.sqrt para calcular la raíz
# - Devuelve el resultado
# - Ejemplo: calcular_raiz_cuadrada(25) → 5.0

def calcular_raiz_cuadrada(numero):
    "módulo que calcula la raiz cuadrada"
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada 

# TODO: Crea función obtener_fecha_actual()
# - Usa datetime.now() para obtener la fecha actual
# - Devuelve un string en formato "DD/MM/YYYY"
# - Ejemplo: obtener_fecha_actual() → "04/02/2026"
def obtener_fecha_actual():
    "método que da la fecha actual"
    hoy = datetime.now()
    return hoy.strftime('%d/%m/%Y')

# TODO: Crea función numero_aleatorio(min, max)
# - Usa random.randint para generar número aleatorio
# - Devuelve número entre min y max (inclusive)
# - Ejemplo: numero_aleatorio(1, 10) → 7
def numero_aleatorio(min, max):
    "Método que genera un numero aleatorio"
    return random.randint(min, max)

# Pruebas (NO MODIFICAR)
print("--- Ejercicio 1: Biblioteca Estándar ---")
print(f"Raíz cuadrada de 144: {calcular_raiz_cuadrada(144)}")
print(f"Fecha actual: {obtener_fecha_actual()}")
print(f"Número aleatorio: {numero_aleatorio(1, 100)}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 2: Importaciones específicas
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Importa solo lo que necesitas

# TODO: Importa solo pi y ceil de math
from math import pi, ceil

# TODO: Crea función calcular_area_circulo(radio)
# - Usa pi para calcular el área: pi * radio ** 2
# - Usa ceil para redondear hacia arriba
# - Devuelve el área redondeada
# - Ejemplo: calcular_area_circulo(5) → 79 (ceil de 78.54)

def calcular_area_circulo(radio):
    "Método que calcula el area de un circulo"
    area = (pi * radio**2)
    return ceil(area)

# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 2: Importaciones Específicas ---")
print(f"Área de círculo con radio 3: {calcular_area_circulo(3)}")
print(f"Área de círculo con radio 7: {calcular_area_circulo(7)}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 3: Trabajar con fechas
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Crea funciones para manejar fechas

# TODO: Importa datetime y timedelta
from datetime import datetime, timedelta

# TODO: Crea función dias_hasta_fecha(dia, mes, año)
# - Crea un objeto datetime con la fecha objetivo
# - Obtén la fecha actual con datetime.now()
# - Calcula la diferencia: fecha_objetivo - fecha_actual
# - Devuelve el número de días (puede ser negativo si ya pasó)
# - Ejemplo: dias_hasta_fecha(25, 12, 2026) → días hasta Navidad

def dias_hasta_fecha(dia, mes, año):
    "Función que devuelve la diferencia de la fecha actual de la ingresada a la función"
    fecha_medir = datetime(año, mes, dia)
    fecha_actual= datetime.now()
    diferencia = fecha_medir - fecha_actual
    return diferencia.days


# TODO: Crea función agregar_dias(fecha_str, dias)
# - fecha_str en formato "DD/MM/YYYY"
# - Convierte el string a datetime: datetime.strptime(fecha_str, "%d/%m/%Y")
# - Suma los días usando timedelta(days=dias)
# - Devuelve nueva fecha en formato "DD/MM/YYYY"
# - Ejemplo: agregar_dias("01/01/2026", 30) → "31/01/2026"

def agregar_dias(fecha_str, dias):
    "Función que convierte una fecha str a formato time y le suma la cantidad de día s ingresados"
    fecha_date = datetime.strptime(fecha_str, "%d/%m/%Y")
    dias_agregados = timedelta(days=dias)
    total_fechas = fecha_date + dias_agregados
    return f'{total_fechas.strftime("%d/%m/%Y")}'
# Pruebas (NO MODIFICAR):

print("\n--- Ejercicio 3: Fechas ---")
print(f"Días hasta 01/01/2027: {dias_hasta_fecha(1, 1, 2027)}")
print(f"15 días después de 01/02/2026: {agregar_dias('01/02/2026', 15)}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 4: Crear módulo de utilidades (simulado)
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Crea funciones que podrían estar en un módulo separado

# TODO: Crea función validar_email(email)
# - Verifica que el email contenga "@" y "."
# - El "@" debe estar antes que el "."
# - Devuelve True si es válido, False si no
# - Ejemplo: validar_email("juan@email.com") → True
# - Ejemplo: validar_email("juan.com") → False
def validar_email(email):
   if "@" not in email or  "." not  in email:
       return False
   
   posicion_arroba = email.index("@")
   posicion_punto = email.rindex(".")
   return posicion_arroba < posicion_punto

# TODO: Crea función validar_telefono(telefono)
# - El teléfono debe tener exactamente 10 dígitos
# - Usa .isdigit() para verificar que solo tiene números
# - Devuelve True si es válido, False si no
# - Ejemplo: validar_telefono("3001234567") → True
# - Ejemplo: validar_telefono("300-123-45") → False
def validar_telefono(telefono):
    if len(telefono) == 10:
        if telefono.isdigit():
            return True
        else: 
            return False
    return False

# TODO: Crea función limpiar_texto(texto)
# - Elimina espacios al inicio y final con .strip()
# - Convierte a minúsculas con .lower()
# - Devuelve el texto limpio
# - Ejemplo: limpiar_texto("  HOLA Mundo  ") → "hola mundo"
def limpiar_texto(texto):
    "funcion que borra espacios y devuelve a minusculas un texto"
    limpio = texto.strip()
    limpio2 = limpio.lower()
    return limpio2

# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 4: Validaciones ---")
print(f"Email válido: {validar_email('ana@correo.com')}")
print(f"Email inválido: {validar_email('ana.correo.com')}")
print(f"Teléfono válido: {validar_telefono('3101234567')}")
print(f"Teléfono inválido: {validar_telefono('310-123')}")
print(f"Texto limpio: '{limpiar_texto('  Python 3.14  ')}'")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 5: Usar __name__ == "__main__"
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Crea una función de prueba que solo se ejecute directamente

# TODO: Crea función pruebas_matematicas()
# - Imprime "=== Ejecutando pruebas ==="
# - Prueba suma: 5 + 3 = 8
# - Prueba resta: 10 - 4 = 6
# - Prueba multiplicación: 3 * 4 = 12
# - Imprime cada resultado
# - Imprime "=== Pruebas completadas ==="
def pruebas_matematicas():
    "Funcion de operaciones básicas, para ejecutar directamente del archivo"
    print("=== Ejecutando pruebas ===")
    print(f'suma (3+5): {3+5}')
    print(f'resta (10-4): {10-4} ')
    print(f'multiplicacion (3*4): {3*4}')
    print("=== Pruebas completadas ===")
# TODO: Crea bloque if __name__ == "__main__":
# - Dentro del bloque, llama a pruebas_matematicas()
# - Este código solo se ejecutará si corres este archivo directamente

if __name__ == "__main__":
    pruebas_matematicas()

# Nota: Si importas este archivo desde otro, pruebas_matematicas()
# NO se ejecutará automáticamente

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 6: Organizar código en "módulos" (en un solo archivo)
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Simula la organización de un proyecto en módulos

# TODO: Crea clase Producto (simula models/producto.py)
# - Constructor: __init__(self, id, nombre, precio)
# - Método to_dict(self): devuelve diccionario con id, nombre, precio
# - Método @classmethod from_dict(cls, data): crea Producto desde diccionario
class Producto():
    def __init__(self, id, nombre, precio):
        "Constructor"
        self.id = id
        self.nombre = nombre
        self.precio = precio
    
    def to_dic(self):
        "Método que devuelve un diccionario"
        return {'id': self.id,'nombre': self.nombre,'precio': self.precio}
    
    @classmethod
    def from_dicts(cls, data):
        "Método que crea un producto desde el diccionario"
        return cls(data['id'], data['nombre'], data['precio'])

# TODO: Crea clase Inventario (simula services/inventario.py)
# - Constructor: __init__(self, archivo="inventario.json")
#   * self.archivo = archivo
#   * self.productos = [] (comienza vacío)
# - Método agregar(self, producto): agrega Producto a la lista
# - Método listar(self): imprime todos los productos
#   * Formato: "ID [id] - [nombre]: $[precio]"
# - Método total(self): calcula y devuelve la suma de precios
class Inventario():
    def __init__(self, archivo='inventario.json'):
        self.archivo= archivo
        self.productos = []
    
    def agregar(self, producto):
        "Método que agrega un producto a la lista"
        nuevo = self.productos.append(producto)
        return nuevo
    
    def listar(self):
        "Método que muestra la Lista de todos los productos"
        if not self.productos:
            print("No hay producto disponibles")
            return
        for producto in self.productos:
            print(f'ID{producto.id} - {producto.nombre} - {producto.precio}')
    
    def total(self):
        "Método que muestra el total del precio de los productos"
        return sum(producto.precio for producto in self.productos)

# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 6: Organización Modular ---")
inventario = Inventario()

p1 = Producto(1, "Laptop", 1500000)
p2 = Producto(2, "Mouse", 35000)
p3 = Producto(3, "Teclado", 120000)

inventario.agregar(p1)
inventario.agregar(p2)
inventario.agregar(p3)

print("Productos en inventario:")
inventario.listar()
print(f"Valor total: ${inventario.total()}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 7: Gestor de Contactos Modular
# ═══════════════════════════════════════════════════════════════

# Instrucciones: Crea un sistema de contactos con estructura modular

# TODO: Crea clase Contacto (simula models/contacto.py)
# - Constructor: __init__(self, id, nombre, telefono, email)
# - Método to_dict(self): devuelve diccionario
# - Método @classmethod from_dict(cls, data): crea Contacto desde dict
# - Método __str__(self): devuelve representación legible
#   * Formato: "👤 [nombre] - Tel: [telefono] - Email: [email]"
class Contacto:
    def __init__(self, id, nombre, telefono, email):
        "Constructor de inicia los argumentos"
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def to_dict (self):
        "método que devuelve en diccionario los datos ingresados"
        return {'id':self.id, 'nombre': self.nombre, 'telefono': self.telefono, 'email': self.email}
    
    @classmethod
    def from_dict(cls, data):
        "Método que crea el contacto desde el diccionario"
        return cls(data['id'], data['nombre'], data['telefono'], data['email'])
    
    def __str__(self):
        "método str que devuelve el contenido del diccionario"
        return f'👤 {self.nombre} - Tel: {self.telefono} - Email {self.email}'

# TODO: Crea clase GestorContactos (simula services/gestor.py)
# - Constructor: __init__(self, archivo="contactos.json")
#   * self.archivo = archivo
#   * self.contactos = self.cargar()
class GestorContactos:
    def __init__(self, archivo = 'contactos.json'):
        self.archivo = archivo
        self.contactos = self.cargar()
# - Método cargar(self):
#   * Usa try/except con FileNotFoundError
#   * Lee JSON del archivo
#   * Convierte cada dict a Contacto usando from_dict
#   * Devuelve lista de contactos
#   * Si no existe archivo: devuelve []
    def cargar (self):
        "Método que carga el archivo .json"
        try:
            with open(self.archivo, 'r', encoding ='utf-8') as f:
                datos = json.load(f)
                return [Contacto.from_dict(c) for c in datos]
        except FileNotFoundError:
            return []
# - Método guardar(self):
#   * Convierte cada Contacto a dict usando to_dict
#   * Guarda en JSON con encoding="utf-8", indent=2, ensure_ascii=False

    def guardar(self):
        "Método que guarda el archivo .json"
        with open(self.archivo, 'w', encoding = 'utf-8') as f:
            datos = [c.to_dict() for c in self.contactos]
            json.dump(datos, f, indent= 2, ensure_ascii=False)
        
# - Método agregar(self, nombre, telefono, email):
#   * Calcula nuevo_id (max de ids existentes + 1, o 1 si está vacío)
#   * Crea nuevo Contacto
#   * Agrega a self.contactos
#   * Llama a self.guardar()
#   * Imprime "✅ Contacto [nombre] agregado"
    def agregar(self, nombre, telefono, email):
        "Método que agrega un contacto al diccionario"
        if self.contactos:
            nuevo_id = max (c.id for c in self.contactos) + 1
        else:
            nuevo_id = 1

        contacto = Contacto(nuevo_id, nombre, telefono, email)
        self.contactos.append(contacto)
        self.guardar()
        print(f'✅ Contacto {nombre} agregado')

# - Método listar(self):
#   * Si está vacío: imprime "📇 No hay contactos" y return
#   * Si no: imprime cada contacto usando su __str__
    def listar(self):
        if not self.contactos:
            print("📇 No hay contactos")
            return
        print(f'Contactos Disponibles: {len(self.contactos)}')
        for contacto in self.contactos:
            print(contacto)

# - Método buscar(self, nombre):
#   * Busca por nombre (case-insensitive)
#   * Devuelve el Contacto si lo encuentra
#   * Devuelve None si no
    def buscar (self, nombre):
        "Método que busca un contacto"
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
               return contacto
        return None
# Pruebas (NO MODIFICAR)
print("\n--- Ejercicio 7: Gestor de Contactos ---")
gestor = GestorContactos("contactos_ejercicio.json")

print("1. Agregando contactos:")
gestor.agregar("Laura Gómez", "3001112233", "laura@email.com")
gestor.agregar("Pedro Ruiz", "3104445566", "pedro@email.com")
gestor.agregar("Sofia Martín", "3207778899", "sofia@email.com")

print("\n2. Listando contactos:")
gestor.listar()

print("\n3. Buscando contacto:")
contacto = gestor.buscar("pedro ruiz")
if contacto:
    print(f"Encontrado: {contacto}")
else:
    print("No encontrado")

print("\n4. Verificando persistencia:")
gestor2 = GestorContactos("contactos_ejercicio.json")
print(f"Contactos cargados: {len(gestor2.contactos)}")

print("\n=== FIN DE LOS EJERCICIOS ===")

# -----------------------------------------------
# 🏆 CRITERIOS DE ÉXITO
# -----------------------------------------------
# Para considerar estos ejercicios completados:
# 1. Importas y usas módulos de la biblioteca estándar
# 2. Creas funciones de validación reutilizables
# 3. Trabajas con fechas usando datetime
# 4. Entiendes __name__ == "__main__"
# 5. Organizas código en clases separadas (Modelo/Servicio)
# 6. Tu GestorContactos maneja persistencia correctamente
#
# Ejecuta: python exercises_06.py

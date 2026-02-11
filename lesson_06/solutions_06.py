"""
SOLUCIONES - LECCIÓN 6: MÓDULOS Y ORGANIZACIÓN DE CÓDIGO
========================================================

Estas son las soluciones completas de los ejercicios.
Compara tu código con estas soluciones para aprender.
"""

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 1: Usar módulos de la biblioteca estándar
# ═══════════════════════════════════════════════════════════════

import math
import random
from datetime import datetime

def calcular_raiz_cuadrada(numero):
    """Calcula la raíz cuadrada usando math.sqrt"""
    return math.sqrt(numero)

def obtener_fecha_actual():
    """Devuelve la fecha actual en formato DD/MM/YYYY"""
    ahora = datetime.now()
    return ahora.strftime("%d/%m/%Y")

def numero_aleatorio(min, max):
    """Genera un número aleatorio entre min y max (inclusive)"""
    return random.randint(min, max)

# Pruebas
print("--- Ejercicio 1: Biblioteca Estándar ---")
print(f"Raíz cuadrada de 144: {calcular_raiz_cuadrada(144)}")
print(f"Fecha actual: {obtener_fecha_actual()}")
print(f"Número aleatorio: {numero_aleatorio(1, 100)}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 2: Importaciones específicas
# ═══════════════════════════════════════════════════════════════

from math import pi, ceil

def calcular_area_circulo(radio):
    """Calcula el área de un círculo y redondea hacia arriba"""
    area = pi * radio ** 2
    return ceil(area)

# Pruebas
print("\n--- Ejercicio 2: Importaciones Específicas ---")
print(f"Área de círculo con radio 3: {calcular_area_circulo(3)}")
print(f"Área de círculo con radio 7: {calcular_area_circulo(7)}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 3: Trabajar con fechas
# ═══════════════════════════════════════════════════════════════

from datetime import datetime, timedelta

def dias_hasta_fecha(dia, mes, año):
    """Calcula cuántos días faltan hasta una fecha específica"""
    fecha_objetivo = datetime(año, mes, dia)
    fecha_actual = datetime.now()
    diferencia = fecha_objetivo - fecha_actual
    return diferencia.days

def agregar_dias(fecha_str, dias):
    """Suma días a una fecha en formato DD/MM/YYYY"""
    # Convertir string a datetime
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    # Agregar días
    nueva_fecha = fecha + timedelta(days=dias)
    # Convertir de vuelta a string
    return nueva_fecha.strftime("%d/%m/%Y")

# Pruebas
print("\n--- Ejercicio 3: Fechas ---")
print(f"Días hasta 01/01/2027: {dias_hasta_fecha(1, 1, 2027)}")
print(f"15 días después de 01/02/2026: {agregar_dias('01/02/2026', 15)}")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 4: Crear módulo de utilidades (simulado)
# ═══════════════════════════════════════════════════════════════

def validar_email(email):
    """Valida que un email tenga formato correcto"""
    # Verificar que contenga @ y .
    if "@" not in email or "." not in email:
        return False
    
    # Verificar que @ esté antes que el último .
    posicion_arroba = email.index("@")
    posicion_punto = email.rindex(".")  # último punto
    
    return posicion_arroba < posicion_punto

def validar_telefono(telefono):
    """Valida que un teléfono tenga 10 dígitos"""
    # Verificar longitud y que solo sean dígitos
    return len(telefono) == 10 and telefono.isdigit()

def limpiar_texto(texto):
    """Limpia un texto eliminando espacios y convirtiendo a minúsculas"""
    return texto.strip().lower()

# Pruebas
print("\n--- Ejercicio 4: Validaciones ---")
print(f"Email válido: {validar_email('ana@correo.com')}")
print(f"Email inválido: {validar_email('ana.correo.com')}")
print(f"Teléfono válido: {validar_telefono('3101234567')}")
print(f"Teléfono inválido: {validar_telefono('310-123')}")
print(f"Texto limpio: '{limpiar_texto('  Python 3.14  ')}'")

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 5: Usar __name__ == "__main__"
# ═══════════════════════════════════════════════════════════════

def pruebas_matematicas():
    """Ejecuta pruebas básicas de operaciones matemáticas"""
    print("\n=== Ejecutando pruebas ===")
    
    # Prueba suma
    resultado_suma = 5 + 3
    print(f"Suma: 5 + 3 = {resultado_suma}")
    
    # Prueba resta
    resultado_resta = 10 - 4
    print(f"Resta: 10 - 4 = {resultado_resta}")
    
    # Prueba multiplicación
    resultado_mult = 3 * 4
    print(f"Multiplicación: 3 * 4 = {resultado_mult}")
    
    print("=== Pruebas completadas ===")

# Este código solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    pruebas_matematicas()

# ═══════════════════════════════════════════════════════════════
# EJERCICIO 6: Organizar código en "módulos" (en un solo archivo)
# ═══════════════════════════════════════════════════════════════

class Producto:
    """Representa un producto del inventario (simula models/producto.py)"""
    
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
    
    def to_dict(self):
        """Convierte el producto a diccionario"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un Producto desde un diccionario"""
        return cls(data["id"], data["nombre"], data["precio"])

class Inventario:
    """Gestiona productos (simula services/inventario.py)"""
    
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = []
    
    def agregar(self, producto):
        """Agrega un producto al inventario"""
        self.productos.append(producto)
    
    def listar(self):
        """Lista todos los productos"""
        for producto in self.productos:
            print(f"ID {producto.id} - {producto.nombre}: ${producto.precio}")
    
    def total(self):
        """Calcula el valor total del inventario"""
        return sum(p.precio for p in self.productos)

# Pruebas
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

import json

class Contacto:
    """Representa un contacto (simula models/contacto.py)"""
    
    def __init__(self, id, nombre, telefono, email):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def to_dict(self):
        """Convierte el contacto a diccionario"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un Contacto desde un diccionario"""
        return cls(data["id"], data["nombre"], data["telefono"], data["email"])
    
    def __str__(self):
        """Representación legible del contacto"""
        return f"👤 {self.nombre} - Tel: {self.telefono} - Email: {self.email}"

class GestorContactos:
    """Gestiona contactos con persistencia en JSON (simula services/gestor.py)"""
    
    def __init__(self, archivo="contactos.json"):
        self.archivo = archivo
        self.contactos = self.cargar()
    
    def cargar(self):
        """Carga contactos desde el archivo JSON"""
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                # Convertir cada diccionario a objeto Contacto
                return [Contacto.from_dict(c) for c in datos]
        except FileNotFoundError:
            return []
    
    def guardar(self):
        """Guarda contactos en el archivo JSON"""
        with open(self.archivo, "w", encoding="utf-8") as f:
            # Convertir cada Contacto a diccionario
            datos = [c.to_dict() for c in self.contactos]
            json.dump(datos, f, indent=2, ensure_ascii=False)
    
    def agregar(self, nombre, telefono, email):
        """Agrega un nuevo contacto"""
        # Calcular nuevo ID
        if self.contactos:
            nuevo_id = max(c.id for c in self.contactos) + 1
        else:
            nuevo_id = 1
        
        # Crear y agregar contacto
        contacto = Contacto(nuevo_id, nombre, telefono, email)
        self.contactos.append(contacto)
        self.guardar()
        print(f"✅ Contacto {nombre} agregado")
    
    def listar(self):
        """Lista todos los contactos"""
        if not self.contactos:
            print("📇 No hay contactos")
            return
        
        for contacto in self.contactos:
            print(contacto)
    
    def buscar(self, nombre):
        """Busca un contacto por nombre (case-insensitive)"""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None

# Pruebas
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

print("\n=== FIN DE LAS SOLUCIONES ===")

# -----------------------------------------------
# 📝 NOTAS IMPORTANTES
# -----------------------------------------------
"""
1. IMPORTACIONES:
   - Importa solo lo que necesitas (from math import pi)
   - Usa alias para nombres largos (import datetime as dt)
   - Agrupa imports: estándar → terceros → propios

2. MÓDULOS PROPIOS:
   - Un archivo .py = un módulo
   - Mantén responsabilidades claras
   - Usa __name__ == "__main__" para código de prueba

3. ORGANIZACIÓN:
   - Separa modelos de lógica de negocio
   - models/ para clases de datos
   - services/ para lógica y operaciones
   - utils/ para funciones auxiliares

4. BUENAS PRÁCTICAS:
   - Nombres descriptivos para módulos (snake_case)
   - Docstrings en funciones y clases
   - Cada módulo debe tener un propósito claro
   - Evita imports circulares

5. ESTRUCTURA RECOMENDADA:
   proyecto/
   ├── main.py              # Punto de entrada
   ├── config.py            # Configuración
   ├── models/              # Modelos de datos
   │   ├── __init__.py
   │   └── entidad.py
   ├── services/            # Lógica de negocio
   │   ├── __init__.py
   │   └── gestor.py
   └── utils/               # Utilidades
       ├── __init__.py
       └── validaciones.py
"""

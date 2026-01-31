# 🎯 SOLUCIONES LECCIÓN 4 - Conceptos Avanzados de POO
# ==========================================
# Soluciones de referencia para exercises_04.py

print("=== INICIANDO SOLUCIONES LECCIÓN 4 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Factory Methods con @classmethod
# -----------------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @classmethod
    def desde_año_nacimiento(cls, nombre, año_nacimiento):
        """Factory method que crea una Persona calculando edad desde año nacimiento"""
        edad = 2026 - año_nacimiento
        return cls(nombre, edad)
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"


# Pruebas
print("--- Ejercicio 1: Factory Methods ---")
p1 = Persona("Ana", 25)
p2 = Persona.desde_año_nacimiento("Carlos", 1995)
print(p1)
print(p2)
print()

# -----------------------------------------------
# EJERCICIO 2: @staticmethod para Validaciones
# -----------------------------------------------
class Validador:
    @staticmethod
    def es_email_valido(email):
        """Verifica si un email contiene @ y ."""
        return "@" in email and "." in email
    
    @staticmethod
    def es_password_seguro(password):
        """Verifica si el password tiene al menos 8 caracteres"""
        return len(password) >= 8


# Pruebas
print("--- Ejercicio 2: Métodos Estáticos ---")
print(f"'ana@gmail.com' es válido? {Validador.es_email_valido('ana@gmail.com')}")
print(f"'anagmail' es válido? {Validador.es_email_valido('anagmail')}")
print(f"'password123' es seguro? {Validador.es_password_seguro('password123')}")
print(f"'pass' es seguro? {Validador.es_password_seguro('pass')}")
print()

# -----------------------------------------------
# EJERCICIO 3: Métodos Mágicos - Comparación
# -----------------------------------------------
class Estudiante:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
    
    def __str__(self):
        return f"{self.nombre}: {self.promedio}"
    
    def __eq__(self, otro):
        """Compara si dos estudiantes tienen el mismo promedio"""
        return self.promedio == otro.promedio
    
    def __lt__(self, otro):
        """Compara si este estudiante tiene menor promedio"""
        return self.promedio < otro.promedio
    
    def __gt__(self, otro):
        """Compara si este estudiante tiene mayor promedio"""
        return self.promedio > otro.promedio


# Pruebas
print("--- Ejercicio 3: Comparaciones ---")
e1 = Estudiante("Ana", 85)
e2 = Estudiante("Carlos", 90)
e3 = Estudiante("María", 85)
print(f"{e1} == {e3}: {e1 == e3}")
print(f"{e1} < {e2}: {e1 < e2}")
print(f"{e2} > {e1}: {e2 > e1}")
print()

# -----------------------------------------------
# EJERCICIO 4: __len__ y __str__ - Lista Personalizada
# -----------------------------------------------
class ListaTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar(self, tarea):
        """Agrega una tarea a la lista"""
        self.tareas.append(tarea)
    
    def __len__(self):
        """Permite usar len() con esta clase"""
        return len(self.tareas)
    
    def __str__(self):
        """Representación legible de la lista"""
        if len(self.tareas) == 0:
            return "Lista vacía"
        else:
            return f"Lista con {len(self.tareas)} tarea(s)"


# Pruebas
print("--- Ejercicio 4: __len__ y __str__ ---")
lista = ListaTareas()
print(f"Tareas: {len(lista)}")
print(lista)
lista.agregar("Estudiar Python")
lista.agregar("Hacer ejercicios")
print(f"Tareas: {len(lista)}")
print(lista)
print()

# -----------------------------------------------
# EJERCICIO 5: __add__ - Sumar Objetos
# -----------------------------------------------
class Carrito:
    def __init__(self):
        self.total = 0
    
    def agregar_producto(self, precio):
        """Agrega un producto al carrito"""
        self.total += precio
    
    def __add__(self, otro):
        """Permite sumar dos carritos usando +"""
        return self.total + otro.total
    
    def __str__(self):
        return f"Carrito: ${self.total}"


# Pruebas
print("--- Ejercicio 5: Sumar Carritos ---")
carrito1 = Carrito()
carrito1.agregar_producto(100)
carrito1.agregar_producto(50)

carrito2 = Carrito()
carrito2.agregar_producto(200)

print(carrito1)
print(carrito2)
print(f"Suma de carritos: ${carrito1 + carrito2}")
print()

# -----------------------------------------------
# EJERCICIO 6: @property - Validación
# -----------------------------------------------
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio  # Atributo privado
    
    @property
    def precio(self):
        """Getter: permite leer el precio"""
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        """Setter: valida antes de asignar"""
        if nuevo_precio < 0:
            raise ValueError("Precio no puede ser negativo")
        self._precio = nuevo_precio


# Pruebas
print("--- Ejercicio 6: Propiedades con Validación ---")
prod = Producto("Laptop", 1000)
print(f"Precio inicial: ${prod.precio}")
prod.precio = 1200
print(f"Nuevo precio: ${prod.precio}")
try:
    prod.precio = -100
except ValueError as e:
    print(f"Error: {e}")
print()

# -----------------------------------------------
# EJERCICIO 7: DESAFÍO - Clase Completa con Todo
# -----------------------------------------------
class Empleado:
    # Variable de clase
    total_empleados = 0
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario
        Empleado.total_empleados += 1
    
    @classmethod
    def crear_junior(cls, nombre):
        """Factory method: crea empleado junior con salario fijo"""
        return cls(nombre, 30000)
    
    @staticmethod
    def calcular_impuesto(salario):
        """Calcula impuesto según tramo de salario"""
        if salario < 50000:
            return salario * 0.10
        else:
            return salario * 0.20
    
    @property
    def salario(self):
        """Getter del salario"""
        return self._salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        """Setter del salario con validación"""
        if nuevo_salario <= 0:
            raise ValueError("Salario debe ser mayor a 0")
        self._salario = nuevo_salario
    
    @property
    def salario_neto(self):
        """Calcula salario después de impuestos"""
        impuesto = Empleado.calcular_impuesto(self._salario)
        return self._salario - impuesto
    
    def __str__(self):
        return f"{self.nombre} - Salario: ${self._salario}"
    
    def __eq__(self, otro):
        """Compara empleados por salario"""
        return self._salario == otro._salario
    
    def __lt__(self, otro):
        """Compara si este empleado gana menos"""
        return self._salario < otro._salario
    
    @classmethod
    def mostrar_total(cls):
        """Muestra el total de empleados creados"""
        print(f"Total de empleados: {cls.total_empleados}")


# Pruebas
print("--- Ejercicio 7: Clase Completa ---")
emp1 = Empleado("Ana", 60000)
emp2 = Empleado.crear_junior("Carlos")

print(emp1)
print(emp2)

print(f"Salario neto de Ana: ${emp1.salario_neto}")
print(f"Salario neto de Carlos: ${emp2.salario_neto}")

print(f"emp1 == emp2: {emp1 == emp2}")
print(f"emp2 < emp1: {emp2 < emp1}")

Empleado.mostrar_total()

print("\n=== FIN DE LAS SOLUCIONES ===")

# -----------------------------------------------
# 💡 EXPLICACIONES CLAVE
# -----------------------------------------------
"""
1. @classmethod:
   - Recibe 'cls' como primer parámetro
   - Puede crear instancias de la clase (factory methods)
   - Útil para constructores alternativos

2. @staticmethod:
   - No recibe ni 'self' ni 'cls'
   - Funciones de utilidad que pertenecen a la clase
   - No acceden a atributos de instancia ni de clase

3. Métodos Mágicos:
   - __str__: representación legible para humanos
   - __eq__: define comportamiento de ==
   - __lt__: define comportamiento de <
   - __add__: define comportamiento de +
   - __len__: permite usar len()

4. @property:
   - Getter: @property
   - Setter: @nombre.setter
   - Permite validación al asignar valores
   - Convierte métodos en atributos

5. Atributos Privados:
   - Convención: usar _ antes del nombre (ej: self._precio)
   - No son verdaderamente privados, pero indican "interno"
"""

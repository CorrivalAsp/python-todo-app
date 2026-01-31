# 🎯 EJERCICIOS LECCIÓN 4 - Conceptos Avanzados de POO
# ==========================================
# Completa cada ejercicio usando @classmethod, @staticmethod, métodos mágicos y @property

print("=== INICIANDO EJERCICIOS LECCIÓN 4 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Factory Methods con @classmethod
# -----------------------------------------------
# Instrucciones: Crea una clase Persona con múltiples constructores

# TODO: Define la clase Persona
# - Constructor normal __init__(nombre, edad)
# - Atributos: self.nombre, self.edad
# - @classmethod desde_año_nacimiento(cls, nombre, año_nacimiento):
#   * Calcula edad = 2026 - año_nacimiento
#   * Devuelve cls(nombre, edad)
# - Método __str__() que devuelva: "[nombre], [edad] años"

class Persona:
    def __init__(self, nombre, edad):
        "Constructor Normal de atributos"
        self.nombre = nombre
        self.edad = edad
    @classmethod
    def desde_año_nacimiento(cls, nombre, año_nacimiento):
        "Método donde se calcula la edad"
        edad = 2026 - año_nacimiento
        return cls(nombre, edad)
    
    def __str__(self):
        "imprime el resultado de ambos parametros"
        return f'{self.nombre}, tiene {self.edad} años '

    
# Prueba tu clase (NO MODIFICAR)
print("--- Ejercicio 1: Factory Methods ---")
p1 = Persona("Ana", 25)
p2 = Persona.desde_año_nacimiento("Carlos", 1995)
print(p1)
print(p2)
print()

# -----------------------------------------------
# EJERCICIO 2: @staticmethod para Validaciones
# -----------------------------------------------
# Instrucciones: Crea una clase Validador con métodos estáticos

# TODO: Define la clase Validador
# - @staticmethod es_email_valido(email):
#   * Verifica que contenga "@" y "."
#   * Devuelve True si es válido, False si no
# - @staticmethod es_password_seguro(password):
#   * Verifica que tenga al menos 8 caracteres
#   * Devuelve True si es seguro, False si no

class Validador:
    @staticmethod
    def es_email_valido(email):
        "Verifica si el email es válido"
        return "@" in email and "." in email
    def es_password_seguro(password):
        "Verifica si la contraseña tiene minimo 8 caracteres"
        if len(password) >= 8:
            return True
        else:
            return False
        
# Prueba tu clase (NO MODIFICAR)
print("--- Ejercicio 2: Métodos Estáticos ---")
print(f"'ana@gmail.com' es válido? {Validador.es_email_valido('ana@gmail.com')}")
print(f"'anagmail' es válido? {Validador.es_email_valido('anagmail')}")
print(f"'password123' es seguro? {Validador.es_password_seguro('password123')}")
print(f"'pass' es seguro? {Validador.es_password_seguro('pass')}")
print()

# -----------------------------------------------
# EJERCICIO 3: Métodos Mágicos - Comparación
# -----------------------------------------------
# Instrucciones: Crea una clase Estudiante con comparaciones

# TODO: Define la clase Estudiante
# - Constructor: __init__(nombre, promedio)
# - Atributos: self.nombre, self.promedio
# - __str__(): devuelve "[nombre]: [promedio]"
# - __eq__(otro): compara promedios (True si son iguales)
# - __lt__(otro): compara promedios (True si self < otro)
# - __gt__(otro): compara promedios (True si self > otro)

class Estudiante:
    def __init__(self, nombre, promedio):
        "Constructor inicial de atributos"
        self.nombre = nombre
        self.promedio = promedio
    
    def __str__(self):
        "Muestra nombre y promedio"
        return f'{self.nombre}: {self.promedio}'
    def __eq__(self, otro):
        "Método que compara si los promedios son iguales"
        if self.promedio == otro.promedio:
            return True
    def __lt__(self, otro):
        "Método que compara si un promedio es menor que otro"
        if self.promedio < otro.promedio:
            return True
    def __gt__(self, otro):
        "Método que compara si promedio es mayor que otro"
        if self.promedio > otro.promedio:
            return True
        


# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase ListaTareas que soporte len()

# TODO: Define la clase ListaTareas
# - Constructor: inicializa self.tareas = []
# - Método agregar(tarea): agrega tarea a la lista
# - __len__(): devuelve len(self.tareas)
# - __str__(): 
#   * Si está vacía: "Lista vacía"
#   * Si no: "Lista con [N] tarea(s)"
class ListaTareas:
    def __init__(self):
        "Constructor inicializa el argumento tareas como lista vacía"
        self.tareas = []
    def agregar(self,tarea):
        "Método para agregar tarea a la lista"
        self.tareas.append(tarea)
    def __len__(self):
        "Devuelve la cantidad de espacios que utiliza la lista"
        return len(self.tareas)
    def __str__(self):
        "Método que devuelve el estado de las listas"
        if len(self.tareas) == 0:
            return f'Lista Vacía'
        else:
            return f'Lista con {len(self.tareas)} tareas.'
            
# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase Carrito que se pueda sumar

# TODO: Define la clase Carrito
# - Constructor: inicializa self.total = 0
# - Método agregar_producto(precio): suma al total
# - __add__(otro): devuelve self.total + otro.total
# - __str__(): devuelve "Carrito: $[total]"

class Carrito:
    def __init__(self):
        "Constructor inicializa el total en 0"
        self.total = 0
    def agregar_producto(self, precio):
        "Método donde se agrega un producto con su precio"
        self.total += precio
    def __add__(self, otro):
        "Devuelve la suma de dos productos"
        return self.total + otro.total
    def __str__(self):
        "Muestra el total del carrito"
        return f'Carrito: ${self.total}'

# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase Producto con precio validado

# TODO: Define la clase Producto
# - Constructor: __init__(nombre, precio)
# - Atributos: self.nombre, self._precio (con _)
# - @property precio: getter que devuelve self._precio
# - @precio.setter: 
#   * Valida que precio >= 0
#   * Si es negativo, lanza ValueError("Precio no puede ser negativo")
#   * Si es válido, asigna a self._precio

class Producto:
    def __init__(self, nombre, precio):
        "Constructor que inicia los atributo"
        self.nombre = nombre
        self._precio = precio
    @property
    def precio(self):
        "Devuelve el valor del precio"
        return self._precio
    @precio.setter
    def precio (self, nuevo_precio):
        "Agrega el nuevo precio al atributo si este es mayor que 0"
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else: 
            raise ValueError ("El precio no debe ser negativo")
            
    
    
# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase Empleado que use todos los conceptos

# TODO: Define la clase Empleado
# - Variable de clase: total_empleados = 0
# - Constructor: __init__(nombre, salario)
# - Atributos: self.nombre, self._salario
# - En __init__: incrementa Empleado.total_empleados
#
# - @classmethod crear_junior(cls, nombre):
#   * Crea empleado con salario = 30000
#   * Devuelve cls(nombre, 30000)
#
# - @staticmethod calcular_impuesto(salario):
#   * Si salario < 50000: impuesto = salario * 0.10
#   * Si no: impuesto = salario * 0.20
#   * Devuelve el impuesto
#
# - @property salario: getter
# - @salario.setter: valida que salario > 0
#
# - @property salario_neto:
#   * Calcula: salario - impuesto
#   * Usa Empleado.calcular_impuesto(self._salario)
#
# - __str__(): "[nombre] - Salario: $[salario]"
# - __eq__(otro): compara salarios
# - __lt__(otro): compara salarios
#
# - @classmethod mostrar_total(cls):
#   * Imprime: "Total de empleados: [total_empleados]"

class Empleado:
    total_empleados = 0
    def __init__(self, nombre, salario):
        "Constructor donde se inician los atributos nombre y salario como atributo privado y se incrementa el total de empleados"
        self.nombre = nombre
        self._salario = salario
        Empleado.total_empleados += 1

    @classmethod
    def crear_junior(cls, nombre):
        "Crea el empleado junior con un salario fijo"
        return cls(nombre, 30000)
    
    @staticmethod
    def calcular_impuesto(salario):
        "Calcula un impuesto dependiendo del salario"
        if salario < 50000:
            impuesto = salario *0.10
            return impuesto
        else:
            impuesto = salario *0.20
            return impuesto
    @property
    def salario(self):
        "Método getter para obtener el salario"
        return self._salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        "Método que devuelve el salario si este es mayor a 0"
        if nuevo_salario > 0:
            self._salario = nuevo_salario
        else:
            raise ValueError("El salario debe ser mayor a 0") 
    
    @property
    def salario_neto(self):
        "Método que calcula el salario neto del empleado"
        impuesto = Empleado.calcular_impuesto(self._salario)
        return self._salario - impuesto

    def __str__(self):
        "Método que muestra tanto el nombre del empleado como su salario"
        return f'{self.nombre} - Salario: $ {self._salario}'
    
    def __eq__(self, otro):
        "Método que compara si dos salarios son iguales"
        if self.salario == otro.salario:
            return True
        else:
            return False
    def __lt__ (self, otro):
        "Método que compara si un salario es menor que otro"
        if self._salario < otro.salario:
            return True
        else:
            return False
    @classmethod
    def mostrar_total(cls):
        "Muestra la variable de toda la clase"
        print(f'Total Empleado {Empleado.total_empleados}')

# Prueba tu clase (NO MODIFICAR)
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

print("\n=== FIN DE LOS EJERCICIOS ===")

# -----------------------------------------------
# 🏆 CRITERIOS DE ÉXITO
# -----------------------------------------------
# Para considerar estos ejercicios completados:
# 1. Usas @classmethod correctamente
# 2. Usas @staticmethod para utilidades
# 3. Implementas métodos mágicos correctamente
# 4. Usas @property con validación
# 5. El programa se ejecuta sin errores
#
# Ejecuta: python exercises_04.py

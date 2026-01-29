# ✅ SOLUCIONES LECCIÓN 3 - Clases y Objetos
# ==========================================
# ⚠️ IMPORTANTE: Intenta resolver exercises_03.py ANTES de ver estas soluciones

print("=== SOLUCIONES EJERCICIOS LECCIÓN 3 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Tu primera clase
# -----------------------------------------------

class Libro:
    """Representa un libro con título y autor."""
    
    def __init__(self, titulo, autor):
        """Inicializa un libro."""
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_info(self):
        """Muestra información del libro."""
        print(f"📚 {self.titulo} por {self.autor}")

print("--- Ejercicio 1: Clase Libro ---")
libro1 = Libro("Python Crash Course", "Eric Matthes")
libro2 = Libro("Automate the Boring Stuff", "Al Sweigart")
libro1.mostrar_info()
libro2.mostrar_info()
print()

# -----------------------------------------------
# EJERCICIO 2: Clase con método que modifica atributos
# -----------------------------------------------

class CuentaBancaria:
    """Representa una cuenta bancaria simple."""
    
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa una cuenta bancaria."""
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        """Deposita dinero en la cuenta."""
        self.saldo += cantidad
        print(f"💰 Depósito de ${cantidad}. Nuevo saldo: ${self.saldo}")
    
    def retirar(self, cantidad):
        """Retira dinero de la cuenta."""
        self.saldo -= cantidad
        print(f"💸 Retiro de ${cantidad}. Nuevo saldo: ${self.saldo}")
    
    def mostrar_saldo(self):
        """Muestra el saldo actual."""
        print(f"Saldo de {self.titular}: ${self.saldo}")

print("--- Ejercicio 2: Cuenta Bancaria ---")
cuenta = CuentaBancaria("Jhon", 1000)
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.mostrar_saldo()
print()

# -----------------------------------------------
# EJERCICIO 3: Clase Estudiante con múltiples métodos
# -----------------------------------------------

class Estudiante:
    """Representa un estudiante con sus calificaciones."""
    
    def __init__(self, nombre):
        """Inicializa un estudiante."""
        self.nombre = nombre
        self.calificaciones = []
    
    def agregar_calificacion(self, nota):
        """Agrega una calificación."""
        self.calificaciones.append(nota)
    
    def promedio(self):
        """Calcula y devuelve el promedio de calificaciones."""
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def __str__(self):
        """Representación en string del estudiante."""
        return f"{self.nombre} - Promedio: {self.promedio():.2f}"

print("--- Ejercicio 3: Estudiante ---")
estudiante = Estudiante("Ana")
estudiante.agregar_calificacion(85)
estudiante.agregar_calificacion(92)
estudiante.agregar_calificacion(78)
print(f"Promedio de {estudiante.nombre}: {estudiante.promedio()}")
print(estudiante)
print()

# -----------------------------------------------
# EJERCICIO 4: Clase Tarea para To-Do App
# -----------------------------------------------

class Tarea:
    """Representa una tarea con descripción, estado y prioridad."""
    
    def __init__(self, descripcion):
        """Inicializa una tarea."""
        self.descripcion = descripcion
        self.completada = False
        self.prioridad = "media"
    
    def completar(self):
        """Marca la tarea como completada."""
        self.completada = True
    
    def cambiar_prioridad(self, nueva_prioridad):
        """Cambia la prioridad de la tarea."""
        self.prioridad = nueva_prioridad
    
    def __str__(self):
        """Representación en string de la tarea."""
        estado = "✅" if self.completada else "⏳"
        return f"{estado} {self.descripcion} (Prioridad: {self.prioridad})"

print("--- Ejercicio 4: Clase Tarea ---")
tarea1 = Tarea("Estudiar Python")
tarea2 = Tarea("Hacer ejercicios")
print(tarea1)
tarea1.completar()
tarea1.cambiar_prioridad("alta")
print(tarea1)
print(tarea2)
print()

# -----------------------------------------------
# EJERCICIO 5: DESAFÍO - Clase Producto con stock
# -----------------------------------------------

class Producto:
    """Representa un producto con nombre, precio y stock."""
    
    def __init__(self, nombre, precio, stock):
        """Inicializa un producto."""
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def vender(self, cantidad):
        """
        Intenta vender una cantidad del producto.
        
        Returns:
            True si la venta fue exitosa, False si no hay suficiente stock.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"✅ Vendidas {cantidad} unidades de {self.nombre}")
            return True
        else:
            print(f"❌ Stock insuficiente de {self.nombre}")
            return False
    
    def reabastecer(self, cantidad):
        """Agrega stock al producto."""
        self.stock += cantidad
        print(f"📦 Reabastecidas {cantidad} unidades de {self.nombre}")
    
    def info(self):
        """Devuelve información del producto."""
        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"

print("--- Ejercicio 5: Clase Producto ---")
producto = Producto("Laptop", 1200, 5)
print(producto.info())
exitoso = producto.vender(2)
print(f"Venta exitosa: {exitoso}")
print(producto.info())
exitoso = producto.vender(10)
print(f"Venta exitosa: {exitoso}")
producto.reabastecer(15)
print(producto.info())
print()

# -----------------------------------------------
# EJERCICIO 6: SUPER DESAFÍO - Gestor de Tareas
# -----------------------------------------------

class TodoList:
    """Gestiona una lista de tareas."""
    
    def __init__(self):
        """Inicializa la lista de tareas."""
        self.tareas = []
    
    def agregar(self, descripcion):
        """Agrega una nueva tarea."""
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f"➕ Tarea agregada: {descripcion}")
    
    def listar(self):
        """Lista todas las tareas."""
        if len(self.tareas) == 0:
            print("No hay tareas")
        else:
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")
    
    def completar_tarea(self, numero):
        """Marca una tarea como completada."""
        if 1 <= numero <= len(self.tareas):
            self.tareas[numero - 1].completar()
            print(f"✅ Tarea {numero} completada")
        else:
            print("❌ Número de tarea inválido")
    
    def total(self):
        """Devuelve el total de tareas."""
        return len(self.tareas)

print("--- Ejercicio 6: TodoList ---")
mi_lista = TodoList()
mi_lista.agregar("Aprender POO")
mi_lista.agregar("Practicar clases")
mi_lista.agregar("Crear proyecto")
print()
mi_lista.listar()
print()
mi_lista.completar_tarea(1)
print()
mi_lista.listar()
print(f"\nTotal de tareas: {mi_lista.total()}")
print()

# -----------------------------------------------
# EJERCICIO 7: BONUS - Clase Contador
# -----------------------------------------------

class Contador:
    """Cuenta cuántas instancias se han creado."""
    
    total_instancias = 0  # Variable de clase
    
    def __init__(self):
        """Incrementa el contador al crear una instancia."""
        Contador.total_instancias += 1
    
    @classmethod
    def mostrar_total(cls):
        """Muestra el total de instancias creadas."""
        print(f"Total de contadores creados: {cls.total_instancias}")

print("--- Ejercicio 7: Contador de instancias ---")
c1 = Contador()
c2 = Contador()
c3 = Contador()
Contador.mostrar_total()

print("\n=== FIN DE LAS SOLUCIONES ===")

# -----------------------------------------------
# 💡 NOTAS IMPORTANTES SOBRE LAS SOLUCIONES
# -----------------------------------------------
#
# 1. __init__ (Constructor):
#    - Siempre tiene self como primer parámetro
#    - Se usa para inicializar atributos
#    - Se ejecuta automáticamente al crear el objeto
#
# 2. self:
#    - Referencia al objeto actual
#    - Obligatorio en todos los métodos de instancia
#    - Se usa para acceder a atributos: self.nombre
#
# 3. __str__:
#    - Método especial para representación en string
#    - Se llama automáticamente con print()
#    - Debe devolver un string (no imprimir)
#
# 4. Validaciones:
#    - Siempre valida antes de modificar datos
#    - Ejemplo: verificar stock antes de vender
#    - Ejemplo: verificar número válido antes de acceder a lista
#
# 5. Variables de clase vs instancia:
#    - Clase: Contador.total_instancias (compartida)
#    - Instancia: self.nombre (única por objeto)
#
# 6. @classmethod:
#    - Decorador para métodos de clase
#    - Usa 'cls' en vez de 'self'
#    - Accede a variables de clase, no de instancia

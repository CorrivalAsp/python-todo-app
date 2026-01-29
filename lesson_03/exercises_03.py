# 🎯 EJERCICIOS LECCIÓN 3 - Clases y Objetos
# ==========================================
# Completa cada ejercicio creando las clases solicitadas.

print("=== INICIANDO EJERCICIOS LECCIÓN 3 ===\n")

# -----------------------------------------------
# EJERCICIO 1: Tu primera clase
# -----------------------------------------------
# Instrucciones: Crea una clase Libro que tenga título y autor

# TODO: Define la clase Libro
# - Constructor __init__ que reciba: titulo, autor
# - Atributos: self.titulo, self.autor
# - Método mostrar_info() que imprima: "📚 [titulo] por [autor]"

class Libro:
    def __init__(self, titulo, autor):
        "inicializa los atributos"
        self.titulo = titulo #Titulo del libro
        self.autor = autor #Nombre del autor
    def mostrar_info(self):
        "Muestra la información guardada en los atributos"
        print(f'El libro {self.titulo} escrito por el autor {self.autor}.')
       


# Prueba tu clase (NO MODIFICAR)
print("--- Ejercicio 1: Clase Libro ---")
libro1 = Libro("Python Crash Course", "Eric Matthes")
libro2 = Libro("Automate the Boring Stuff", "Al Sweigart")
libro1.mostrar_info()
libro2.mostrar_info()
print()

# -----------------------------------------------
# EJERCICIO 2: Clase con método que modifica atributos
# -----------------------------------------------
# Instrucciones: Crea una clase CuentaBancaria

# TODO: Define la clase CuentaBancaria
# - Constructor que reciba: titular, saldo_inicial (por defecto 0)
# - Atributos: self.titular, self.saldo
# - Método depositar(cantidad) que sume al saldo e imprima el nuevo saldo
# - Método retirar(cantidad) que reste del saldo e imprima el nuevo saldo
# - Método mostrar_saldo() que imprima: "Saldo de [titular]: $[saldo]"
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial =0):
        "inicializa los atributos de cuenta bancaria "
        self.titular = titular
        self.saldo_inicial = saldo_inicial
    
    def depositar(self, cantidad):

        "Aumenta el valor teniendo presente la cantidad depositada"
        nuevo_saldo= self.saldo_inicial + cantidad
        print(f' Su nuevo saldo es de ${nuevo_saldo}')
        self.saldo_inicial = nuevo_saldo
        return self.saldo_inicial
    
    def retirar(self, cantidad):
        "Substrae de la cuenta el valor de cantidad"
        nuevo_saldo = self.saldo_inicial - cantidad
        print(f' Su nuevo saldo es de ${nuevo_saldo}')
        self.saldo_inicial = nuevo_saldo
        return self.saldo_inicial
    
    def mostrar_saldo(self):
        "Muestra el sando que hay en la cuenta del titular"
        print(f'Saldo de {self.titular}: ${self.saldo_inicial}')

# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase Estudiante con calificaciones

# TODO: Define la clase Estudiante
# - Constructor que reciba: nombre
# - Atributos: self.nombre, self.calificaciones (lista vacía)
# - Método agregar_calificacion(nota) que agregue la nota a la lista
# - Método promedio() que devuelva el promedio de las calificaciones
#   (suma de calificaciones / cantidad de calificaciones)
# - Método __str__() que devuelva: "[nombre] - Promedio: [promedio]"
class Estudiante:
    def __init__(self, nombre):
        "Inicializador de los argumentos"
        self.nombre = nombre
        self.calificaciones = []
    
    def agregar_calificacion(self, nota):

        "Agrega las calificaciones a la lista"
        self.calificaciones.append(nota)
        print(f' Nota agredada ')
        return self.calificaciones
    
    def promedio(self):
        "Saca el promedio de las notas sobre la cantidad de notas"
        self.nota_promedio = sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else print(f'Error en digitación, no hay notas')
        return self.nota_promedio
    
    def __str__(self):
       "Solo trae la información que queda después de hacer el promedio del estudiante"
       return f'{self.nombre} - Promedio: {self.nota_promedio}'



# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea tu propia clase Tarea mejorada

# TODO: Define la clase Tarea
# - Constructor que reciba: descripcion
# - Atributos: 
#   * self.descripcion
#   * self.completada (False por defecto)
#   * self.prioridad ("media" por defecto)
# - Método completar() que marque completada = True
# - Método cambiar_prioridad(nueva_prioridad) que actualice la prioridad
# - Método __str__() que devuelva:
#   * Si completada: "✅ [descripcion] (Prioridad: [prioridad])"
#   * Si no: "⏳ [descripcion] (Prioridad: [prioridad])"
class Tarea:
    def __init__(self, descripcion):
        "Inicializador de los atributos de Tarea"
        self.descripcion = descripcion
        self.completada = False
        self.prioridad = 'media'
    
    def completar(self):
        "Convierte a true una tarea que se haya completado"
        self.completada= True
        print(f'La tarea {self.descripcion} fué completada') 
    
    def cambiar_prioridad (self, nueva_prioridad):
        "Cambia la prioridad de la tarea"
        self.prioridad = nueva_prioridad
        return self.prioridad
    
    def __str__(self):
        "Muestra la informacion de lo que se hizo con las tareas"
        estado = "✅" if self.completada else "⏳"
        return f'{estado} {self.descripcion} {self.prioridad}'
    
        

# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase para gestionar inventario

# TODO: Define la clase Producto
# - Constructor que reciba: nombre, precio, stock
# - Atributos: self.nombre, self.precio, self.stock
# - Método vender(cantidad):
#   * Si hay suficiente stock, restar la cantidad y devolver True
#   * Si no hay suficiente, imprimir "Stock insuficiente" y devolver False
# - Método reabastecer(cantidad) que sume al stock
# - Método info() que devuelva: "[nombre] - Precio: $[precio] - Stock: [stock]"

class Producto:
    def __init__(self, nombre, precio, stock):
        "Iniciador del producto"
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        "La venta que resta valor al stock"
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f' Producto {self.nombre} vendido! - Cantidad restante: {self.stock}')
            return True
        else: 
            print(f'Stock insuficiente para el producto {self.nombre}')
            return False
        
    def reabastecer(self, cantidad):
        "Operados que suma la cantidad al Stock"
        self.stock += cantidad
    def info(self):
        return f'{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}'

# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase que gestione múltiples tareas

# TODO: Define la clase TodoList
# - Constructor: inicializa self.tareas como lista vacía
# - Método agregar(descripcion):
#   * Crea una Tarea (usando la clase del ejercicio 4)
#   * La agrega a self.tareas
#   * Imprime: "➕ Tarea agregada: [descripcion]"
# - Método listar():
#   * Si no hay tareas: imprime "No hay tareas"
#   * Si hay tareas: muestra cada una con su número (1, 2, 3...)
# - Método completar_tarea(numero):
#   * Valida que el número sea válido
#   * Marca la tarea como completada
# - Método total() que devuelva la cantidad de tareas

class TodoList:

    def __init__(self):
        "Inicializa las tareas como lista vacía"
        self.tareas = []
    
    def agregar(self, descripcion):
        "Agrega una tarea usando la clase Tarea"
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f'➕ Tarea agregada: {descripcion}')
    
    def listar(self):
        if len(self.tareas) == 0:
            print(f"No hay tareas pendientes ")
        else:
            print(f"📝 Tienes {len(self.tareas)} tarea(s):")
            for i, tarea in enumerate(self.tareas, start = 1):
                print(f'#{i}. {tarea}')
    
    def completar_tarea(self, numero):
        "Convierte a true una tarea que se haya completado"
        if 1 <= numero <= len(self.tareas):
            self.tareas[numero-1].completar()
        else:
            print(f'Numero de tarea inválido')
    
    def total(self):
        "Muestra el total de tareas"
        return f'{len(self.tareas)}'
        

# Prueba tu clase (NO MODIFICAR)
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
# Instrucciones: Crea una clase simple con variable de clase

# TODO: Define la clase Contador
# - Variable de clase: total_instancias = 0
# - Constructor: incrementa total_instancias en 1
# - Método de clase (@classmethod) mostrar_total(cls):
#   * Imprime: "Total de contadores creados: [total_instancias]"

class Contador:
    total_instancias = 0
    def __init__(self):
        "Iniciador de los argumentos"
        Contador.total_instancias += 1
    

    @classmethod 
    def mostrar_total(cls):
        print(f'Total de instancias creadas {cls.total_instancias}')

    
        

# Prueba tu clase (NO MODIFICAR)
print("--- Ejercicio 7: Contador de instancias ---")
c1 = Contador()
c2 = Contador()
c3 = Contador()
Contador.mostrar_total()

print("\n=== FIN DE LOS EJERCICIOS ===")

# -----------------------------------------------
# 🏆 CRITERIOS DE ÉXITO
# -----------------------------------------------
# Para considerar estos ejercicios completados:
# 1. Todas las clases están definidas correctamente
# 2. Cada clase tiene su constructor __init__
# 3. Los métodos funcionan según lo especificado
# 4. El programa se ejecuta sin errores
# 5. Los objetos se crean y usan correctamente
#
# Ejecuta: python exercises_03.py

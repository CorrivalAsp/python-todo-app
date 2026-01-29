# Lección 3 - Programación Orientada a Objetos (Clases)
# Fecha: 27 de enero 2026

print("=== LECCIÓN 3: CLASES Y OBJETOS ===\n")

# -----------------------------------------------
# PARTE 1: ¿Qué es una clase?
# -----------------------------------------------

# Una CLASE es como un plano o molde para crear objetos
# Un OBJETO es una instancia de una clase

# Analogía: 
# - Clase = Plano de una casa
# - Objeto = La casa construida con ese plano

# -----------------------------------------------
# PARTE 2: Mi primera clase
# -----------------------------------------------

class Perro:
    """Representa un perro con nombre y edad."""
    
    # __init__ es el CONSTRUCTOR - se ejecuta al crear un objeto
    def __init__(self, nombre, edad):
        """Inicializa un nuevo perro."""
        self.nombre = nombre  # Atributo (característica)
        self.edad = edad      # Atributo (característica)
    
    # Método (acción que puede hacer el perro)
    def ladrar(self):
        """El perro ladra."""
        print(f"{self.nombre} dice: ¡Guau guau!")
    
    # Método con parámetros
    def cumplir_años(self):
        """El perro cumple un año más."""
        self.edad += 1
        print(f"¡{self.nombre} ahora tiene {self.edad} años!")
    
    # Método que devuelve información
    def descripcion(self):
        """Devuelve una descripción del perro."""
        return f"{self.nombre} es un perro de {self.edad} años"

# Crear objetos (instancias de la clase)
print("--- Creando objetos ---")
mi_perro = Perro("Max", 3)
tu_perro = Perro("Luna", 5)

# Usar métodos
mi_perro.ladrar()
tu_perro.ladrar()

# Acceder a atributos
print(f"Mi perro se llama: {mi_perro.nombre}")
print(f"Tu perro se llama: {tu_perro.nombre}")

# Usar métodos que modifican el objeto
mi_perro.cumplir_años()

# Usar métodos que devuelven valores
print(mi_perro.descripcion())
print()

# -----------------------------------------------
# PARTE 3: Clase para nuestra To-Do App
# -----------------------------------------------

class Tarea:
    """Representa una tarea individual."""
    
    def __init__(self, descripcion):
        """
        Crea una nueva tarea.
        
        Args:
            descripcion (str): Descripción de la tarea
        """
        self.descripcion = descripcion
        self.completada = False  # Por defecto, las tareas están pendientes
    
    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True
        print(f"✅ Tarea completada: {self.descripcion}")
    
    def marcar_pendiente(self):
        """Marca la tarea como pendiente."""
        self.completada = False
        print(f"⏳ Tarea marcada como pendiente: {self.descripcion}")
    
    def __str__(self):
        """
        Representación en string de la tarea.
        Este método especial se llama cuando usas print() o str()
        """
        estado = "✅" if self.completada else "⏳"
        return f"{estado} {self.descripcion}"

# Usar la clase Tarea
print("--- To-Do App con clases ---")

tarea1 = Tarea("Aprender clases en Python")
tarea2 = Tarea("Hacer ejercicios de POO")
tarea3 = Tarea("Crear clase Task mejorada")

print("Tareas creadas:")
print(tarea1)
print(tarea2)
print(tarea3)
print()

# Marcar una tarea como completada
tarea1.marcar_completada()
print("\nEstado actualizado:")
print(tarea1)
print()

# -----------------------------------------------
# PARTE 4: Clase con más funcionalidades
# -----------------------------------------------

class TareaAvanzada:
    """Tarea con más características."""
    
    # Variable de clase (compartida por todas las instancias)
    total_tareas = 0
    
    def __init__(self, descripcion, prioridad="media"):
        """
        Crea una tarea avanzada.
        
        Args:
            descripcion (str): Descripción de la tarea
            prioridad (str): Prioridad (alta, media, baja)
        """
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        
        # Incrementar el contador de clase
        TareaAvanzada.total_tareas += 1
    
    def __str__(self):
        """Representación en string."""
        estado = "✅" if self.completada else "⏳"
        prioridad_simbolo = {
            "alta": "🔴",
            "media": "🟡",
            "baja": "🟢"
        }
        simbolo = prioridad_simbolo.get(self.prioridad, "⚪")
        return f"{estado} {simbolo} {self.descripcion}"
    
    def cambiar_prioridad(self, nueva_prioridad):
        """Cambia la prioridad de la tarea."""
        self.prioridad = nueva_prioridad
        print(f"Prioridad cambiada a: {nueva_prioridad}")
    
    @classmethod
    def mostrar_total(cls):
        """Método de clase - muestra el total de tareas creadas."""
        print(f"Total de tareas creadas: {cls.total_tareas}")

print("--- Tareas avanzadas ---")
tarea_a = TareaAvanzada("Estudiar Python", "alta")
tarea_b = TareaAvanzada("Hacer ejercicio", "baja")
tarea_c = TareaAvanzada("Leer documentación", "media")

print(tarea_a)
print(tarea_b)
print(tarea_c)
print()

TareaAvanzada.mostrar_total()
print()

# -----------------------------------------------
# PARTE 5: Gestor de Tareas (clase que contiene otras clases)
# -----------------------------------------------

class GestorTareas:
    """Gestiona una lista de tareas."""
    
    def __init__(self):
        """Inicializa el gestor con una lista vacía."""
        self.tareas = []
    
    def agregar(self, descripcion):
        """Agrega una nueva tarea."""
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f"➕ Tarea agregada: {descripcion}")
    
    def listar(self):
        """Muestra todas las tareas."""
        if len(self.tareas) == 0:
            print("📭 No hay tareas")
        else:
            print(f"📝 Tienes {len(self.tareas)} tarea(s):")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"  {i}. {tarea}")
    
    def completar(self, numero):
        """Marca una tarea como completada."""
        if 1 <= numero <= len(self.tareas):
            self.tareas[numero - 1].marcar_completada()
        else:
            print("❌ Número de tarea inválido")
    
    def eliminar(self, numero):
        """Elimina una tarea."""
        if 1 <= numero <= len(self.tareas):
            tarea = self.tareas.pop(numero - 1)
            print(f"🗑️ Tarea eliminada: {tarea.descripcion}")
        else:
            print("❌ Número de tarea inválido")
    
    def pendientes(self):
        """Devuelve el número de tareas pendientes."""
        return sum(1 for tarea in self.tareas if not tarea.completada)
    
    def completadas(self):
        """Devuelve el número de tareas completadas."""
        return sum(1 for tarea in self.tareas if tarea.completada)

# Usar el GestorTareas
print("--- Gestor de Tareas Completo ---")

gestor = GestorTareas()

# Agregar tareas
gestor.agregar("Aprender POO")
gestor.agregar("Practicar clases")
gestor.agregar("Crear mi propia clase")
print()

# Listar tareas
gestor.listar()
print()

# Completar una tarea
gestor.completar(1)
print()

# Ver estado
gestor.listar()
print()

# Estadísticas
print(f"Pendientes: {gestor.pendientes()}")
print(f"Completadas: {gestor.completadas()}")

print("\n=== FIN DE LA LECCIÓN 3 ===")

# -----------------------------------------------
# 💡 CONCEPTOS IMPORTANTES
# -----------------------------------------------
#
# 1. CLASE vs OBJETO
#    - Clase: El molde/plantilla (class Perro)
#    - Objeto: La instancia creada (mi_perro = Perro("Max", 3))
#
# 2. __init__ (Constructor)
#    - Método especial que se ejecuta al crear un objeto
#    - Se usa para inicializar atributos
#
# 3. self
#    - Referencia al objeto actual
#    - Siempre es el primer parámetro de los métodos
#    - Se usa para acceder a atributos y otros métodos
#
# 4. ATRIBUTOS
#    - self.nombre, self.edad, self.completada
#    - Características del objeto
#
# 5. MÉTODOS
#    - Funciones que pertenecen a una clase
#    - Pueden acceder y modificar atributos
#
# 6. __str__
#    - Método especial para representación en string
#    - Se llama con print() o str()
#
# 7. Variables de clase vs Variables de instancia
#    - Clase: Compartidas por todos los objetos
#    - Instancia: Únicas para cada objeto

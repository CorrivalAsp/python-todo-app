# Lección 4 - Conceptos Avanzados de POO
# Fecha: 29 de enero 2026

print("=== LECCIÓN 4: CONCEPTOS AVANZADOS DE POO ===\n")

# -----------------------------------------------
# CONCEPTOS PREVIOS: Métodos y funciones que usaremos
# -----------------------------------------------
print("--- Conceptos Previos ---")

# 1. split() - Divide un string en partes
texto = "29/01/2026"
partes = texto.split('/')  # Divide por '/'
print(f"'{texto}'.split('/') = {partes}")  # ['29', '01', '2026']

# También funciona con espacios
frase = "Hola mundo Python"
palabras = frase.split(' ')  # Divide por espacio
print(f"'{frase}'.split(' ') = {palabras}")  # ['Hola', 'mundo', 'Python']

# 2. int() - Convierte string a número entero
numero_texto = "42"
numero = int(numero_texto)
print(f"int('{numero_texto}') = {numero} (tipo: {type(numero).__name__})")

# 3. ** - Operador de potencia
resultado = 2 ** 3  # 2 elevado a la 3
print(f"2 ** 3 = {resultado}")
print(f"10 ** 2 = {10 ** 2}")

# 4. range() - Genera secuencia de números
print(f"range(2, 6) genera: {list(range(2, 6))}")  # [2, 3, 4, 5]
print(f"range(5) genera: {list(range(5))}")  # [0, 1, 2, 3, 4]

# 5. Formato :02d - Número con 2 dígitos (rellena con 0)
dia = 5
mes = 12
print(f"Día {dia} formateado: {dia:02d}")  # 05
print(f"Mes {mes} formateado: {mes:02d}")  # 12
print(f"Fecha: {dia:02d}/{mes:02d}/2026")  # 05/12/2026

print("\n" + "="*50 + "\n")

# -----------------------------------------------
# PARTE 1: MÁS SOBRE @classmethod - Factory Methods
# -----------------------------------------------

class Fecha:
    """Clase para representar fechas con múltiples constructores."""
    
    def __init__(self, dia, mes, año):
        """Constructor principal."""
        self.dia = dia
        self.mes = mes
        self.año = año
    
    @classmethod
    def desde_string(cls, fecha_str):
        """
        Constructor alternativo desde string.
        Ejemplo: Fecha.desde_string("29/01/2026")
        """
        dia, mes, año = fecha_str.split('/')
        return cls(int(dia), int(mes), int(año))
    
    @classmethod
    def hoy(cls):
        """Constructor que crea la fecha de hoy."""
        from datetime import date
        hoy = date.today()
        return cls(hoy.day, hoy.month, hoy.year)
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

# Usar diferentes constructores
print("--- Factory Methods con @classmethod ---")
fecha1 = Fecha(29, 1, 2026)  # Constructor normal
fecha2 = Fecha.desde_string("15/03/2025")  # Desde string
fecha3 = Fecha.hoy()  # Fecha de hoy

print(f"Fecha 1: {fecha1}")
print(f"Fecha 2: {fecha2}")
print(f"Fecha 3 (hoy): {fecha3}")
print()

# -----------------------------------------------
# PARTE 2: @staticmethod - Métodos sin self ni cls
# -----------------------------------------------

class Matematicas:
    """Clase con métodos estáticos (utilidades)."""
    
    @staticmethod
    def es_par(numero):
        """Verifica si un número es par."""
        return numero % 2 == 0
    
    @staticmethod
    def es_primo(numero):
        """Verifica si un número es primo."""
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """Calcula el factorial de un número."""
        if n <= 1:
            return 1
        return n * Matematicas.factorial(n - 1)

# Usar métodos estáticos (no necesitas crear un objeto)
print("--- Métodos Estáticos (@staticmethod) ---")
print(f"5 es par? {Matematicas.es_par(5)}")
print(f"8 es par? {Matematicas.es_par(8)}")
print(f"7 es primo? {Matematicas.es_primo(7)}")
print(f"Factorial de 5: {Matematicas.factorial(5)}")
print()

# -----------------------------------------------
# PARTE 3: Métodos Mágicos (Dunder Methods)
# -----------------------------------------------

class Producto:
    """Producto con métodos mágicos."""
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        """Para print() - versión amigable."""
        return f"{self.nombre}: ${self.precio}"
    
    def __repr__(self):
        """Para debugging - versión técnica."""
        return f"Producto('{self.nombre}', {self.precio})"
    
    def __eq__(self, otro):
        """Para comparar con == (igualdad)."""
        return self.precio == otro.precio
    
    def __lt__(self, otro):
        """Para comparar con < (menor que)."""
        return self.precio < otro.precio
    
    def __add__(self, otro):
        """Para sumar productos con +."""
        return self.precio + otro.precio

print("--- Métodos Mágicos ---")
p1 = Producto("Laptop", 1000)
p2 = Producto("Mouse", 50)
p3 = Producto("Teclado", 1000)

print(f"str(p1): {str(p1)}")  # Llama a __str__
print(f"repr(p1): {repr(p1)}")  # Llama a __repr__
print(f"p1 == p3: {p1 == p3}")  # Llama a __eq__ (True, mismo precio)
print(f"p2 < p1: {p2 < p1}")  # Llama a __lt__ (True, 50 < 1000)
print(f"p1 + p2: ${p1 + p2}")  # Llama a __add__
print()

# -----------------------------------------------
# PARTE 4: __len__ - Para usar len(objeto)
# -----------------------------------------------

class Carrito:
    """Carrito de compras con __len__."""
    
    def __init__(self):
        self.productos = []
    
    def agregar(self, producto):
        self.productos.append(producto)
    
    def __len__(self):
        """Permite usar len(carrito)."""
        return len(self.productos)
    
    def __str__(self):
        if len(self.productos) == 0:
            return "Carrito vacío"
        return f"Carrito con {len(self)} producto(s)"

print("--- Método __len__ ---")
carrito = Carrito()
print(f"Carrito vacío - len: {len(carrito)}")

carrito.agregar(Producto("Laptop", 1000))
carrito.agregar(Producto("Mouse", 50))
print(f"Después de agregar - len: {len(carrito)}")
print(carrito)
print()

# -----------------------------------------------
# PARTE 5: @property - Getters y Setters Elegantes
# -----------------------------------------------

class Persona:
    """Persona con validación de edad usando @property."""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  # Atributo "privado" (convención con _)
    
    @property
    def edad(self):
        """Getter - Se accede como persona.edad (sin paréntesis)."""
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        """Setter - Se usa como persona.edad = 30."""
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if nueva_edad > 150:
            raise ValueError("La edad no puede ser mayor a 150")
        self._edad = nueva_edad
    
    @property
    def es_mayor_edad(self):
        """Propiedad calculada (sin setter)."""
        return self._edad >= 18

print("--- Propiedades (@property) ---")
persona = Persona("Ana", 25)

# Acceder como atributo (sin paréntesis)
print(f"Edad: {persona.edad}")
print(f"¿Es mayor de edad? {persona.es_mayor_edad}")

# Modificar con validación
persona.edad = 30  # Llama al setter
print(f"Nueva edad: {persona.edad}")

# Intentar valor inválido
try:
    persona.edad = -5  # ❌ Error
except ValueError as e:
    print(f"Error: {e}")
print()

# -----------------------------------------------
# PARTE 6: Combinando Todo - Clase Banco
# -----------------------------------------------

class CuentaBancaria:
    """Cuenta bancaria con conceptos avanzados."""
    
    # Variable de clase
    total_cuentas = 0
    tasa_interes = 0.03
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial
        CuentaBancaria.total_cuentas += 1
    
    # Factory method
    @classmethod
    def crear_cuenta_ahorro(cls, titular, saldo_inicial):
        """Crea una cuenta con tasa de interés especial."""
        cuenta = cls(titular, saldo_inicial)
        return cuenta
    
    # Método estático
    @staticmethod
    def calcular_interes(monto, años):
        """Calcula interés compuesto."""
        return monto * ((1 + CuentaBancaria.tasa_interes) ** años)
    
    # Property
    @property
    def saldo(self):
        """Getter del saldo."""
        return self._saldo
    
    # Métodos mágicos
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.saldo:.2f}"
    
    def __eq__(self, otra):
        return self.saldo == otra.saldo
    
    def __lt__(self, otra):
        return self.saldo < otra.saldo
    
    def __add__(self, otra):
        """Suma los saldos de dos cuentas."""
        return self.saldo + otra.saldo
    
    # Método de clase
    @classmethod
    def mostrar_total_cuentas(cls):
        print(f"Total de cuentas creadas: {cls.total_cuentas}")

print("--- Clase Completa con Todo ---")

# Crear cuentas
c1 = CuentaBancaria("Ana", 1000)
c2 = CuentaBancaria.crear_cuenta_ahorro("Carlos", 2000)

print(c1)  # __str__
print(c2)

# Comparaciones
print(f"c1 < c2: {c1 < c2}")  # __lt__

# Sumar saldos
print(f"Saldo total: ${c1 + c2}")  # __add__

# Método estático
interes = CuentaBancaria.calcular_interes(1000, 5)
print(f"$1000 en 5 años: ${interes:.2f}")

# Método de clase
CuentaBancaria.mostrar_total_cuentas()

print("\n=== FIN DE LA LECCIÓN 4 ===")

# -----------------------------------------------
# 💡 RESUMEN DE CONCEPTOS
# -----------------------------------------------
#
# 1. @classmethod:
#    - Primer parámetro: cls (la clase)
#    - Útil para: factory methods, modificar variables de clase
#    - Ejemplo: Fecha.desde_string("29/01/2026")
#
# 2. @staticmethod:
#    - No recibe self ni cls
#    - Útil para: utilidades relacionadas con la clase
#    - Ejemplo: Matematicas.es_par(5)
#
# 3. Métodos Mágicos:
#    - __str__: print(objeto)
#    - __repr__: repr(objeto) - debugging
#    - __eq__: objeto1 == objeto2
#    - __lt__: objeto1 < objeto2
#    - __add__: objeto1 + objeto2
#    - __len__: len(objeto)
#
# 4. @property:
#    - Getter: acceder como atributo (sin paréntesis)
#    - Setter: validar antes de asignar
#    - Propiedades calculadas: sin setter

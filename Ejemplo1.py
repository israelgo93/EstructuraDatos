"""
DIFERENCIA CLARA:

TAD NumeroComplejo (especificación abstracta):
==============================================
- CONCEPTO: Representar números de la forma a + bi
- OPERACIONES REQUERIDAS: crear, sumar, restar, obtener partes
- NO ESPECIFICA: cómo almacenar, qué algoritmos usar

ESTRUCTURA DE DATOS (implementación concreta):
==============================================
"""

# Esto es la ESTRUCTURA DE DATOS
class NumeroComplejo:
    """
    DECISIONES DE IMPLEMENTACIÓN que tomamos:
    1. Usar clase de Python
    2. Almacenar en dos atributos separados
    3. Usar tipos float de Python
    4. Algoritmo directo para suma
    """
    
    def __init__(self, real, imaginario):
        # DECISIÓN: usar atributos separados
        self.real = float(real)           # DECISIÓN: convertir a float
        self.imaginario = float(imaginario)
    
    def sumar(self, otro):
        # DECISIÓN: algoritmo específico de suma
        nueva_real = self.real + otro.real
        nueva_imag = self.imaginario + otro.imaginario
        return NumeroComplejo(nueva_real, nueva_imag)
    
    def __str__(self):
        # DECISIÓN: formato de presentación específico
        return f"{self.real} + {self.imaginario}i"

# Uso (esto también es parte de la estructura de datos)
c1 = NumeroComplejo(4, 4)    # DECISIÓN: sintaxis de Python
c2 = NumeroComplejo(1, 2)
resultado = c1.sumar(c2)     # DECISIÓN: método específico
print(resultado)             # Output: 5.0 + 6.0i
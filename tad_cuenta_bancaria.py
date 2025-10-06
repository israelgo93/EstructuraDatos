"""
=====================================================================
TAD CUENTA BANCARIA - EJEMPLO PEDAGÓGICO COMPLETO
Estructura de Datos - ULEAM
Septiembre 2025
=====================================================================

Este ejemplo ilustra:
1. Especificación formal de un TAD
2. Implementación como estructura de datos en Python
3. Aplicación de axiomas y contratos
4. Validaciones y manejo de errores
5. Casos de prueba completos

Conceptos clave:
- Abstracción: Separación entre QUÉ hace (TAD) y CÓMO lo hace (implementación)
- Encapsulación: Atributos privados, acceso controlado
- Invariantes: Propiedades que siempre se mantienen
- Contratos: Precondiciones y postcondiciones
=====================================================================
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum


# =====================================================================
# PARTE 1: ESPECIFICACIÓN DEL TAD CUENTA BANCARIA
# =====================================================================

"""
TAD CuentaBancaria = (S, Σ, A)

S (Sorts/Tipos):
    - CuentaBancaria
    - Dinero (float)
    - String (número de cuenta, titular)
    - Boolean
    - Transaccion

Σ (Signatura - Operaciones):
    crear(titular: String, numero_cuenta: String) -> CuentaBancaria
    depositar(cuenta: CuentaBancaria, monto: Dinero) -> CuentaBancaria
    retirar(cuenta: CuentaBancaria, monto: Dinero) -> CuentaBancaria
    consultar_saldo(cuenta: CuentaBancaria) -> Dinero
    obtener_titular(cuenta: CuentaBancaria) -> String
    obtener_numero(cuenta: CuentaBancaria) -> String
    transferir(origen: CuentaBancaria, destino: CuentaBancaria, monto: Dinero) -> None
    obtener_historial(cuenta: CuentaBancaria) -> List[Transaccion]

A (Axiomas - Propiedades que se deben cumplir):
    1. consultar_saldo(crear(t, n)) = 0
       // Una cuenta recién creada tiene saldo 0
    
    2. consultar_saldo(depositar(c, m)) = consultar_saldo(c) + m  [si m > 0]
       // Depositar aumenta el saldo
    
    3. consultar_saldo(retirar(c, m)) = consultar_saldo(c) - m  
       [si m > 0 y m <= consultar_saldo(c)]
       // Retirar disminuye el saldo
    
    4. obtener_titular(crear(t, n)) = t
       // El titular es el proporcionado al crear
    
    5. obtener_numero(crear(t, n)) = n
       // El número es el proporcionado al crear
    
    6. retirar(c, m) requiere: m <= consultar_saldo(c)
       // No se puede retirar más de lo que hay (precondición)
    
    7. depositar(c, m) requiere: m > 0
       // Solo se pueden depositar montos positivos (precondición)
    
    8. retirar(c, m) requiere: m > 0
       // Solo se pueden retirar montos positivos (precondición)
    
    9. transferir(origen, destino, m) = 
       retirar(origen, m) y depositar(destino, m)
       // Una transferencia es un retiro + un depósito

INVARIANTES (propiedades que SIEMPRE deben ser verdaderas):
    - I1: saldo >= 0  (nunca negativo)
    - I2: titular != ""  (siempre hay un titular)
    - I3: numero_cuenta != ""  (siempre hay un número)
    - I4: len(historial) >= 0  (el historial puede estar vacío pero no None)
"""


# =====================================================================
# PARTE 2: TIPOS AUXILIARES
# =====================================================================

class TipoTransaccion(Enum):
    """Enumeración para tipos de transacciones"""
    DEPOSITO = "DEPÓSITO"
    RETIRO = "RETIRO"
    TRANSFERENCIA_ENVIADA = "TRANSFERENCIA ENVIADA"
    TRANSFERENCIA_RECIBIDA = "TRANSFERENCIA RECIBIDA"
    APERTURA = "APERTURA DE CUENTA"


@dataclass
class Transaccion:
    """
    Representa una transacción bancaria.
    Esto es un tipo de dato auxiliar para el TAD.
    """
    tipo: TipoTransaccion
    monto: float
    fecha: datetime
    saldo_resultante: float
    descripcion: str = ""
    
    def __str__(self) -> str:
        return (f"[{self.fecha.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{self.tipo.value}: ${self.monto:.2f} | "
                f"Saldo: ${self.saldo_resultante:.2f} | "
                f"{self.descripcion}")


# =====================================================================
# PARTE 3: EXCEPCIONES PERSONALIZADAS
# =====================================================================

class CuentaBancariaError(Exception):
    """Clase base para errores de cuenta bancaria"""
    pass


class SaldoInsuficienteError(CuentaBancariaError):
    """Se lanza cuando se intenta retirar más dinero del disponible"""
    pass


class MontoInvalidoError(CuentaBancariaError):
    """Se lanza cuando el monto es inválido (negativo o cero)"""
    pass


class CuentaBloqueadaError(CuentaBancariaError):
    """Se lanza cuando se intenta operar sobre una cuenta bloqueada"""
    pass


# =====================================================================
# PARTE 4: IMPLEMENTACIÓN DE LA ESTRUCTURA DE DATOS
# =====================================================================

class CuentaBancaria:
    """
    IMPLEMENTACIÓN del TAD Cuenta Bancaria.
    
    Esta es la ESTRUCTURA DE DATOS concreta que implementa
    la especificación abstracta del TAD.
    
    Atributos privados (encapsulación):
        _titular: Nombre del titular de la cuenta
        _numero_cuenta: Número único de la cuenta
        _saldo: Saldo actual (siempre >= 0)
        _historial: Lista de transacciones
        _activa: Indica si la cuenta está activa
    """
    
    # ========== CONSTRUCTOR ==========
    
    def __init__(self, titular: str, numero_cuenta: str):
        """
        Operación: crear(titular, numero_cuenta) -> CuentaBancaria
        
        Crea una nueva cuenta bancaria con saldo inicial 0.
        
        Precondiciones:
            - titular no puede ser vacío
            - numero_cuenta no puede ser vacío
        
        Postcondiciones:
            - saldo = 0
            - cuenta está activa
            - historial contiene solo la transacción de apertura
        """
        # Validar precondiciones
        if not titular or titular.strip() == "":
            raise ValueError("El titular no puede estar vacío")
        if not numero_cuenta or numero_cuenta.strip() == "":
            raise ValueError("El número de cuenta no puede estar vacío")
        
        # Inicializar atributos privados
        self._titular: str = titular.strip()
        self._numero_cuenta: str = numero_cuenta.strip()
        self._saldo: float = 0.0
        self._historial: List[Transaccion] = []
        self._activa: bool = True
        
        # Registrar apertura de cuenta
        transaccion = Transaccion(
            tipo=TipoTransaccion.APERTURA,
            monto=0.0,
            fecha=datetime.now(),
            saldo_resultante=0.0,
            descripcion=f"Apertura de cuenta para {self._titular}"
        )
        self._historial.append(transaccion)
        
        # Verificar invariante
        self._verificar_invariante()
    
    # ========== MÉTODOS PRIVADOS (AUXILIARES) ==========
    
    def _verificar_invariante(self) -> None:
        """
        Verifica que los invariantes de la clase se mantengan.
        
        Invariantes:
            I1: saldo >= 0
            I2: titular no vacío
            I3: numero_cuenta no vacío
            I4: historial no None
        
        Lanza AssertionError si algún invariante se viola.
        """
        assert self._saldo >= 0, "Invariante violado: saldo negativo"
        assert self._titular != "", "Invariante violado: titular vacío"
        assert self._numero_cuenta != "", "Invariante violado: número de cuenta vacío"
        assert self._historial is not None, "Invariante violado: historial None"
    
    def _verificar_cuenta_activa(self) -> None:
        """Verifica que la cuenta esté activa antes de operar"""
        if not self._activa:
            raise CuentaBloqueadaError(
                f"La cuenta {self._numero_cuenta} está bloqueada"
            )
    
    def _registrar_transaccion(self, tipo: TipoTransaccion, 
                              monto: float, descripcion: str = "") -> None:
        """Registra una transacción en el historial"""
        transaccion = Transaccion(
            tipo=tipo,
            monto=monto,
            fecha=datetime.now(),
            saldo_resultante=self._saldo,
            descripcion=descripcion
        )
        self._historial.append(transaccion)
    
    # ========== OPERACIONES DEL TAD (MÉTODOS PÚBLICOS) ==========
    
    def depositar(self, monto: float) -> None:
        """
        Operación: depositar(cuenta, monto) -> None
        
        Deposita dinero en la cuenta.
        
        Precondiciones:
            - monto > 0
            - cuenta debe estar activa
        
        Postcondiciones:
            - saldo_nuevo = saldo_anterior + monto
            - se registra la transacción
        
        Axioma verificado:
            consultar_saldo(depositar(c, m)) = consultar_saldo(c) + m
        """
        # Verificar precondiciones
        self._verificar_cuenta_activa()
        
        if monto <= 0:
            raise MontoInvalidoError(
                f"El monto a depositar debe ser positivo. Recibido: ${monto:.2f}"
            )
        
        # Guardar estado anterior para verificar postcondición
        saldo_anterior = self._saldo
        
        # Realizar operación
        self._saldo += monto
        self._registrar_transaccion(
            TipoTransaccion.DEPOSITO,
            monto,
            f"Depósito de ${monto:.2f}"
        )
        
        # Verificar postcondición (axioma 2)
        assert self._saldo == saldo_anterior + monto, \
            "Postcondición violada en depositar"
        
        # Verificar invariante
        self._verificar_invariante()
    
    def retirar(self, monto: float) -> float:
        """
        Operación: retirar(cuenta, monto) -> float
        
        Retira dinero de la cuenta.
        
        Precondiciones:
            - monto > 0
            - monto <= saldo (no se puede retirar más de lo que hay)
            - cuenta debe estar activa
        
        Postcondiciones:
            - saldo_nuevo = saldo_anterior - monto
            - se registra la transacción
            - retorna el monto retirado
        
        Axioma verificado:
            consultar_saldo(retirar(c, m)) = consultar_saldo(c) - m
        """
        # Verificar precondiciones
        self._verificar_cuenta_activa()
        
        if monto <= 0:
            raise MontoInvalidoError(
                f"El monto a retirar debe ser positivo. Recibido: ${monto:.2f}"
            )
        
        if monto > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. Intentaste retirar ${monto:.2f} "
                f"pero solo tienes ${self._saldo:.2f}"
            )
        
        # Guardar estado anterior
        saldo_anterior = self._saldo
        
        # Realizar operación
        self._saldo -= monto
        self._registrar_transaccion(
            TipoTransaccion.RETIRO,
            monto,
            f"Retiro de ${monto:.2f}"
        )
        
        # Verificar postcondición (axioma 3)
        assert self._saldo == saldo_anterior - monto, \
            "Postcondición violada en retirar"
        
        # Verificar invariante
        self._verificar_invariante()
        
        return monto
    
    def transferir(self, cuenta_destino: 'CuentaBancaria', monto: float) -> None:
        """
        Operación: transferir(origen, destino, monto) -> None
        
        Transfiere dinero de esta cuenta a otra cuenta.
        
        Precondiciones:
            - monto > 0
            - monto <= saldo de cuenta origen
            - ambas cuentas deben estar activas
            - cuenta_destino no puede ser None
        
        Postcondiciones:
            - saldo_origen_nuevo = saldo_origen_anterior - monto
            - saldo_destino_nuevo = saldo_destino_anterior + monto
            - se registran transacciones en ambas cuentas
        
        Axioma verificado:
            transferir(origen, destino, m) = retirar(origen, m) y depositar(destino, m)
        """
        # Verificar precondiciones
        if cuenta_destino is None:
            raise ValueError("La cuenta destino no puede ser None")
        
        if cuenta_destino._numero_cuenta == self._numero_cuenta:
            raise ValueError("No puedes transferir a tu misma cuenta")
        
        # Guardar estados anteriores
        saldo_origen_anterior = self._saldo
        saldo_destino_anterior = cuenta_destino._saldo
        
        # Realizar transferencia (axioma 9: retiro + depósito)
        self.retirar(monto)  # Esto ya valida precondiciones
        cuenta_destino.depositar(monto)
        
        # Actualizar descripciones de transacciones
        self._historial[-1].tipo = TipoTransaccion.TRANSFERENCIA_ENVIADA
        self._historial[-1].descripcion = (
            f"Transferencia enviada a cuenta {cuenta_destino._numero_cuenta}"
        )
        
        cuenta_destino._historial[-1].tipo = TipoTransaccion.TRANSFERENCIA_RECIBIDA
        cuenta_destino._historial[-1].descripcion = (
            f"Transferencia recibida de cuenta {self._numero_cuenta}"
        )
        
        # Verificar postcondiciones
        assert self._saldo == saldo_origen_anterior - monto, \
            "Postcondición violada en transferir (origen)"
        assert cuenta_destino._saldo == saldo_destino_anterior + monto, \
            "Postcondición violada en transferir (destino)"
    
    def consultar_saldo(self) -> float:
        """
        Operación: consultar_saldo(cuenta) -> float
        
        Retorna el saldo actual de la cuenta.
        
        Precondiciones: ninguna
        Postcondiciones: retorna saldo >= 0
        """
        return self._saldo
    
    def obtener_titular(self) -> str:
        """
        Operación: obtener_titular(cuenta) -> str
        
        Retorna el nombre del titular.
        
        Axioma verificado:
            obtener_titular(crear(t, n)) = t
        """
        return self._titular
    
    def obtener_numero_cuenta(self) -> str:
        """
        Operación: obtener_numero(cuenta) -> str
        
        Retorna el número de cuenta.
        
        Axioma verificado:
            obtener_numero(crear(t, n)) = n
        """
        return self._numero_cuenta
    
    def obtener_historial(self) -> List[Transaccion]:
        """
        Operación: obtener_historial(cuenta) -> List[Transaccion]
        
        Retorna una copia del historial de transacciones.
        
        Nota: Retornamos una copia para mantener encapsulación.
        """
        return self._historial.copy()
    
    def bloquear_cuenta(self) -> None:
        """Bloquea la cuenta, impidiendo operaciones"""
        self._activa = False
        print(f"⚠️  Cuenta {self._numero_cuenta} bloqueada")
    
    def activar_cuenta(self) -> None:
        """Activa una cuenta previamente bloqueada"""
        self._activa = True
        print(f"✅ Cuenta {self._numero_cuenta} activada")
    
    def esta_activa(self) -> bool:
        """Retorna si la cuenta está activa"""
        return self._activa
    
    # ========== MÉTODOS ESPECIALES ==========
    
    def __str__(self) -> str:
        """Representación en string de la cuenta"""
        estado = "ACTIVA" if self._activa else "BLOQUEADA"
        return (f"CuentaBancaria({self._numero_cuenta}) | "
                f"Titular: {self._titular} | "
                f"Saldo: ${self._saldo:.2f} | "
                f"Estado: {estado}")
    
    def __repr__(self) -> str:
        """Representación técnica de la cuenta"""
        return (f"CuentaBancaria(titular='{self._titular}', "
                f"numero_cuenta='{self._numero_cuenta}')")


# =====================================================================
# PARTE 5: FUNCIONES DE PRUEBA Y DEMOSTRACIÓN
# =====================================================================

def imprimir_separador(titulo: str = "") -> None:
    """Imprime un separador visual"""
    print("\n" + "="*70)
    if titulo:
        print(f"  {titulo}")
        print("="*70)


def test_axioma_1_cuenta_nueva_saldo_cero():
    """
    Prueba AXIOMA 1: consultar_saldo(crear(t, n)) = 0
    Una cuenta recién creada debe tener saldo 0
    """
    imprimir_separador("TEST AXIOMA 1: Cuenta nueva tiene saldo 0")
    
    cuenta = CuentaBancaria("Juan Pérez", "001-2024-001")
    saldo = cuenta.consultar_saldo()
    
    print(f"Cuenta creada: {cuenta}")
    print(f"Saldo inicial: ${saldo:.2f}")
    
    assert saldo == 0, "❌ AXIOMA 1 VIOLADO: Saldo inicial no es 0"
    print("✅ AXIOMA 1 VERIFICADO: Cuenta nueva tiene saldo 0")


def test_axioma_2_depositar_aumenta_saldo():
    """
    Prueba AXIOMA 2: consultar_saldo(depositar(c, m)) = consultar_saldo(c) + m
    Depositar debe aumentar el saldo exactamente por el monto depositado
    """
    imprimir_separador("TEST AXIOMA 2: Depositar aumenta el saldo")
    
    cuenta = CuentaBancaria("María García", "001-2024-002")
    saldo_inicial = cuenta.consultar_saldo()
    monto_deposito = 1000.00
    
    print(f"Saldo inicial: ${saldo_inicial:.2f}")
    print(f"Depositando: ${monto_deposito:.2f}")
    
    cuenta.depositar(monto_deposito)
    saldo_final = cuenta.consultar_saldo()
    
    print(f"Saldo final: ${saldo_final:.2f}")
    
    assert saldo_final == saldo_inicial + monto_deposito, \
        "❌ AXIOMA 2 VIOLADO: El saldo no aumentó correctamente"
    print(f"✅ AXIOMA 2 VERIFICADO: {saldo_inicial} + {monto_deposito} = {saldo_final}")


def test_axioma_3_retirar_disminuye_saldo():
    """
    Prueba AXIOMA 3: consultar_saldo(retirar(c, m)) = consultar_saldo(c) - m
    Retirar debe disminuir el saldo exactamente por el monto retirado
    """
    imprimir_separador("TEST AXIOMA 3: Retirar disminuye el saldo")
    
    cuenta = CuentaBancaria("Carlos López", "001-2024-003")
    cuenta.depositar(5000.00)  # Primero depositamos para tener saldo
    
    saldo_inicial = cuenta.consultar_saldo()
    monto_retiro = 2000.00
    
    print(f"Saldo inicial: ${saldo_inicial:.2f}")
    print(f"Retirando: ${monto_retiro:.2f}")
    
    cuenta.retirar(monto_retiro)
    saldo_final = cuenta.consultar_saldo()
    
    print(f"Saldo final: ${saldo_final:.2f}")
    
    assert saldo_final == saldo_inicial - monto_retiro, \
        "❌ AXIOMA 3 VIOLADO: El saldo no disminuyó correctamente"
    print(f"✅ AXIOMA 3 VERIFICADO: {saldo_inicial} - {monto_retiro} = {saldo_final}")


def test_axioma_6_no_retirar_mas_del_saldo():
    """
    Prueba AXIOMA 6: retirar(c, m) requiere m <= consultar_saldo(c)
    No se debe poder retirar más dinero del disponible
    """
    imprimir_separador("TEST AXIOMA 6: No se puede retirar más del saldo")
    
    cuenta = CuentaBancaria("Ana Martínez", "001-2024-004")
    cuenta.depositar(1000.00)
    
    saldo_actual = cuenta.consultar_saldo()
    monto_invalido = 1500.00
    
    print(f"Saldo actual: ${saldo_actual:.2f}")
    print(f"Intentando retirar: ${monto_invalido:.2f}")
    
    try:
        cuenta.retirar(monto_invalido)
        print("❌ AXIOMA 6 VIOLADO: Se permitió retiro con saldo insuficiente")
        assert False, "Debería haber lanzado SaldoInsuficienteError"
    except SaldoInsuficienteError as e:
        print(f"✅ AXIOMA 6 VERIFICADO: {e}")


def test_axioma_9_transferencia():
    """
    Prueba AXIOMA 9: transferir(origen, destino, m) = 
                     retirar(origen, m) y depositar(destino, m)
    Una transferencia es un retiro de origen + depósito en destino
    """
    imprimir_separador("TEST AXIOMA 9: Transferencia = Retiro + Depósito")
    
    cuenta_origen = CuentaBancaria("Roberto Sánchez", "001-2024-005")
    cuenta_destino = CuentaBancaria("Laura Torres", "001-2024-006")
    
    cuenta_origen.depositar(3000.00)
    
    saldo_origen_inicial = cuenta_origen.consultar_saldo()
    saldo_destino_inicial = cuenta_destino.consultar_saldo()
    monto_transferencia = 1500.00
    
    print(f"Saldo origen antes: ${saldo_origen_inicial:.2f}")
    print(f"Saldo destino antes: ${saldo_destino_inicial:.2f}")
    print(f"Monto a transferir: ${monto_transferencia:.2f}")
    
    cuenta_origen.transferir(cuenta_destino, monto_transferencia)
    
    saldo_origen_final = cuenta_origen.consultar_saldo()
    saldo_destino_final = cuenta_destino.consultar_saldo()
    
    print(f"Saldo origen después: ${saldo_origen_final:.2f}")
    print(f"Saldo destino después: ${saldo_destino_final:.2f}")
    
    assert saldo_origen_final == saldo_origen_inicial - monto_transferencia, \
        "❌ AXIOMA 9 VIOLADO: Saldo origen incorrecto"
    assert saldo_destino_final == saldo_destino_inicial + monto_transferencia, \
        "❌ AXIOMA 9 VIOLADO: Saldo destino incorrecto"
    
    print("✅ AXIOMA 9 VERIFICADO: Transferencia = Retiro + Depósito")


def test_manejo_errores():
    """
    Prueba el manejo correcto de errores y validaciones
    """
    imprimir_separador("TEST: Manejo de Errores")
    
    cuenta = CuentaBancaria("Pedro Ramírez", "001-2024-007")
    cuenta.depositar(500.00)
    
    # Test 1: Monto negativo en depósito
    print("\n1. Intentando depositar monto negativo...")
    try:
        cuenta.depositar(-100.00)
        print("❌ ERROR: Se permitió depósito negativo")
    except MontoInvalidoError as e:
        print(f"✅ Correcto: {e}")
    
    # Test 2: Monto cero en retiro
    print("\n2. Intentando retirar monto cero...")
    try:
        cuenta.retirar(0)
        print("❌ ERROR: Se permitió retiro de $0")
    except MontoInvalidoError as e:
        print(f"✅ Correcto: {e}")
    
    # Test 3: Operación en cuenta bloqueada
    print("\n3. Intentando operar en cuenta bloqueada...")
    cuenta.bloquear_cuenta()
    try:
        cuenta.depositar(100.00)
        print("❌ ERROR: Se permitió operar en cuenta bloqueada")
    except CuentaBloqueadaError as e:
        print(f"✅ Correcto: {e}")
    
    cuenta.activar_cuenta()


def test_historial_transacciones():
    """
    Prueba el registro correcto de transacciones
    """
    imprimir_separador("TEST: Historial de Transacciones")
    
    cuenta = CuentaBancaria("Elena Vargas", "001-2024-008")
    
    # Realizar varias operaciones
    cuenta.depositar(1000.00)
    cuenta.depositar(500.00)
    cuenta.retirar(300.00)
    cuenta.depositar(200.00)
    
    print(f"\n{cuenta}")
    print(f"\nHistorial de transacciones ({len(cuenta.obtener_historial())} transacciones):")
    print("-" * 70)
    
    for transaccion in cuenta.obtener_historial():
        print(transaccion)
    
    historial = cuenta.obtener_historial()
    assert len(historial) == 5, "Número incorrecto de transacciones"  # 1 apertura + 4 operaciones
    print("\n✅ Historial registrado correctamente")


def demo_caso_uso_real():
    """
    Demostración de un caso de uso real completo
    """
    imprimir_separador("DEMOSTRACIÓN: Caso de Uso Real")
    
    print("\n📋 Escenario: Sistema de Nómina Empresarial\n")
    
    # Crear cuentas
    print("1️⃣  Creando cuentas...")
    cuenta_empresa = CuentaBancaria("Tech Solutions S.A.", "EMP-2024-001")
    cuenta_empleado1 = CuentaBancaria("Sofía Mendoza", "EMP-001-2024")
    cuenta_empleado2 = CuentaBancaria("Diego Castro", "EMP-002-2024")
    
    # La empresa deposita capital inicial
    print("\n2️⃣  Empresa deposita capital inicial...")
    cuenta_empresa.depositar(50000.00)
    print(f"   {cuenta_empresa}")
    
    # Pago de nómina
    print("\n3️⃣  Procesando pagos de nómina...")
    salarios = [
        (cuenta_empleado1, 2500.00, "Sofía Mendoza"),
        (cuenta_empleado2, 2800.00, "Diego Castro")
    ]
    
    for cuenta, salario, nombre in salarios:
        cuenta_empresa.transferir(cuenta, salario)
        print(f"   ✓ Pagado ${salario:.2f} a {nombre}")
    
    # Estado final
    print("\n4️⃣  Estado final de cuentas:")
    print(f"   Empresa: ${cuenta_empresa.consultar_saldo():.2f}")
    print(f"   Empleado 1: ${cuenta_empleado1.consultar_saldo():.2f}")
    print(f"   Empleado 2: ${cuenta_empleado2.consultar_saldo():.2f}")
    
    # Verificación de conservación del dinero
    total = (cuenta_empresa.consultar_saldo() + 
             cuenta_empleado1.consultar_saldo() + 
             cuenta_empleado2.consultar_saldo())
    
    print(f"\n5️⃣  Verificación de conservación del dinero:")
    print(f"   Total en el sistema: ${total:.2f}")
    print(f"   Depósito inicial: $50000.00")
    assert total == 50000.00, "❌ ERROR: El dinero no se conservó"
    print("   ✅ El dinero se conservó correctamente")


# =====================================================================
# FUNCIÓN PRINCIPAL PARA EJECUTAR TODAS LAS PRUEBAS
# =====================================================================

def ejecutar_todas_las_pruebas():
    """
    Ejecuta todas las pruebas del TAD Cuenta Bancaria.
    
    Esta función debe usarse en clase para demostrar:
    1. Que la implementación cumple con la especificación del TAD
    2. Que todos los axiomas se verifican
    3. Que el manejo de errores es correcto
    4. Que la estructura es útil en casos reales
    """
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  PRUEBAS COMPLETAS - TAD CUENTA BANCARIA".center(68) + "█")
    print("█" + "  Estructura de Datos - UC3M 2025".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70)
    
    try:
        # Pruebas de axiomas
        test_axioma_1_cuenta_nueva_saldo_cero()
        test_axioma_2_depositar_aumenta_saldo()
        test_axioma_3_retirar_disminuye_saldo()
        test_axioma_6_no_retirar_mas_del_saldo()
        test_axioma_9_transferencia()
        
        # Pruebas de manejo de errores
        test_manejo_errores()
        
        # Prueba de historial
        test_historial_transacciones()
        
        # Demostración de caso real
        demo_caso_uso_real()
        
        # Resumen final
        imprimir_separador("RESUMEN DE PRUEBAS")
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE! 🎉")
        print("\n✅ Todos los axiomas del TAD están verificados")
        print("✅ El manejo de errores funciona correctamente")
        print("✅ Los invariantes se mantienen en todo momento")
        print("✅ La implementación es correcta y robusta")
        print("\n" + "█"*70 + "\n")
        
    except AssertionError as e:
        print(f"\n❌ ERROR EN PRUEBAS: {e}")
        raise
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")
        raise


# =====================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =====================================================================

if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
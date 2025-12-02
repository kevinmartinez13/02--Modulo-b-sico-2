import random
import datetime
from decimal import Decimal, ROUND_HALF_UP

class CuentaBancaria:
    _contador_cuentas = 0  # Contador para generar números únicos

    def __init__(self, titular, saldo_inicial=0, tipo_cuenta="AHORROS"):
        if not isinstance(titular, str) or len(titular.strip()) == 0:
            raise ValueError("El titular debe ser un texto no vacío")
        if not isinstance(saldo_inicial, (int, float)) or saldo_inicial < 0:
            raise ValueError("El saldo inicial debe ser un número positivo")

        self.titular = titular.strip().title()
        self.tipo_cuenta = tipo_cuenta.upper()
        self.fecha_apertura = datetime.datetime.now()
        self.activa = True

        self.__saldo = Decimal(str(saldo_inicial)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.__numero_cuenta = self.__generar_numero_cuenta()
        self.__historial = []
        self.__pin = None

        CuentaBancaria._contador_cuentas += 1

        if saldo_inicial > 0:
            self.__registrar_transaccion("DEPOSITO_INICIAL", saldo_inicial, "Apertura de cuenta")

    def __generar_numero_cuenta(self):
        prefijo = "ACC"
        numero = str(random.randint(100000, 999999))
        sufijo = str(CuentaBancaria._contador_cuentas).zfill(4)
        return f"{prefijo}-{numero}-{sufijo}"

    def __validar_monto(self, monto):
        if not isinstance(monto, (int, float, Decimal)):
            raise TypeError("El monto debe ser un número")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if monto > 1000000:
            raise ValueError("El monto excede el límite de transacción ($1,000,000)")
        return Decimal(str(monto)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def __validar_cuenta_activa(self):
        if not self.activa:
            raise RuntimeError("La cuenta está inactiva. No se pueden realizar transacciones.")

    def __registrar_transaccion(self, tipo, monto, descripcion=""):
        transaccion = {
            'fecha': datetime.datetime.now(),
            'tipo': tipo,
            'monto': float(monto),
            'saldo_anterior': float(self.__saldo) if tipo != "DEPOSITO_INICIAL" else 0,
            'saldo_nuevo': float(self.__saldo) if tipo != "DEPOSITO_INICIAL" else float(monto),
            'descripcion': descripcion,
            'id_transaccion': len(self.__historial) + 1
        }
        self.__historial.append(transaccion)

    def depositar(self, monto, descripcion="Depósito"):
        self.__validar_cuenta_activa()
        monto_validado = self.__validar_monto(monto)

        saldo_anterior = self.__saldo
        self.__saldo += monto_validado
        self.__registrar_transaccion("DEPOSITO", monto_validado, descripcion)
        return {
            'exitoso': True,
            'tipo': 'DEPOSITO',
            'monto': float(monto_validado),
            'saldo_anterior': float(saldo_anterior),
            'saldo_nuevo': float(self.__saldo),
            'fecha': datetime.datetime.now(),
            'mensaje': f"Depósito exitoso. Nuevo saldo: ${self.__saldo:,.2f}"
        }

    def retirar(self, monto, descripcion="Retiro"):
        self.__validar_cuenta_activa()
        monto_validado = self.__validar_monto(monto)

        if monto_validado > self.__saldo:
            raise ValueError(f"Fondos insuficientes. Saldo disponible: ${self.__saldo:,.2f}")
        saldo_anterior = self.__saldo
        self.__saldo -= monto_validado
        self.__registrar_transaccion("RETIRO", monto_validado, descripcion)
        return {
            'exitoso': True,
            'tipo': 'RETIRO',
            'monto': float(monto_validado),
            'saldo_anterior': float(saldo_anterior),
            'saldo_nuevo': float(self.__saldo),
            'fecha': datetime.datetime.now(),
            'mensaje': f"Retiro exitoso. Nuevo saldo: ${self.__saldo:,.2f}"
        }

# Ejemplo de uso
if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Luis", 500)
    print(cuenta1.depositar(200))
    print(cuenta1.retirar(100))

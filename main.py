class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def calcular_intereses(self):
        if self.saldo < 10000:
            self.saldo *= 1.03
        elif self.saldo < 1000000:
            self.saldo *= 1.04
        else:
            self.saldo *= 1.06
        return self.saldo

    def calificacion_literal(self):
        if self.saldo < 10000:
            return "D"
        elif self.saldo < 1000000:
            return "C"
        elif self.saldo < 10000000:
            return "B"
        else:
            return "A"


# Ejemplo de uso
cuenta = CuentaBancaria(50000)
nuevo_saldo = cuenta.calcular_intereses()
calificacion = cuenta.calificacion_literal()

print(f"Nuevo Saldo: {nuevo_saldo:.2f}")
print(f"Calificación Literal: {calificacion}")

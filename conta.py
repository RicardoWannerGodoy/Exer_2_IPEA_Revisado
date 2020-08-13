class Conta:

    def __init__(self, id):
        self.id = id
        self.saldo = 0

    def deposito(self, quantia):
        if quantia < 0:
            print("Impossivel depositar valor negativo!")
        else:
            self.saldo += quantia

    def retirada(self, quantia):
        if quantia > self.saldo:
            print(f"Valor indisponivel na conta. Saldo atual é: {self.saldo}")
            return 0
        self.saldo -= quantia
        return quantia
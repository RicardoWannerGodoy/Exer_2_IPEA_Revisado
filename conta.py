# Essa "class Conta" tem as funções "deposito" e a "retirada":
class Conta:

    def __init__(self, idconta):
        self.idconta = idconta
        self.saldo = 0

    # Função criada para a entrada das variáveis da "class Conta".

    def deposito(self, quantia):
        if quantia < 0:
            print('Senhor(a) usuário(a), não é possível depositar valor negativo!')
        else:
            self.saldo += quantia

    # Função criada para a entrada dos valores das contas.

    def retirada(self, quantia):
        if quantia > self.saldo:
            print(f'Senhor(a) usuário(a) valor indisponivel na conta. Seu saldo atual é: {self.saldo}')
            return 0
        self.saldo -= quantia
        return quantia

    # Função criada para a saída dos valores das contas.

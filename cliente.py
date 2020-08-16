from Exer_2_Python_RWG.conta import Conta
# Importando nesse momento a "class Conta" para utilizar aqui na "class Cliente".


# Essa "class Cliente" tem somente a entrada das variáveis dos clientes:
class Cliente:
    def __init__(self, idcliente, nmcliente, dtcliente):
        self.idcliente = idcliente
        self.nmcliente = nmcliente
        self.dtcliente = dtcliente
        self.cccliente = Conta(0)
        self.experiencia = 0

    # Função cria as variáveis dos clientes.

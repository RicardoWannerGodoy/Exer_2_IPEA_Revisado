from Exer_2_Python_RWG.conta import Conta

class Cliente:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.conta = Conta(0)
        self.experiencia = 0

# Sugiro que depois o random seja colocado lá na simulation.py e você já traga o número de cada loja
import random

from Exer_2_Python_RWG.conta import Conta

class Loja:
    def __init__(self, id):
        self.id = id
        self.conta = Conta(0)
        self.custo_produto = round(random.random() * 100, 2)
        self.experiencia = random.randint(1, 5)
        self.capacidade = random.randint(5, 200)

    def visita_cliente(self):
        if self.capacidade > 0:
            self.capacidade -= 1
            return True
        else:
            print("Limite de visitas alcançado.")
            return False


    def oferece_experiencia(self):
        return self.experiencia

    def __repr__(self):
        return self.id



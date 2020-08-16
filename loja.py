import random
# Importando o "método random" para as execuções randômicas das funções da "class Loja".

# Importando nesse momento a "class Conta" para utilizar aqui na "class Loja".
from Exer_2_Python_RWG.conta import Conta


# Essa "class Loja" tem as funções "visita_cliente" e a "oferece_experiencia":
class Loja:
    def __init__(self, idloja, nmloja):
        self.idloja = idloja
        self.nmloja = nmloja
        self.ccloja = Conta(0)
        self.custo_produto = round(random.random() * 100, 2)
        self.experiencia = random.randint(1, 5)
        self.capacidade = random.randint(5, 200)

    # Função criada para a entrada das variáveis e listas.

    def visita_cliente(self):
        if self.capacidade > 0:
            self.capacidade -= 1
            return True
        else:
            print('Atingimento do limite de visitas máxima da loja.')
            return False

    # Função criada para a entrada capacidade que as loas podem receber seus clientes.

    def oferece_experiencia(self):
        return self.experiencia

    # Função criada para destinar a experiencia do clienete quando da sua visita a loja.

    def __repr__(self):
        return self.idloja

    # Função criada para retornar o "id" quando ele for desconhecido.

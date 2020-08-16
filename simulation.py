import random
# Importando o "método random" para as execuções randômicas das funções da "class Simulacao".

# Importando nesse momento as "class Loja" e "class Cliente" para utilização aqui na "class Simulacao".
from Exer_2_Python_RWG.loja import Loja
from Exer_2_Python_RWG.cliente import Cliente


# Essa "class Simulacao" tem as funções "salvar_arquivo_dados", "criar_lojas", "criar_clientes"
# "media_experiencia", "deposito_inicial" e a "run_model":
class Simulacao:
    def __init__(self):
        self.lojas = []
        self.criar_lojas()
        self.clientes = []
        self.criar_clientes()
        self.deposito_inicial()

    # Função criada para a entrada das variáveis na "class Simulacao".

    def salvar_arquivo_dados(self, exp_media):
        clientes = []
        lojas = []
        for item in self.clientes:
            item.cccliente = item.cccliente.__dict__
            clientes.append(str(item.__dict__) + "\n")
        for item in self.lojas:
            item.ccloja = item.ccloja.__dict__
            lojas.append(str(item.__dict__) + "\n")
        with open('arquivo.txt', 'w') as file:
            file.write('\nInformações dos clientes:')
            file.writelines(clientes)
            file.write('\nInformações das lojas:')
            file.writelines(lojas)
            file.write('\nSenhor(a) usuário(a) a média de experiência dos clientes que visitaram as lojas é:')
            file.write(str(exp_media))

    # Função criada para salvar em arquivo .txt o conteúdo de saída que o programa executa.

    def criar_lojas(self):
        x = int(input('Senhor(a) usuário(a) quantas lojas serão criadas?\n'))
        for idloja in range(x):
            nmloja = input(f'Por favor, usuário(a) digite o nome da loja {idloja}:\n')
            self.lojas.append(Loja(idloja, nmloja))

    # Função que cria uma lista de lojas com o "input" do usuáriodo programa.

    def criar_clientes(self):
        x = int(input('Senhor(a) usuário(a) quantos clientes serão criados?\n'))
        for idcliente in range(x):
            nmcliente = input(f'Por favor, usuário(a) digite o nome do cliente {idcliente}:\n')
            dtcliente = input(f'Por favor, usuário(a) digite a idade do cliente {idcliente}:\n')
            self.clientes.append(Cliente(idcliente, nmcliente, dtcliente))

    # Função que cria uma lista de clientes com o "input" do usuáriodo programa.

    def media_experiencia(self):
        experiencia_somada = 0
        for item in self.clientes:
            experiencia_somada += item.experiencia
        return experiencia_somada / len(self.clientes)

    # Função que calcula a média das experiências dos clientes com a loja visitada.

    def deposito_inicial(self):
        for item in self.clientes:
            item.cccliente.deposito(random.randint(100, 200))

    # Função que faz um deposito randômico na conta dos clientes em um range de valor de "100 a 200".

    def run_model(self):
        for item in self.clientes:
            # Nesse momento o programa escolhe uma loja aleatória.
            loja_escolhida = random.choice(self.lojas)
            # Nesse momento o programa verifica a capacidade da loja.
            posso_ir = loja_escolhida.visita_cliente()
            if posso_ir:
                loja_escolhida.ccloja.deposito(item.cccliente.retirada(loja_escolhida.custo_produto))
                item.experiencia += loja_escolhida.experiencia
        return self.media_experiencia()
    # Função realiza duas ações: uma da escolha da loja pelo cliente e a outra um deposito na conta da loja
    # escolhida randômicamente pelo programa.


if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()
    minha_sim.salvar_arquivo_dados(media)

    # Aqui o progama chama a "class Simulacao" roda a média da experiência do cliente e a função
    # salvar_arquivo_dados, que irá criar um arquivo .txt com as informações criadas pelo programa.

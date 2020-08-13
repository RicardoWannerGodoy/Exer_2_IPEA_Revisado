import random
from Exer_2_Python_RWG.loja import Loja
from Exer_2_Python_RWG.cliente import Cliente


class Simulacao:
    def __init__(self):
        self.lojas = []
        self.criar_lojas()
        self.clientes = []
        self.criar_clientes()
        # 2. Popule essa lista, chamando a função dessa própria classe chamada criar_lojas, utilizando self.função()
        # **** Lembrando para chamar uma FUNÇÃO DE DENTRO DA PROPRIA CLASSE, USE self.funcao1()
        self.deposito_inicial()

    def salvar_arquivo_dados(self, media):

        clientes=[]
        lojas = []
        for item in self.clientes:
            item.conta = item.conta.__dict__
            clientes.append(str(item.__dict__)+"\n")
        for item in self.lojas:
            item.conta = item.conta.__dict__
            lojas.append(str(item.__dict__)+"\n")
        with open('arquivo.txt', 'w') as file:
            file.write("Clientes: ")
            file.writelines(clientes)
            file.write("\nLojas: ")
            file.writelines(lojas)
            file.write("\nMedia de experiencia: ")
            file.write(str(media))


    def criar_lojas(self):
        x=int(input("Quantas lojas queres criar? "))
        for id in range(x):
            name = input(f"Digite o nome da loja {id}: ")
            self.lojas.append(Loja(name))

    def criar_clientes(self):
        x = int(input("Quantos clientes queres criar? "))
        for id in range(x):
            name = input(f"Digite o nome do Cliente {id}: ")
            idade = input("Digite idade do Cliente: ")
            self.clientes.append(Cliente(id,name,idade))


    def media_experiencia(self):
        experiencia_somada = 0
        for item in self.clientes:
            experiencia_somada += item.experiencia
        return experiencia_somada / len(self.clientes)

    def deposito_inicial(self):
        for item in self.clientes:
            item.conta.deposito(random.randint(100, 200))

    def run_model(self):
        # Decidir se a visita a loja ocorre três vezes.

        for item in self.clientes:
            # Escolhe uma loja aleatoria
            loja_escolhida = random.choice(self.lojas)
            # Verificar a capacidade
            posso_ir = loja_escolhida.visita_cliente()
            if posso_ir:
                loja_escolhida.conta.deposito(item.conta.retirada(loja_escolhida.custo_produto))
                item.experiencia +=loja_escolhida.experiencia

        return self.media_experiencia()


if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()
    minha_sim.salvar_arquivo_dados(media)
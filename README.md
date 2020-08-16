### Montando um modelo baseado em agentes (ABM) 

Mestrado Profissional em Políticas Públicas e Desenvolvimento.<br/>
Turma 4 MPPPD, 16 julho 2020 01:45

#### Python para Modelagem Baseada em Agentes

#### Autores:
Prof. Bernardo Alves Furtado e<br/>
Aluno Ricardo Godoy

#### Pergunta da Pesquisa
A satisfação dos clientes depende do atendimento oferecido pela loja visitada?

#### Hipótese: 
Verificar qual é a média dessa satisfação dos clientes.

#### Agentes:
Consumidores (localização (trabalho/moradia), preferências (+perto, +barato, intensidade de uso)
Postos de combustíveis (localização fixa, (decidem) precificação, lucro)

#### Ambiente
Preço de custo combustível (variável)

#### Comportamentos
Escolha de abastecimento (localização, preço corrente)
Decisão sobre margens de lucros (custo, lucro)

#### Resposta do modelo
Preços médios -- Eles variam junto com a variação do preço de custo
Correlação preços de custo
Comportamento margens de lucro
Calibração e validação
Buscar dados de mercado
How to run

## Memorial do Programa:

##### menu.py

````from Exer_2_Python_RWG import simulation````

Importando nesse momento a "class Simulacao" para utilizar aqui na função "main".

Essa função "main" tem o obetivo de chamar e executar todas as outras "class" do programa:

def main():

Aqui inicia o programa, esse foi limitado em 5 passos:

    print('###########################################################################################')
    print('########################## "Informações Prelimirares do Programa" #########################')
    print('###########################################################################################\n')

    nome = input('Usuário(a) qual é o seu nome? =>:\n')

Aqui o usuário do programa é chamado para interagir com o programa digitando o seu nome.

    passos = 6
    while passos > 5:
        print(f'{nome}, lembramos que o programa tem um limite de até 5 passos no máximo:\n')
        passos = int(input(f'Por favor, {nome} digite a quantidade de passos que o programa deverá rodar:\n'))
        if passos > 5:
            print(f'{nome}, digite novamente, pois o limite máximo de passos é até 5.\n')

Nessa parte o usuário poderá digitar a quantidade de vezes que o programa vai rodar:

    todas_as_medias = 0
    for i in range(passos):
        sim = simulation.Simulacao()
        todas_as_medias += sim.run_model()
        if i == passos - 1:
            sim.salvar_arquivo_dados(sim.media_experiencia())

Nessa parte do programa o "menu" chama a "class Simulacao".

    print()
    print(f'A média da experiência dos clientes com {passos} passo(s) é de =>: {todas_as_medias/passos}\n')

O programa agora imprime a quantidade de passos e a média das experiências atribuidas para os clientes.

    print('###########################################################################################')
    print('#################################### "Fim do Programa" ####################################')
    print('###########################################################################################\n')

Nesse momento o programa é finalizado e o arquivo de saída foi gerado na pasta onde o programa está rodando.

````
if __name__ == '__main__':
    main()
````

##### simulation.py

````import random````

Importando o "método random" para as execuções randômicas das funções da "class Simulacao".

Importando nesse momento as "class Loja" e "class Cliente" para utilização aqui na "class Simulacao".

````from Exer_2_Python_RWG.loja import Loja````

````from Exer_2_Python_RWG.cliente import Cliente````


Essa "class Simulacao" tem as funções "salvar_arquivo_dados", "criar_lojas", "criar_clientes"
"media_experiencia", "deposito_inicial" e a "run_model":

class Simulacao:

    def __init__(self):
        self.lojas = []
        self.criar_lojas()
        self.clientes = []
        self.criar_clientes()
        self.deposito_inicial()

Função criada para a entrada das variáveis na "class Simulacao".

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

Função criada para salvar em arquivo .txt o conteúdo de saída que o programa executa.

    def criar_lojas(self):
        x = int(input('Senhor(a) usuário(a) quantas lojas serão criadas?\n'))
        for idloja in range(x):
            nmloja = input(f'Por favor, usuário(a) digite o nome da loja {idloja}:\n')
            self.lojas.append(Loja(idloja, nmloja))

Função que cria uma lista de lojas com o "input" do usuáriodo programa.

    def criar_clientes(self):
        x = int(input('Senhor(a) usuário(a) quantos clientes serão criados?\n'))
        for idcliente in range(x):
            nmcliente = input(f'Por favor, usuário(a) digite o nome do cliente {idcliente}:\n')
            dtcliente = input(f'Por favor, usuário(a) digite a idade do cliente {idcliente}:\n')
            self.clientes.append(Cliente(idcliente, nmcliente, dtcliente))

Função que cria uma lista de clientes com o "input" do usuáriodo programa.

    def media_experiencia(self):
        experiencia_somada = 0
        for item in self.clientes:
            experiencia_somada += item.experiencia
        return experiencia_somada / len(self.clientes)

Função que calcula a média das experiências dos clientes com a loja visitada.

    def deposito_inicial(self):
        for item in self.clientes:
            item.cccliente.deposito(random.randint(100, 200))


Função que faz um deposito randômico na conta dos clientes em um range de valor de "100 a 200".

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
        
Função realiza duas ações: uma da escolha da loja pelo cliente e a outra um deposito na conta da loja
escolhida randômicamente pelo programa.

````
if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()
    minha_sim.salvar_arquivo_dados(media)
````

Aqui o progama chama a "class Simulacao" roda a média da experiência do cliente e a função
salvar_arquivo_dados, que irá criar um arquivo .txt com as informações criadas pelo programa.

##### conta.py

Essa "class Conta" tem as funções "deposito" e a "retirada":

class Conta:

    def __init__(self, idconta):
        self.idconta = idconta
        self.saldo = 0

Função criada para a entrada das variáveis da "class Conta".

    def deposito(self, quantia):
        if quantia < 0:
            print('Senhor(a) usuário(a), não é possível depositar valor negativo!')
        else:
            self.saldo += quantia

Função criada para a entrada dos valores das contas.

    def retirada(self, quantia):
        if quantia > self.saldo:
            print(f'Senhor(a) usuário(a) valor indisponivel na conta. Seu saldo atual é: {self.saldo}')
            return 0
        self.saldo -= quantia
        return quantia

Função criada para a saída dos valores das contas.

##### loja.py

````import random````

Importando o "método random" para as execuções randômicas das funções da "class Loja".

Importando nesse momento a "class Conta" para utilizar aqui na "class Loja".

````from Exer_2_Python_RWG.conta import Conta````


Essa "class Loja" tem as funções "visita_cliente" e a "oferece_experiencia":

###### class Loja:
````
    def __init__(self, idloja, nmloja):
        self.idloja = idloja
        self.nmloja = nmloja
        self.ccloja = Conta(0)
        self.custo_produto = round(random.random() * 100, 2)
        self.experiencia = random.randint(1, 5)
        self.capacidade = random.randint(5, 200)
````

Função criada para a entrada das variáveis e listas.
    
````
    def visita_cliente(self):
        if self.capacidade > 0:
            self.capacidade -= 1
            return True
        else:
            print('Atingimento do limite de visitas máxima da loja.')
            return False
````
Função criada para a entrada capacidade que as loas podem receber seus clientes.
    
```
    def oferece_experiencia(self):
        return self.experiencia
```
Função criada para destinar a experiencia do clienete quando da sua visita a loja.

``` 
    def __repr__(self):
        return self.idloja
```
Função criada para retornar o "id" quando ele for desconhecido.

##### cliente.py
Importando nesse momento a "class Conta" para utilizar aqui na "class Cliente".<br/>

```from Exer_2_Python_RWG.conta import Conta```

Essa "class Cliente" tem somente a entrada das variáveis dos clientes:
###### class Cliente:
```
    def __init__(self, idcliente, nmcliente, dtcliente):
        self.idcliente = idcliente
        self.nmcliente = nmcliente
        self.dtcliente = dtcliente
        self.cccliente = Conta(0)
        self.experiencia = 0
```
Função cria as variáveis dos clientes.


##### arquivo.txt

Informações dos clientes:<br/>
````
{'idcliente': 0, 'nmcliente': 'rt', 'dtcliente': '67', 'cccliente': {'idconta': 0, 'saldo': 88.25}, 'experiencia': 5}<br/>
{'idcliente': 1, 'nmcliente': 'Lr', 'dtcliente': '32', 'cccliente': {'idconta': 0, 'saldo': 152.25}, 'experiencia': 5}<br/>
````
Informações das lojas:<br/>
````
{'idloja': 0, 'nmloja': 'Lu', 'ccloja': {'idconta': 0, 'saldo': 83.5}, 'custo_produto': 41.75, 'experiencia': 5, 'capacidade': 79}<br/>
````
Senhor(a) usuário(a) a média de experiência dos clientes que visitaram as lojas é:5.0
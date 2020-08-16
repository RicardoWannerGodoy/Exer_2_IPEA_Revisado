from Exer_2_Python_RWG import simulation


# Importando nesse momento a "class Simulacao" para utilizar aqui na função "main".


# Essa função "main" tem o obetivo de chamar e executar todas as outras "class" do programa:
def main():
    # Aqui inicia o programa, esse foi limitado em 5 passos:

    print('###########################################################################################')
    print('########################## "Informações Prelimirares do Programa" #########################')
    print('###########################################################################################\n')

    nome = input('Usuário(a) qual é o seu nome? =>:\n')
    # Aqui o usuário do programa é chamado para interagir com o programa digitando o seu nome.

    passos = 6
    while passos > 5:
        print(f'{nome}, lembramos que o programa tem um limite de até 5 passos no máximo:\n')
        passos = int(input(f'Por favor, {nome} digite a quantidade de passos que o programa deverá rodar:\n'))
        if passos > 5:
            print(f'{nome}, digite novamente, pois o limite máximo de passos é até 5.\n')
    # Nessa parte o usuário poderá digitar a quantidade de vezes que o programa vai rodar:

    todas_as_medias = 0
    for i in range(passos):
        sim = simulation.Simulacao()
        todas_as_medias += sim.run_model()
        if i == passos - 1:
            sim.salvar_arquivo_dados(sim.media_experiencia())
    # Nessa parte do programa o "menu" chama a "class Simulacao".

    print()
    print(f'A média da experiência dos clientes com {passos} passo(s) é de =>: {todas_as_medias/passos}\n')
    # O programa agora imprime a quantidade de passos e a média das experiências atribuidas para os clientes.

    print('###########################################################################################')
    print('#################################### "Fim do Programa" ####################################')
    print('###########################################################################################\n')
    # Nesse momento o programa é finalizado e o arquivo de saída foi gerado na pasta onde o programa está rodando.


if __name__ == '__main__':
    main()

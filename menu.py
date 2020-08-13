from Exer_2_Python_RWG import simulation

if __name__ == '__main__':
    passos = 6
    while passos>5:
        passos = int(input("Quantos passos vc gostaria de executar: "))
        if passos>5:
            print("Digite novamente, limite máximo de passos é 5.")

    todas_as_medias = 0
    for i in range(passos):
        sim = simulation.Simulacao()
        todas_as_medias += sim.run_model()
        if i == passos-1:
            sim.salvar_arquivo_dados(sim.media_experiencia())
    print(f'A média da experiencia de simular {passos} vezes é: {todas_as_medias/passos}')

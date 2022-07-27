def main():
    """
    No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion,
    Sheldon e Raj discutem qual dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. A
    sugestão de Raj para a resolução do impasse é uma disputa de Pedra-Papel-Tesoura. Contudo, Sheldon
    argumenta que, se as partes envolvidas se conhecem, entre 75% e 80% das disputas de Pedra-Papel-Tesoura
    terminam empatadas, e então sugere o Pedra-Papel-Tesoura-Lagarto-Spock.

    As regras do jogo proposto são:

    a tesoura corta o papel;
    o papel embrulha a pedra;
    a pedra esmaga o lagarto;
    o lagarto envenena Spock;
    Spock destrói a tesoura;
    a tesoura decapita o lagarto;
    o lagarto come o papel;
    o papel contesta Spock;
    Spock vaporiza a pedra;
    a pedra quebra a tesoura.

    Embora a situação não se resolva no episódio (ambos escolhem Spock, resultando em um empate), não
    é difıcil deduzir o que aconteceria se a disputa continuasse. Caso Sheldon vencesse, ele se
    deleitaria com a vitória, exclamando "Bazinga!"; caso Raj vencesse, ele concluiria que
    "Raj trapaceou!"; caso o resultado fosse empate, ele exigiria nova partida: "De novo!".
    Conhecidas as personagens do jogo escolhido por ambos, faça um programa que imprima a provável
    reação de Sheldon.
    """
    n = 1
    t = int(input())
    while n <= t:
        escolhas = input().split(' ')
        if escolhas[0] == escolhas[1]:
            print(f'Caso #{n}: De novo!')
        elif escolhas[0] == 'pedra' and escolhas[1] == 'papel' or escolhas[0] == 'pedra' and \
                escolhas[1] == 'Spock':
            print(f'Caso #{n}: Raj trapaceou!')
        elif escolhas[0] == 'papel' and escolhas[1] == 'tesoura' or escolhas[0] == 'papel' and \
                escolhas[1] == 'lagarto':
            print(f'Caso #{n}: Raj trapaceou!')
        elif escolhas[0] == 'tesoura' and escolhas[1] == 'pedra' or escolhas[0] == 'tesoura' and \
                escolhas[1] == 'Spock':
            print(f'Caso #{n}: Raj trapaceou!')
        elif escolhas[0] == 'lagarto' and escolhas[1] == 'pedra' or escolhas[0] == 'lagarto' and \
                escolhas[1] == 'tesoura':
            print(f'Caso #{n}: Raj trapaceou!')
        elif escolhas[0] == 'Spock' and escolhas[1] == 'papel' or escolhas[0] == 'Spock' and \
                escolhas[1] == 'lagarto':
            print(f'Caso #{n}: Raj trapaceou!')
        else:
            print(f'Caso #{n}: Bazinga!')
        n += 1


if __name__ == '__main__':
    main()

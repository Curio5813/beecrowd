def main():
    """
     A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do
     resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo
     Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta.
     Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados
     pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

    - Quantos GRENAIS fizeram parte da estatística.
    - O número de vitórias do Inter.
    - O número de vitórias do Grêmio.
    - O número de Empates.
    - Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso
    termine empatado).
    """
    cont_grenais, cont_gremio, cont_inter, cont_empate = 0, 0, 0, 0
    continuar = 1
    while continuar == 1:
        inter, gremio = input().split(' ')
        inter, gremio = int(inter), int(gremio)
        cont_grenais += 1
        if gremio > inter:
            cont_gremio += 1
        elif inter > gremio:
            cont_inter += 1
        elif gremio == inter:
            cont_empate += 1
        print('Novo grenal (1-sim 2-nao)')
        continuar = int(input())
    print(f'{cont_grenais} grenais\n'
          f'Inter:{cont_inter}\n'
          f'Gremio:{cont_gremio}\n'
          f'Empates:{cont_empate}')
    if cont_inter > cont_gremio:
        print('Inter venceu mais')
    elif cont_gremio > cont_inter:
        print('Gremio venceu mais')
    elif cont_inter == cont_gremio:
        print('Nao houve vencedor')


if __name__ == '__maina__':
    main()

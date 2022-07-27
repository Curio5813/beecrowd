def main():
    """
    Iu-di-oh! é um jogo de cartas que virou uma verdadeira febre entre os jovens! Todo
    jogador de Iu-di-oh! tem seu próprio baralho, contendo várias cartas do jogo. Cada
    carta contém N atributos (como força, velocidade, inteligência, etc.). Os atributos
    são numerados de 1 a N e são dados por inteiros positivos.

    Uma partida de Iu-di-oh! é sempre jogada por dois jogadores. Ao iniciar a partida,
    cada jogador escolhe exatamente uma carta de seu baralho. Após as escolhas, um atributo
    é sorteado. Vence o jogador cujo atributo sorteado em sua carta escolhida é maior que
    na carta escolhida pelo adversário. Caso os atributos sejam iguais, a partida empata.

    Marcos e Leonardo estão na grande final do campeonato brasileiro de Iu-di-oh!, cujo
    prêmio é um Dainavision (que é quase um Plaisteition 2!). Dados os baralhos de ambos,
    a carta escolhida por cada um e o atributo sorteado, determine o vencedor!

    Entrada
    A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro
    N (1 ≤ N ≤ 100), o número de atributos de cada carta. A segunda linha contém dois inteiros
    M e L (1 ≤ M, L ≤ 100), o número de cartas no baralho de Marcos e de Leonardo,
    respectivamente.

    As próximas M linhas descrevem o baralho de Marcos. As cartas são numeradas de 1 a M,
    e a i-ésima linha descreve a i-ésima carta. Cada linha contém N inteiros
    ai,1,ai,2,..., ai,N (1 ≤ ai,j ≤ 109). O inteiro ai,j indica o atributo j da carta i.
    As próximas L linhas descrevem o baralho de Leonardo. As cartas são numeradas de 1 e L
    e são descritas de maneira análoga.

    A próxima linha contém dois inteiros CM e CL (1 ≤ CM ≤ M, 1 ≤ CL ≤ L), as cartas
    escolhidas por Marcos e Leonardo, respectivamente. Por fim, a última linha contém um
    inteiro A (1 ≤ A ≤ N) indicando o atributo sorteado.

    A entrada termina com fim-de-arquivo (EOF).

    Saída
    Para cada caso de teste, imprima uma linha contendo “Marcos” se Marcos é o vencedor,
    “Leonardo” se Leonardo é o vencedor, ou “Empate” caso contrário (sem aspas).
    """
    while True:
        cartas_m, cartas_l = [], []
        try:
            n = int(input())
            ma, leo = input().split()
            ma, leo = int(ma), int(leo)
            for k in range(ma):
                marcos = [int(x) for x in input().split()]
                cartas_m.append(marcos)
            for k in range(leo):
                leonardo = [int(x) for x in input().split()]
                cartas_l.append(leonardo)
            c_m, c_l = input().split()
            c_m, c_l = int(c_m), int(c_l)
            choice_m = cartas_m[c_m - 1]
            choice_l = cartas_l[c_l - 1]
            att = int(input())
        except EOFError:
            break
        else:
            if choice_m[att - 1] > choice_l[att - 1]:
                print('Marcos')
            elif choice_m[att - 1] < choice_l[att - 1]:
                print('Leonardo')
            else:
                print('Empate')


if __name__ == '__main__':
    main()

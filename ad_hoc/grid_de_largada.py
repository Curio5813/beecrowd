from time import sleep


def grid_de_largada():
    """
    Na Nlogônia, vai ser realizada a sensacional final mundial da fórmula 17.
    Os competidores se alinham na largada e disputam a corrida. Você vai ter
    acesso aos grids de largada e de chegada. A questão é determinar o número
    mínimo de ultrapassagens que foram efetuadas durante a competição.

    Entrada
    Cada caso de teste utiliza três linhas. A primeira linha de um caso de teste
    contém um inteiro N (2 ≤ N ≤ 24) indicando o número de competidores. Cada
    competidor é identificado com um número de 1 a N. A segunda linha de cada
    caso tem os N competidores, em ordem do grid de largada. A terceira linha de
    cada caso tem os mesmos competidores, porém agora na ordem de chegada.

    Saída
    Para cada caso de teste imprima uma linha contendo um único número inteiro,
    que indica o número mínimo de ultrapassagens necessárias para se chegar do
    grid de largada ao grid de chegada.
    :return:
    """
    while True:
        try:
            ultrapassagem = 0
            n = int(input())
            largada = list(map(int, input().split(" ")))
            chegada = list(map(int, input().split(" ")))
            for i in range(len(chegada) - 1, -1, -1):
                saida = largada.index(largada[i])
                final = chegada.index(largada[i])
                print(f"{i}: {final} {saida}")
                sleep(1)
                if saida > final:
                    ultrapassagem += saida - final
                    print(ultrapassagem)
                    sleep(1)
                elif saida <= final:
                    k = i
                    while k >= 0:
                        if final < chegada.index(largada[k - 1]):
                            ultrapassagem += 1
                            print(ultrapassagem)
                            sleep(1)
                        k -= 1
            print(ultrapassagem)
        except EOFError:
            break


grid_de_largada()

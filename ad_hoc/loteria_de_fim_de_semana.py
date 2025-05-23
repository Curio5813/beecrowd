from collections import Counter


def loteria_de_fim_de_semana():
    """
    Algumas pessoas são contra loterias por motivos morais, alguns
    governos as proíbem, mas com a criação da internet essa popular
    forma de aposta, que teve início na China e ajudou a financiar
    a Grande Muralha, está prosperando.

    Mas as chances de se ganhar em uma loteria nacional são pequenas,
    por conta disso seus colegas de classe decidiram organizar uma loteria
    particular, cujo sorteio se realiza toda sexta-feira. A loteria é
    baseada em um estilo popular: um estudante que quer apostar escolhe
    C números distintos entre 1 e K e paga US$ 1.00 (note que as loterias
    tradicionais como a US National Lotto usam C=6 e K=49). Na sexta-feira
    durante o almoço, C números (também de 1 a K) são sorteados. O estudante
    que acertar a maior quantidade de números sorteados recebe o montante
    coletado nas apostas. O montante é dividido no caso de empates e acumulado
    para a próxima semana se ninguém acertar qualquer um dos números sorteados.

    Alguns de seus colegas não acreditam nas leis da probabilidade e pediram para
    você para escrever um programa que determine os números que foram sorteados
    o menor número de vezes considerando todos os sorteios prévios, para que eles
    possam apostar nesses números.

    Entrada
    A entrada contém diversos casos de teste. A primeira linha de um caso de teste
    contém três inteiros N, C e K que indicam, respectivamente, o número de sorteios
    que já aconteceram (1 ≤ N ≤ 10000), quantos números compõem uma aposta (1 ≤ C ≤ 10)
    e o valor máximo que pode ser escolhido numa aposta (C < K ≤ 100). Cada uma das
    próximas N linhas contém C inteiros distintos Xi indicando os números sorteados
    em cada concurso prévio (1 ≤ Xi ≤ K, para 1 ≤ i ≤ C). O fim da entrada é indicado
    por N = C = K = 0.

    Saída
    Para cada caso de teste, seu programa deve escrever uma linha de saída, contendo o
    conjunto de números que foram sorteados o menor número de vezes. Este conjunto deve
    ser impresso como uma lista em ordem crescente. Deixe um espaço em branco entre dois
    números consecutivos na lista.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, c, k = entrada[0], entrada[1], entrada[2]
    while n != 0 and c != 0 and k != 0:
        sorteados, nao_sorteados = [], []
        for i in range(n):
            sorteio = list(map(int, input().strip().split(" ")))
            sorteados.extend(sorteio)
        numeros_sorteados = Counter(sorted(sorteados))
        for i in range(1, k + 1):
            if i not in sorteados:
                nao_sorteados.append(i)
        nao_sorteados.sort()
        if len(nao_sorteados) != 0:
            for i in range(0, len(nao_sorteados)):
                if i >= len(nao_sorteados) - 1:
                    print(nao_sorteados[i])
                    break
                print(nao_sorteados[i], end=" ")
        else:
            min_valor = min(numeros_sorteados.values())
            menores = [numero for numero, vezes in numeros_sorteados.items() if vezes == min_valor]
            print(*menores)
        entrada = list(map(int, input().strip().split(" ")))
        n, c, k = entrada[0], entrada[1], entrada[2]



loteria_de_fim_de_semana()

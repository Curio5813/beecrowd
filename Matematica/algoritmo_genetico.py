def algoritmo_genetico():
    """
    Algumas disciplinas de computação são muito teóricas e
    as vezes entediantes. Na tentativa de despertar o interesse
    dos alunos pelo conteúdo, o professor de Inteligência Artificial,
    sempre que possível, propõe um desafio envolvendo o conteúdo
    visto na aula do dia.

    A aula de hoje foi sobre algoritmos genéticos e procedimento
    explicado pelo professor foi o seguinte:

    A partir de 2 indivíduos (duas sequências de N bits: x0x1...xN-1)
    A e B, escolhe-se um posição de corte Y ( 1 ≤ Y < N) e então ocorre
    a recombinação (crossover), gerando 2 novos indivíduos: o primeiro
    é formado pelos bits x0...xY-1 do indivíduo A seguidos dos bits
    xY..xN-1 do indivíduo B, o segundo é formado pelos bits x0...xY-1
    do indivíduo B seguidos dos bits xY..xN-1 do indivíduo A.

    A imagem abaixo ilustra o resultado do crossover com Y = 5.

    ![](https://resources.beecrowd.com/gallery/images/contests/C_01.png)

    Após o crossover, cada bit dos novos indivíduos pode sofrer mutação (alterar
    seu valor) de acordo com uma probabilidade de mutação P especificada.

    O enunciado do desafio deixado pelo professor foi o seguinte:
    "Escreva um programa que receba 3 indivíduos, a posição do "corte" e a
    probabilidade de mutação. O programa deverá calcular qual a probabilidade
    de se obter o terceiro indivíduo como resultado de um crossover entre os
    dois primeiros."

    Entrada
    A primeira linha contém um inteiro T (1 ≤ T ≤ 50), o número de casos de teste.

    Cada caso de teste é composto por 5 linhas.

    A primeira linha contém o inteiro N (2 ≤ N ≤ 8), a quantidade de bits de cada
    indivíduo.

    A segunda linha contém um número inteiro Y (1 ≤ Y < N) seguido de um número
    de ponto flutuante P (0 ≤ P ≤ 1), a posição de corte e probabilidade de ocorrência
    de mutação, respectivamente.

    A terceira linha contém o primeiro indivíduo que será utilizado no crossover.

    A quarta linha contém o segundo indivíduo que será utilizado no crossover.

    A quinta linha contém o indivíduo que será comparado com os possíveis resultados
    do crossover.

    Saída
    Para cada caso de teste imprima uma única linha contendo a resposta com 7 dígitos
    após o ponto decimal.
    :return:
    """
    t = int(input())
    for i in range(t):
        n = int(input())
        entrada1 = list(input().strip().split(" "))
        y, p = int(entrada1[0]), float(entrada1[1])
        genes, crossovers, mutacao, mutacoes = [], [], '', []
        for j in range(3):
            gene = input()
            genes.append(gene)
        for j in range(0, len(genes)):
            if j == 0:
                crossover = genes[j][0:y] + genes[j + 1][y:]
                crossovers.append(crossover)
            if j == 1:
                crossover = genes[j][0:y] + genes[j - 1][y:]
                crossovers.append(crossover)
                break
        print(genes)
        print(crossovers)
        for j in range(0, len(crossovers)):
            for k in range(0, len(crossovers[j])):
                if crossovers[j][k] != genes[2][k]:
                    mutacao += genes[2][k]
                elif crossovers[j][k] == genes[2][k]:
                    mutacao += crossovers[j][k]
            mutacoes.append(mutacao)
            mutacao = ''
        print(mutacoes)
        for j in range(0, len(crossovers)):
            if j == 0:
                permutacao = mutacoes[j][0:y] + crossovers[j + 1][y:]
                crossovers.append(permutacao)
            if j == 1:
                permutacao = crossovers[j][0:y] + mutacoes[j - 1][y:]
                crossovers.append(permutacao)
                break
        crossovers.extend(crossovers)
        print(crossovers)
        qtd = crossovers.count(genes[2]) * p
        print(qtd)
        probabilidade = (1 - (qtd / (len(crossovers)))) * p
        print(f"{probabilidade:.7f}")


algoritmo_genetico()

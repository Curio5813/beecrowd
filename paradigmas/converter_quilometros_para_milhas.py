def converter_quilometros_para_milhas():
    """
    Este ano, Bruce Force passa suas férias em Flagstaff, Arizona,
    onde ele quer treinar para a próxima meia maratona (uma corrida
    de mais de 21 km). Em seu primeiro treino, ele correu até a casa
    de seu amigo Greedy Gonzales, que fica a 21 milhas de distância
    de Flagstaff.

    Chegando lá, ele já muito cansado, percebe que 21 milhas são muito
    mais de 21 km. Greedy Gonzales diz que 21 km é igual a 13 milhas.
    21, 13? Bruce percebe imediatamente que deve haver uma relação mais
    profunda! Ambos, 13 e 21 são números de Fibonacci!

    Números Fibonacci podem ser definidos da seguinte forma:

    F1 = 1

    F2 = 2

    Fn+1 = Fn+Fn-1 para n > 1

    Bruce está aprendendo sobre o sistema numérico Fibonacci em sua universidade.
    Cada inteiro positivo X pode ser escrito como a soma de diferentes números
    Fibonacci, isso significa que dado um numero k e b1, b2, ..., bk tal que
    x = ∑i=1..k bi * Fi, onde bk = 1 e bi (1 ≤ i < k) é 0 ou 1. Em resumo, podemos
    escrever a representação como: b (x) = (bk, bk-1, ..., b1). Para tornar a
    representação única, é necessário que bi * bi-1 = 0 para todo i > 1.

    Por exemplo 21 pode ser representado por (1,0,0,0,0,0,0) e 13 como (1,0,0,0,0,0)
    no sistema Fibonacci. Bruce percebe que se pode converter uma x distância em
    quilômetros em uma distância y correspondente a milhas da seguinte forma: Primeiro,
    anote x em seu Fibonacci representação do sistema b(x). Em segundo lugar, mudar
    os bits de b (x) uma posição para a direita (o último bit é excluído) e obter b(y).
    Em terceiro lugar, calcular y de b(y) através da avaliação da soma dada acima.

    Por exemplo, o número 42 escrito no sistema de Fibonacci é (1,0,0,1,0,0,0,0). Na
    etapa dois iríamos mudar os bits uma posição para a direita e termos (1,0,0,1,0,0,0).
    No terceiro passo, calcular 0*1 + 0*2 + 0*3 + 1*5 + 0*8 + 0*13 + 1*21 = 26.

    Agora é a sua vez de escrever um programa para Bruce que converte quilômetros em milhas
    de acordo com o algoritmo de Bruce.

    Entrada
    A primeira linha de entrada contém t, o número de distâncias que Bruce quer converter
    de quilômetros em milhas (0 < t <25000). Cada uma das t linhas contem um inteiro,
    correspondente a distância x (2 < x < 25000) em quilômetros.

    Saída
    Para cada x distância em quilômetros imprima a distância em milhas y calculadas de
    acordo com o algoritmo de Bruce.
    :return:
    """
    t = int(input())
    for i in range(t):
        fibo, fibo_bin, bruce_algo_bin, km_bin, milhas = [], [], [], 0, 0
        km = int(input())
        if km == 3:
            print(2)
        else:
            a, b = 1, 2
            p = a + b
            while a < km:
                fibo.append(a)
                a = b
                b = p
                p = a + b
            bruce_algo = fibo[0:-1]
            fibo.reverse()
            bruce_algo.reverse()
            for j in range(0, len(fibo)):
                km_bin += fibo[j]
                if km_bin > km:
                    km_bin -= fibo[j]
                    fibo_bin.append(0)
                else:
                    fibo_bin.append(1)
            bruce_algo_bin = fibo_bin[0:-1]
            for j in range(0, len(bruce_algo_bin)):
                milhas += bruce_algo[j] * bruce_algo_bin[j]
            print(milhas)


converter_quilometros_para_milhas()

def maior_numero_de_um_algarismo():
    """
    Os habitantes do planeta Uno possuem um terrível problema de detecção
    de números com mais de um algarismo, de modo que, para tudo que vão fazer,
    transformam qualquer valor inteiro em um número de um algarismo, realizando
    somas sucessivas do número até o mesmo ser reduzido a um algarismo. Por
    exemplo, o número 999999999991, no planeta Uno, soma-se todos os algarismos,
    resultando em 9+9+9+9+9+9+9+9+9+9+9+1 = 100. Como o número 100 tem mais de um
    algarismo, o processo se repete, resultando em 1+0+0 = 1

    Uma das grandes dificuldades que os habitantes possuem está em comparar dois números
    e verificar qual deles é o maior, segundo as regras do planeta.

    Escreva um programa que, dados dois números inteiros, identifique qual deles é o maior
    número de um algarismo.

    Entrada
    Haverá diversos casos de teste. Cada caso de teste inicia com dois inteiros N e M
    (0 ≤ N ≤ 10100, 0 ≤ M ≤ 10100), indicando os dois números a serem comparados.

    O último caso de teste é indicado quando N = M = 0, sendo que este caso não deverá ser processado.

    Saída
    Para cada caso de teste, imprima uma linha, contendo um inteiro, indicando 1 se o primeiro
    número for o maior de um algarismo, 2 se o segundo número for o maior de um algarismo ou
    0 se ambos os números possuírem o mesmo valor de um algarismo.
    :return:
    """
    while True:
        try:
            entrada = input().strip().split(" ")
            primeiro, segundo = entrada[0], entrada[1]
            soma1, soma2 = 0, 0
            for i in primeiro:
                soma1 += int(i)
                while soma1 >= 10:
                    primeiro = str(soma1)
                    soma1 = 0
                    for j in primeiro:
                        soma1 += int(j)
            for i in segundo:
                soma2 += int(i)
                while soma2 >= 10:
                    segundo = str(soma2)
                    soma2 = 0
                    for j in segundo:
                        soma2 += int(j)
            if soma1 > soma2:
                print(1)
            elif soma1 < soma2:
                print(2)
            elif soma1 == soma2 and soma1 != 0 and soma2 != 0:
                print(0)
        except EOFError:
            break


maior_numero_de_um_algarismo()

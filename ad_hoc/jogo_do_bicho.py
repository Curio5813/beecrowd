def jogo_do_bicho():
    """
    Em um país muito distante, as pessoas são viciadas em um jogo de
    apostas bastante simples. O jogo é baseado em números e é chamado
    jogo do bicho. O nome do jogo deriva do fato que os números são
    divididos em 25 grupos, dependendo do valor dos dois últimos dígitos
    (dezenas e unidades), e cada grupo recebe o nome de um animal. Cada
    grupo é associado a um animal da seguinte forma: o primeiro grupo
    (burro) consiste nos números 01, 02, 03 e 04; o segundo grupo (águia)
    é composto dos números 05, 06, 07 e 08; e assim em diante, até o ultimo
    grupo contendo os números 97, 98, 99 e 00. As regras do jogo são simples.
    No momento da aposta, o jogador decide o valor da aposta V e um número
    N (0 ≤ N ≤ 1000000). Todos os dias, na praça principal da cidade, um
    número M é sorteado (0 ≤ M ≤ 1000000). O prêmio de cada apostador é
    calculado da seguinte forma:

    Se M e N têm os mesmos quatro últimos dígitos (milhar, centena, dezena e
    unidade), o apostador recebe V × 3000 (por exemplo, N = 99301 e M = 19301);
    Se M e N têm os mesmos três últimos dígitos (centena, dezena e unidade), o
    apostador recebe V × 500 (por exemplo, N = 38944 e M = 83944);
    Se M e N têm os mesmos dois últimos dígitos (dezena e unidades), o apostador
    recebe V × 50 (por exemplo, N = 111 e M = 552211);
    Se M e N têm os dois últimos dígitos no mesmo grupo, correspondendo ao mesmo
    animal, o apostador recebe V × 16 (por exemplo, N = 82197 and M = 337600);
    Se nenhum dos casos acima ocorrer, o apostador não recebe nada.
    Obviamente, o prêmio dado a cada apostador é o máximo possível de acordo com as
    regras acima. No entanto, não é possível acumular prêmios, de forma que apenas
    um dos critérios acima deve ser aplicado no cálculo do prêmio. Se um número N ou M
    com menos de quatro dígitos for apostado ou sorteado, assuma que dígitos 0 devem
    ser adicionados na frente do numero para que se torne de quatro dígitos; por exemplo,
    17 corresponde a 0017.
    Dado o valor apostado, o número escolhido pelo apostador, e o número sorteado,
    seu programa deve calcular qual o prêmio que o apostador deve receber.
    Entrada
    A entrada contém vários casos de teste. Cada caso consiste em apenas uma linha,
    contendo um número real V e dois inteiros N e M, representando respectivamente o
    valor da aposta com duas casas decimais (0.01 ≤ V ≤ 1000.00), o número escolhido
    para a aposta (0 ≤ N ≤ 1000000) e o número sorteado (0 ≤ M ≤ 1000000). O final da
    entrada é indicado por uma linha contendo V = M = N = 0.

    Saída
    Para cada um dos casos de teste seu programa deve imprimir uma linha contendo um
    número real, com duas casas decimais, representando o valor do prêmio correspondente
    à aposta dada.
    :return:
    """
    temp, grupos, bicho, cont = [], [], "", 0
    for i in range(0, 10):
        for j in range(0, 10):
            if i == 0 and j == 0:
                pass
            else:
                bicho += str(i) + str(j)
                temp.append(bicho)
                bicho = ""
                cont += 1
                if cont % 4 == 0:
                    grupos.append(temp)
                    temp = []
    grupos.append(['97', '98', '99', '00'])
    while True:
        flag = 0
        entrada = list(input().split(" "))
        if entrada[0] == "0" and entrada[1] == "0" and entrada[2] == "0":
            break
        valor, n, m = float(entrada[0]), entrada[1], entrada[2]
        if len(n) < 4:
            while len(n) < 4:
                n = "0" + n
        if len(m) < 4:
            while len(m) < 4:
                m = "0" + m
        if n[-4::] == m[-4::]:
            print(f"{valor * 3000:.2f}")
            flag = 1
        elif n[-3::] == m[-3::]:
            print(f"{valor * 500:.2f}")
            flag = 1
        elif n[-2::] == m[-2::]:
            print(f"{valor * 50:.2f}")
            flag = 1
        elif n[-2::] != m[-2::]:
            for i in range(0, len(grupos)):
                for j in range(0, len(grupos[i])):
                    if n[-2::] in grupos[i] and m[-2::] in grupos[i]:
                        print(f"{valor * 16:.2f}")
                        flag = 1
                        break
                if flag == 1:
                    break
        if flag == 0:
            print("0.00")


jogo_do_bicho()

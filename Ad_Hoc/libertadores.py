def libertadores():
    """
    A Copa Libertadores da América é a principal competição de futebol entre
    clubes profissionais da América do Sul, organizada pela Confederação Sul-Americana
    de Futebol (CONMEBOL). Ela é conhecida por ter um regulamento muito complicado,
    principalmente nas fases das oitavas, quartas e semi-final.

    Nessas fases são jogadas partidas de ida e volta no sistema mata-mata. Ganha quem
    fizer a maior pontuação no acumulado das duas partidas, sendo 3 pontos para vitória
    e 1 ponto em caso de empate, ambos por partida. Em caso de igualdade na pontuação,
    são critérios de desempate:

    1) saldo de gols (número de gols a favor menos o número de gols contra).

    2) mais gols marcados na casa do adversário.

    3) disputa por pênaltis.

    Todos os critérios devem ser aplicados considerando o acumulado das duas partidas.

    Será que você consegue elaborar um algoritmo que, dados os resultados das partidas de
    ida e de volta, ele identifica o time vencedor?

    Entrada
    A primeira linha de entrada indica o número de casos de teste N (1 ≤ N ≤ 100). Cada
    caso de teste é composto por dois placares: o resultado da partida 1 e o resultado
    da partida 2. O placar é representado pelo formato M x V, onde M (1 ≤ M ≤ 100) é
    o número de gols do time mandante da partida e V (1 ≤ V ≤ 100) é o número de gols
    do time visitante. Como em cada caso de teste existem 2 partidas, considere que o
    Time 1 é sempre o mandante da primeira e o visitante da segunda e vice-versa para
    o Time 2.

    Saída
    Para cada caso de teste, imprima uma linha contendo "Time 1" (sem aspas) caso o Time 1
    seja o vencedor do mata-mata, "Time 2" (sem aspas) caso o Time 2 seja o vencedor do mata-mata
    e "Penaltis" (sem aspas) caso não seja possível identificar o vencedor no tempo convencional.
    :return:
    """
    n = int(input())
    cont, resultado, resultados = 0, [0, 0, 0, 0], []
    for i in range(1, (2 * n) + 1):
        if i % 2 == 1:
            placar = input().split(" ")
            time1 = int(placar[0])
            time2 = int(placar[2])
            resultado[0] = time1
            resultado[2] = time2
        elif i % 2 == 0:
            placar = input().split(" ")
            time1 = int(placar[2])
            time2 = int(placar[0])
            resultado[1] = time1
            resultado[3] = time2
        if i > 1 and i % 2 == 0:
            resultados.append(resultado)
            resultado = [0, 0, 0, 0]
    for i in range(0, len(resultados)):
        if resultados[i][0] > resultados[i][2] and resultados[i][1] > resultados[i][3]:
            print("Time 1")
        elif resultados[i][0] < resultados[i][2] and resultados[i][1] < resultados[i][3]:
            print("Time 2")
        elif resultados[i][0] == resultados[i][2] and resultados[i][1] > resultados[i][3]:
            print("Time 1")
        elif resultados[i][0] == resultados[i][2] and resultados[i][1] < resultados[i][3]:
            print("Time 2")
        elif resultados[i][0] > resultados[i][2] and resultados[i][1] == resultados[i][3]:
            print("Time 1")
        elif resultados[i][0] < resultados[i][2] and resultados[i][1] == resultados[i][3]:
            print("Time 2")
        else:
            if resultados[i][0] + resultados[i][1] > resultados[i][2] + resultados[i][3]:
                print("Time 1")
            elif resultados[i][0] + resultados[i][1] < resultados[i][2] + resultados[i][3]:
                print("Time 2")
            else:
                if resultados[i][1] > resultados[i][2]:
                    print("Time 1")
                elif resultados[i][1] < resultados[i][2]:
                    print("Time 2")
                else:
                    print("Penaltis")


libertadores()

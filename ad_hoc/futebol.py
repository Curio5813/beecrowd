def futebol():
    """
    O seu time de futebol favorito está jogando em um campeonato para
    caridade, que é parte de um esforço mundial para levantar fundos
    para ajudar crianças com dificuldades. Como em um campeonato normal,
    três pontos são dados ao time que vence um partida, e nenhum para o
    time que perdeu. Se o jogo termina em empate, cada time recebe um ponto.

    O seu time jogou N partidas durante a primeira fase do campeonato, que
    já terminou. Somente alguns times, os com mais pontos acumulados, irão
    avançar para a segunda fase do campeonato. Porém como o objetivo principal
    do campeonato é arrecadar dinheiro, antes de definir os times que passaram
    para a segunda fase, cada time pode comprar gols adicionais. Estes gols contam
    como gols marcados, e podem ser usados para alterar o resultado de qualquer
    partida que o time jogou.

    O orçamento do seu time é suficiente para comprar até G gols. Você pode informar
    o número máximo de pontos que o seu time pode obter após comprar os gols, supondo
    que os outros times não irão comprar nenhum gol?

    Entrada
    A entrada contém diversos casos de teste e termina com EOF. A primeira linha de um
    caso de teste contém dois inteiros N (1 ≤ N ≤ 105) e G (0 ≤ G ≤ 106) representando
    respectivamente o número de partidas que o seu time jogou e o número de gols que o
    seu time pode comprar. Cada uma das próximas N linhas descrevem o resutado de uma
    partida com dois inteiros S e R (0 ≤ S, R, ≤ 100), indicando respectivamente os gols
    que o seu time marcou e sofreu na partida antes da compra de gols.

    Saída
    Para cada caso de teste imprima uma linha com um inteiro representando o número máximo
    total de pontos que o seu time pode obter após comprar os gols.
    :return:
    """
    while True:
        try:
            partidas, gols_comprado = map(int, input().split())
            resultados, diffs, pontos = [], [], 0
            for i in range(partidas):
                resultados.append(list(map(int, input().split())))
            resultados = sorted(resultados)
            resultados.reverse()
            for i in range(len(resultados)):
                diff = resultados[i][0] - resultados[i][1]
                diffs.append(diff)
            diffs.reverse()
            for i in range(len(diffs)):
                if diffs[i] < 0:
                    pontos += 3
                elif diffs[i] == 0 and gols_comprado >= 1:
                    pontos += 3
                    gols_comprado -= 1
                elif diffs[i] == 0 and gols_comprado == 0:
                    pontos += 1
                else:
                    cont = 0
                    while diffs[i] > 0:
                        cont += 1
                        gols_comprado -= 1
                        if gols_comprado == 0:
                            break
                        if diffs[i] + cont >= 1:
                            pontos += 3
            print(pontos)
        except EOFError:
            break


futebol()

"""
2 1
1 1
1 1
3 2
1 3
3 1
2 2
4 10
1 1
2 2
1 3
0 4
"""
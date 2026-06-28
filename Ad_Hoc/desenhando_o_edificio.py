def desenhando_o_edificio():
    """
    Um arquiteto quer projetar um edifício muito alto. A construção será composta
    por alguns andares, e cada andar terá um certo tamanho. O tamanho de um pavimento
    tem que ser maior do que o tamanho do piso imediatamente acima dele. Além disso,
    o designer (que é um fã de um famoso time de futebol espanhol) quer pintar o
    prédio em azul e vermelho, cada andar uma cor, e de tal forma que as cores dos
    dois andares consecutivos sejam diferentes.

    Para projetar o edifício o arquiteto tem n pisos disponíveis, com seus tamanhos e
    cores associadas. Todos os andares estão disponíveis em diferentes tamanhos. O
    arquiteto quer projetar o edifício mais alto possível, com estas restrições, usando
    os andares disponíveis.

    Entrada
    O arquivo de entrada é constituído por uma primeira linha com p número de casos
    de teste para resolver. A primeira linha de cada caso de teste contém o número de
    pisos disponíveis. Então, o tamanho e a cor de cada andar aparece numa linha. Cada
    andar é representado por um número inteiro entre -999999 e 999999. Não há andar com
    o tamanho 0. Os números negativos representam pisos vermelhos e números positivos
    pisos azuis. O tamanho do andar é o valor absoluto do número. Não existem dois
    pisos, com o mesmo tamanho. O número máximo de andares para um problema é 500000.

    Saída
    Para cada caso, a saída será constituída por uma linha com o número de andares do edifício
    mais alto com as condições mencionadas.
    :return:
    """
    while True:
        try:
            n = int(input())
            for i in range(n):
                andares = []
                pisos_disponiveis = int(input())
                for j in range(pisos_disponiveis):
                    andar = int(input())
                    andares.append(andar)
                andares.sort()
                for j in range(len(andares)):
                    for k in range(len(andares)):
                        if abs(andares[j]) < abs(andares[k]):
                            andares[j], andares[k] = andares[k], andares[j]
                piso, pisos = 0, 0
                for j in range(len(andares)):
                    if j == 0:
                        piso = andares[j]
                        pisos += 1
                    if j > 0 and piso > 0:
                        if andares[j] < piso:
                            piso = andares[j]
                            pisos += 1
                    elif j > 0 > piso:
                        if andares[j] > piso:
                            piso = andares[j]
                            pisos += 1
                print(pisos)
        except EOFError:
            break


desenhando_o_edificio()

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
    n = int(input())
    while n > 0:
        andares_azuis, andares_vermelhos, andares_altura, numero_andares, j = [], [], [], 0, 0
        pisos_disponiveis = int(input())
        for i in range(pisos_disponiveis):
            andares = int(input())
            if andares > 0:
                andares_azuis.append(andares)
            elif andares < 0:
                andares_vermelhos.append(abs(andares))
            andares_altura.append(abs(andares))
        andares_azuis.sort()
        andares_azuis.reverse()
        andares_vermelhos.sort()
        andares_vermelhos.reverse()
        andares_altura.sort()
        andares_altura.reverse()
        maximo = max(andares_altura)
        if len(andares_azuis) == 0 or len(andares_vermelhos) == 0:
            print(1)
        else:
            if maximo in andares_azuis and len(andares_azuis) > len(andares_vermelhos):
                for i in range(0, len(andares_azuis)):
                    if i == 0:
                        numero_andares += 2
                        j += 1
                        if j == len(andares_vermelhos):
                            break
                    elif i > 0 and andares_azuis[i] < andares_vermelhos[j]:
                        numero_andares += 2
                        j += 1
                        if j == len(andares_vermelhos):
                            break
                    elif i == len(andares_azuis) - 1 and andares_azuis[i] > andares_vermelhos[j]:
                        numero_andares += 2
                        break
            elif maximo in andares_azuis and len(andares_azuis) < len(andares_vermelhos):
                for i in range(0, len(andares_vermelhos)):
                    if i == 0:
                        numero_andares += 2
                        j += 1
                        if j == len(andares_azuis):
                            break
                    elif i > 0 and andares_vermelhos[i] > andares_azuis[j]:
                        numero_andares += 1
                        j += 1
                        if j == len(andares_azuis) and andares_vermelhos[i + 1] < andares_azuis[j - 1]:
                            numero_andares += 1
                            break
                        else:
                            break
            elif maximo in andares_azuis and len(andares_azuis) == len(andares_vermelhos):
                for i in range(0, len(andares_azuis)):
                    if i == 0:
                        numero_andares += 2
                    elif i > 0 and andares_azuis[i] > andares_vermelhos[i]:
                        numero_andares += 2
            elif maximo in andares_vermelhos and len(andares_vermelhos) > len(andares_azuis):
                for i in range(0, len(andares_vermelhos)):
                    if i == 0:
                        numero_andares += 2
                        j += 1
                        if j == len(andares_azuis):
                            break
                    elif i > 0 and andares_vermelhos[i] < andares_azuis[j]:
                        numero_andares += 2
                        j += 1
                        if j == len(andares_azuis):
                            numero_andares += 1
                            break
                    elif i == len(andares_vermelhos) - 1 and andares_vermelhos[i] > andares_azuis[j]:
                        numero_andares += 2
                        break
            elif maximo in andares_vermelhos and len(andares_vermelhos) < len(andares_azuis):
                for i in range(0, len(andares_azuis)):
                    if i == 0:
                        numero_andares += 2
                        j += 1
                        if j == len(andares_vermelhos):
                            break
                    elif i > 0 and andares_azuis[i] > andares_vermelhos[j]:
                        numero_andares += 1
                        j += 1
                        if j == len(andares_vermelhos) and andares_azuis[i + 1] < andares_vermelhos[j - 1]:
                            numero_andares += 1
                            break
                        else:
                            break
            elif maximo in andares_vermelhos and len(andares_vermelhos) == len(andares_azuis):
                for i in range(0, len(andares_vermelhos)):
                    if i == 0:
                        numero_andares += 2
                    elif i > 0 and andares_vermelhos[i] > andares_azuis[i]:
                        numero_andares += 2
            print(numero_andares)
        n -= 1


desenhando_o_edificio()

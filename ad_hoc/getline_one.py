def getline_one():
    """
    Mangojata está aprendendo programação. Ela acha tudo muito
    fácil, muito simples. Ela está prestes a fazer um pequeno
    programa que leia o nome dos seus amigos e a distância de
    sua casa até cada um deles. Desta forma, ela quer simplesmente
    calcular qual é a distância média que deve ser percorrida para
    chegar na casa de qualquer um de seus amigos (em metros). Porém
    Aristoclenes, que é um programador mais experiente, lhe alertou
    que às vezes o que parece muito simples tem lá seus detalhes,
    dependendo da linguagem que é utilizada para implementação.

    Entrada
    A entrada contém vários casos de teste e termina com EOF (Fim de Arquivo).
    Cada caso de teste consiste de duas linhas de entrada. A primeira linha
    contém o nome de um amigo de Mangojata e a segunda linha contém um valor
    inteiro que indica a distância aproximada da casa deste amigo até a casa
    de Mangojata.

    Saída
    A saída deve ser um único valor com uma casa decimal (utilize uma variável de
    dupla precisão - ddouble) indicando a distância média entre a casa de Mangojata
    e de seus amigos, conforme exemplo abaixo.
    :return:
    """
    while True:
        dist, dist_med, cont, tempo = 0, 0, 0, 0
        try:
            amigo = input()
            distancia = int(input())
            dist += distancia
            cont += 1
            while amigo != "":
                amigo = input()
                if amigo == "":
                    print(end="")
                    print(f"{dist_med:.1f}")
                    break
                else:
                    distancia = int(input())
                    dist += distancia
                    cont += 1
                    dist_med = dist / cont
        except EOFError:
            break


getline_one()

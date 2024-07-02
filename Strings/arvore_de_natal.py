def arvore_de_natal():
    """
    As crianças adoram desenhar árvores de natal e você desafiou
    algumas delas a desenharem árvores de diversos tamanhos com
    apenas com o caractere asterisco "*".

    A regra é simples. De baixo para cima, o tronco da árvore consiste
    de 3 asteriscos e depois 1. Em seguida vem o restante da árvore,
    com cada fileira de folhas iniciando no tamanho que você determinou
    e diminuindo de dois em dois, até chegar na copa da árvore que terá
    apenas um asterisco. Note que para isso dar certo, somente será
    permitido tamanhos ímpares para estas árvores.

    Entrada
    A entrada contém vários casos de teste e termina com EOF. Cada caso
    de teste consiste em um inteiro N (2 < N < 100).

    Saída
    Para cada caso de teste de entrada, seu programa deverá desenhar uma
    árvore conforme especificação acima e exemplo abaixo, com uma linha em
    branco após cada árvore.
    :return:
    """
    while True:
        try:
            n = int(input())
            k, galho, galhos = 1, "", []
            while k <= n:
                galho += "*"
                if len(galho) % 2 == 1:
                    galhos.append(galho)
                k += 1
            for i in range(0, len(galhos)):
                print(f"{galhos[i].center(n).rstrip()}")
            print("*".center(n).rstrip())
            print("***".center(n).rstrip())
            print("")
        except EOFError:
            break


arvore_de_natal()

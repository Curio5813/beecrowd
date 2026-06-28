def chocolate2():
    """
    Por lei, na Nlogônia todas as barras de chocolate são quadradas.
    Anamaria tem uma barra quadrada de chocolate de lado L, que ela quer
    compartilhar com alguns colegas da obi. Mas ela é uma boa cidadã e
    cumpre a lei. Então, ela divide a barra em quatro pedaços quadrados, de
    lado L/2. Depois, ela repete esse procedimento com cada pedaço gerado,
    sucessivamente, enquanto o lado for maior do que, ou igual a 2cm. Você
    deve escrever um programa que, dado o lado L da barra inicial, em centímetros,
    determina quantos pedaços haverá ao final do processo.

    Entrada
    A entrada consiste de uma linha, com um único inteiro, L (2 ≤ L ≤ 104), o
    número de centímetros do lado do quadrado.

    Saída
    Se programa deve imprimir uma única linha, contendo um único inteiro, igual ao
    número total de pedaços obtidos pela Anamaria.
    :return:
    """
    l = int(input())
    cont = 1
    pedaco = l
    while pedaco > 1:
        l //= 2
        pedaco = l
        cont *= 4
    print(cont)


chocolate2()

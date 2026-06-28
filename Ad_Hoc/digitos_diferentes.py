def digitos_diferentes():
    """
    Os habitantes de Nlogônia são muito supersticiosos. Uma de suas crenças
    é que os números das casas de rua que têm um dígito repetido traz sorte
    ruim para os moradores. Portanto, eles nunca iriam viver em uma casa que
    tem o número 838 ou 1004, por exemplo.

    A rainha de Nlogônia ordenou a construção de uma nova avenida à beira-mar e
    quer atribuir para as novas casas apenas números sem dígitos repetidos, para
    evitar desconforto entre os seus súditos. Você foi nomeado por Sua Majestade
    para escrever um programa que, dado dois inteiros N e M, determine a quantidade
    máxima possível de casas que podem assumir um número entre N e M inclusive, sem
    que ocorram dígitos repetidos nestes números.

    Entrada
    Cada teste é descrito usando uma linha. A linha contém dois inteiros N e M, conforme
    descrito acima (1 ≤ N ≤ M ≤ 5000).

    Saída
    Para cada caso de teste imprima um valor inteiro que representa a quantidade máxima
    possível de números de casa entre N e M inclusive, sem dígitos repetidos.
    :return:
    """
    while True:
        try:
            numeros = list(map(int, input().split(" ")))
            inicio, fim = numeros[0], numeros[1]
            cont, flag = 0, 1
            for i in range(inicio, fim + 1):
                str_num = str(i)
                for j in str_num:
                    if str_num.count(j) > 1:
                        flag = 0
                        break
                if flag == 1:
                    cont += 1
                else:
                    flag = 1
            print(cont)
        except EOFError:
            break


digitos_diferentes()

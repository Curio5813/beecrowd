def exercicio_de_historia():
    """
    Esta função calcula o século de um dado ano. A entrada
    consiste em vários casos de teste e é terminada pelo
    final de arquivo (EOF). Cada linha é um novo caso de
    teste e contém um único inteiro N (1 ≤ N ≤ 109), que
    corresponde ao valor de algum ano que deve ser processado.
    A saída para cada caso de teste, imprimi uma única linha
    contendo o valor do século do ano correspondente.
    :return:
    """
    while True:
        try:
            ano = int(input())
            resto = ano % 100
            div_int = ano // 100
            if resto >= 1:
                seculo = div_int + 1
                print(seculo)
            else:
                seculo = div_int
                print(seculo)

        except EOFError:
            break


exercicio_de_historia()

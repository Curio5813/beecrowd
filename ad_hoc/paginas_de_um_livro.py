def paginas_de_um_livro():
    """
    As páginas de um livro são numeradas de 1 até a última página P.
    Dada a quantidade de páginas de um livro, sua tarefa é informar
    quantos dígitos foram usados para numerar este livro, da página
    1 até a página P.

    Entrada
    A entrada é formada por uma única linha contendo um inteiro P
    (que varia de 1 a menos de 1 milhão), que representa o número
    total de páginas do respectivo livro.

    Saída
    A saída é composta por uma única linha na saída, contendo a quantidade
    de dígitos que foram usados para numerar todas as P páginas do livro,
    da página 1 até a página P.
    :return:
    """
    p = int(input())
    qtd_digitos = 0
    for i in range(1, p + 1):
        digitos = str(i)
        qtd_digitos += len(digitos)
    print(qtd_digitos)


paginas_de_um_livro()

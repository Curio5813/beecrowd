def combinador():
    """
    Implemente um programa denominado combinador, que recebe
    duas strings e deve combiná-las, alternando as letras de
    cada string, começando com a primeira letra da primeira
    string, seguido pela primeira letra da segunda string, em
    seguida pela segunda letra da primeira string, e assim
    sucessivamente. As letras restantes da cadeia mais longa
    devem ser adicionadas ao fim da string resultante e retornada.

    Entrada
    A entrada contém vários casos de teste. A primeira linha
    contém um inteiro N que indica a quantidade de casos de
    teste que vem a seguir. Cada caso de teste é composto por uma
    linha que contém duas cadeias de caracteres, cada cadeia de
    caracteres contém entre 1 e 50 caracteres inclusive.

    Saída
    Combine as duas cadeias de caracteres da entrada como mostrado
    no exemplo abaixo e exiba a cadeia resultante.
    :return:
    """
    n = int(input())
    strings, combinator, j = [], "", 0
    for i in range(n):
        strings = input().split(" ")
        if len(strings[0]) == len(strings[1]):
            for k in range(0, len(strings[0])):
                combinator += strings[0][j]
                combinator += strings[1][j]
                j += 1
        elif len(strings[0]) > len(strings[1]):
            for k in range(0, len(strings[1])):
                if j >= len(strings[1]) - 1:
                    combinator += strings[0][j]
                    combinator += strings[1][j]
                    j += 1
                    combinator += strings[0][j::]
                    break
                combinator += strings[0][j]
                combinator += strings[1][j]
                j += 1
        elif len(strings[0]) < len(strings[1]):
            for k in range(0, len(strings[0])):
                if j >= len(strings[0]) - 1:
                    combinator += strings[0][j]
                    combinator += strings[1][j::]
                    break
                combinator += strings[0][j]
                combinator += strings[1][j]
                j += 1
        print(combinator)
        combinator = ""
        j = 0


combinador()

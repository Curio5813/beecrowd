def contagem_de_digitos():
    """
    Diana escreverá uma lista com todos os inteiros positivos
    entre A e B, inclusive, na base decimal e sem zeros à esquerda.
    Ela quer saber quantas vezes cada um dos dígitos irá ser usado.

    Entrada
    Cada caso de teste é dado em uma única linha que contém dois inteiros
    A e B (1 ≤ A ≤ B ≤ 108). O último caso de teste é seguido por uma linha
    contendo dois zeros.
    Saída
    Para cada caso de teste, imprima uma única linha com 10 inteiros representando
    o número de vezes que cada dígito é usado ao escrever todos os inteiros
    entre A e B, inclusive, na base decimal e sem zeros à esquerda. Escreva a
    contagem de cada dígito em ordem crescente do 0 até o 9.
    return:
    """
    while True:
        a, b = map(int, input().split(" "))
        digitos, cont, str_numero, quantidade = "0123456789", 0, "", []
        if a == 0 and b == 0:
            break
        else:
            for i in range(a, b + 1):
                str_numero += str(i)
            for i in digitos:
                quantidade.append(str_numero.count(i))
            print(*quantidade)


contagem_de_digitos()

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
        digitos, cont, qtd = "0123456789", 0, []
        print(3 % 10)
        if a == 0 and b == 0:
            break
        else:
            for k in digitos:
                for i in range(a, b + 1):
                    cont += str(i).count(k)
                qtd.append(cont)
                cont = 0
            print(*qtd)


contagem_de_digitos()

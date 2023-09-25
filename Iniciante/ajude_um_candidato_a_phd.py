def ajude_um_candidato_a_phd():
    """
    Está função calcula e printa a soma de dois números ou.
    caso o problema seja "P=NP", imprime a palavra "skipped".
    A primeira linha de entrada será um único inteiro N
    (1 ≤ N ≤ 1000) denotando o número de casos de teste.
    Em seguida, siga N linhas com ”P = NP” ou um problema de
    adição na forma ”a + b”, onde a, b ∈ [0, 1000] são inteiros.
    Na saída temos o resultado de cada adição. Para linhas
    contendo “P = NP”, imprima “pulado”.
    :return:
    """
    n = int(input())
    for i in range(n):
        num1, num2, k, soma = "", "", 0, 0
        p = input()
        if p == "P=NP":
            print("skipped")
        else:
            while p[k] != "+":
                num1 += p[k]
                k += 1
            else:
                k += 1
                while k <= len(p) - 1:
                    num2 += p[k]
                    k += 1
            num1 = int(num1)
            num2 = int(num2)
            soma = num1 + num2
            print(soma)


ajude_um_candidato_a_phd()

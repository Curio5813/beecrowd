def lexico():
    """
    Esta função recebe como entrada duas strings A e B e calcula
    se a string A deve ser printada antes da string B, ou a string
    B antes da string A, seguindo a seguinte regra: Caso o primeiro
    caractere de A venha antes do primeiro de B, coloca-se A antes de B.
    Se o primeiro caractere for igual, usa-se o seguinte para desempate.
    E se o segundo empatar, usa-se o terceiro, etc. Quando todos os
    caracteres de A forem iguais ao começo de B, ou todos os de B forem
    iguais ao começo de A, coloca-se a menor palavra primeiro. A saída
    contém as mesmas 2 palavras, só que na ordem lexicográfica.
    :return:
    """
    alfab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    a = input()
    b = input()
    n = 0
    lex1 = alfab.index(a[n])
    lex2 = alfab.index(b[n])
    if lex1 < lex2:
        print(a)
        print(b)
    elif lex1 > lex2:
        print(b)
        print(a)
    while lex1 == lex2:
        if n >= len(a) - 1 or n >= len(b) - 1:
            if len(a) == len(b):
                lex1 = alfab.index(a[n])
                lex2 = alfab.index(b[n])
                if lex1 == lex2:
                    print(a)
                    print(b)
                    break
                elif lex1 < lex2:
                    print(a)
                    print(b)
                    break
                elif lex1 > lex2:
                    print(b)
                    print(a)
                    break
            elif len(a) < len(b):
                print(a)
                print(b)
                break
            elif len(a) > len(b):
                print(b)
                print(a)
                break
        n += 1
        lex1 = alfab.index(a[n])
        lex2 = alfab.index(a[n])
        if lex1 < lex2:
            print(a)
            print(b)
            break
        elif lex1 > lex2:
            print(b)
            print(a)
            break


lexico()

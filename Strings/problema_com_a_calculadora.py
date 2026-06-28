def problema_com_a_calculadora():
    """
    Joãozinho tem que ajudar seu pai. Um relatório específico
    com alguns números está saindo com caracteres indesejáveis
    no meio. A ideia é apenas somar os 3 valores que aparecem
    em cada linha sempre na mesma posição, ignorando as letras
    e apresentar esta soma. Não existem espaços em branco na linha.

    Entrada
    A primeira linha de entrada contém um inteiro N (N < 100000).
    Seguem N linhas com exatos 14 caracteres que devem ser lidas e
    delas extraídos e somados os três números existentes.

    Saída
    Para cada linha de entrada, seu programa deve apresentar um valor
    numérico inteiro, que é a soma dos 3 números existentes na linha.
    :return:
    """
    n = int(input())
    for i in range(n):
        j, numero, numeros, k = 0, "", [], 0
        entradas = input()
        while j <= len(entradas) - 1:
            if numero in "1234567890":
                k = j
                while entradas[k] in "1234567890":
                    numero += entradas[k]
                    k += 1
                    if k > len(entradas) - 1:
                        break
                if numero != "":
                    numeros.append(int(numero))
                    numero = ""
            j = k
            j += 1
        print(sum(numeros))


problema_com_a_calculadora()

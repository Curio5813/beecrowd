def ajude_nhonho():
    """
    Depois de Professor Girafales descobrir que Nhonho faltava às aulas
    e pedia para Chaves assinar seu nome na lista de presença em troca
    de um pão com presunto, Nhonho começou a receber toda semana um desafio
    especial do professor, e se ele não os resolvesse, seria dedurado para
    seu pai.

    O desafio dessa semana se chama “Soma permutada”, e consiste em resolver
    o seguinte enigma: abc + acb + bac + bca + cab + cba = K, dado um valor
    de K, sem que ocorram repetições de dígitos (a ≠ b ≠ c).

    Com K = 1332, uma das possíveis soluções seria usar a = 1, b = 2 e c = 3,
    somando suas permutações: 123 + 132 + 213 + 231 + 312 + 321 = 1332.

    Outra solução seria: a = 0, b = 1, c = 5: 015 + 051 + 105 + 150 + 501 + 510 = 1332.

    As explicações acima usaram apenas 3 dígitos para maior facilidade de entendimento,
    o problema real, que Professor Girafales passou a Nhonho e você terá que ajudá-lo a
    resolver, consiste em 5 dígitos, e deverá ser somada todas suas permutações (abcde +
    abced + ..... + edcba), sem repetição de dígitos (a ≠ b ≠ c ≠ d ≠ e).

    Dado o valor de K, exiba, lexicograficamente, todos os possíveis conjuntos de números
    que satisfaçam o enigma de Girafales.

    Entrada
    A primeira linha da entrada possui um inteiro T, indicando a quantidade de casos de
    testes. Cada uma das T linhas a seguir contém um inteiro K (1 ≤ K ≤ 107), como descrito
    acima.

    Saída
    Para cada caso, exiba lexicograficamente o(s) conjunto(s) de valores {a, b, c, d, e}
    que resolvem o enigma do professor Girafales, ou “impossivel” caso não exista solução.

    Deixe uma linha em branco após cada caso de teste. Observe a formatação de saída.
    :return:
    """
    t = int(input())
    digitos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    str_num, numeros_srt, permutacoes, j, m = "", [], [], 0, 0
    for i in range(t):
        k = int(input())
        for j in range(0, len(digitos)):
            for k in range(0, len(digitos)):
                str_num += str(digitos[k])
                if len(str_num) == 5:
                    numeros_srt.append(str_num)
                    str_num = ""
                    m += 1
        print(numeros_srt)


ajude_nhonho()

def divisibilidade_por_3 ():
    """
    No mundo da matemática, para sabermos se um grande número é
    divisível por outro existe uma regra, chamada de regra de
    divisibilidade. Um número natural é divisível por 3 quando a
    soma de todos os seus algarismos forma um número divisível por
    3, ou seja, um múltiplo de 3.

    Ex1: 1.104 é divisível por 3?

    Resposta: SIM. É divisível por 3, pois seus algarismos quando somados:
    1 + 1 + 0 + 4 = 6, que é um número divisível por 3 (porque 6 ÷ 3 = 2,
    que é um número natural).

    Ex2: 2.791.035 é divisível por 3?

    Resposta: SIM. 2.791.035 é constituído de algarismos que somados:
    2 + 7 + 9 + 1 + 0 + 3 + 5 = 27, gera um número divisível por 3
    (pois 27 ÷ 3 = 9, número natural).

    Entrada
    O arquivo de entrada conterá dois números, n (1< n <10) indicando o
    número de algarismos de m, (1< m < 1000000000).

    A entrada termina com o fim do arquivo (EOF).

    Saída
    Seu programa deve fornecer o número da soma dos algarismos de m e logo depois
    apresentar “sim” caso o número seja divisível por 3 ou “nao” caso não seja.
    Não esqueça o fim de linha após o produto, caso contrário seu programa
    apresentará a mensagem: “Presentation Error”.
    :return:
    """
    while True:
        try:
            n, m = map(int, input().strip().split(" "))
            str_m = str(m)
            soma = 0
            for i in str_m:
                i = int(i)
                soma += i
            if soma % 3 == 0:
                print(soma, "sim")
            else:
                print(soma, "nao")
        except EOFError:
            break


divisibilidade_por_3()

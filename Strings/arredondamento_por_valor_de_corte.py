def arredondamento_por_valor_de_corte():
    """
    Frequentemente, ao arredondar um número real para um inteiro nós o fazemos
    para cima se a parte fracionária é maior ou igual a 0,5 e para baixo se a
    parte fracionária é menor do que 0,5. Neste problema você recebe uma string
    num contendo um número real e uma string cutoff contendo um valor de corte.
    A string cutoff será formatada exatamente como "0.####", onde cada '#' representa
    um dígito ('0'-'9'). Pelo menos um dos dígitos da parte fracionária de cutoff
    será diferente de zero. Sua tarefa é arredondar num para cima se a parte fracionária
    é maior do que o valor de corte e para baixo caso contrário, devolvendo o resultado
    como um inteiro. Para evitar problemas com imprecisão de representação em ponto
    flutuante a parte fracionária de num não será exatamente igual a cutoff. Assim,
    o método tradicional de arredondamento descrito na frase inicial seria representado
    por cutoff = "0.5000"

    Entrada
    A entrada contem vários casos de teste. Cada caso de teste é composto por duas linhas.
    A string num está na primeira linha e a string cutoff fica na segunda linha. A string
    num é formada por 1 ou mais dígitos ('0' a '9') com um ponto decimal opcional ('.').
    A string num tem de 1 a 10 caracteres. A string cutoff é formatada exatamente como "0.####",
    onde cada '#' representa um dígito ('0' a '9'). Além disso, a parte fracionária de num NÃO
    será exatamente igual a cutoff.

    O final da entrada é determinado por EOF.

    Saída
    Para cada caso de teste da entrada seu programa deve gerar uma linha de saída somente com a
    parte inteira de num arredondada de acordo com o valor de corte em cutoff.
    :return:
    """
    while True:
        try:
            num = input().split('.')
            if len(num) == 1:
                num.extend(['0'])
            if num[0] == '':
                num[0] = '0'
            cutoff = input().split('.')
            if len(cutoff[1]) > len(num[1]):
                while len(cutoff[1]) > len(num[1]):
                    num[1] += '0'
            elif len(cutoff[1]) < len(num[1]):
                while len(cutoff[1]) < len(num[1]):
                    cutoff[1] += '0'
            if float(cutoff[1]) == float(num[1]):
                diff = float(num[0])
                diff = round(diff, 0)
                print(int(diff))
            elif float(cutoff[1]) > float(num[1]):
                diff = float(num[0])
                diff = round(diff, 0)
                print(int(diff))
            elif float(cutoff[1]) < float(num[1]):
                diff = float(num[0])
                diff = round(diff, 0)
                if float(num[1]) % 9 == 1:
                    diff = float(num[0])
                    diff = round(diff, 0) + 1
                    print(int(diff))
                elif diff == 0:
                    print(1)
                elif float(cutoff[1]) < float(num[1]):
                    print(int(diff) + 1)
        except EOFError:
            break


arredondamento_por_valor_de_corte()

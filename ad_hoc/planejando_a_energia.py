def planejando_a_energia():
    """
    Você está participando de um comitê que irá ajudar a planejar o
    crescimento da energia elétrica no Brasil, garantindo assim que
    as usinas consigam fornecer a energia necessária no futuro.

    Para isso você tem as seguintes informações:

    durante o ano de 2010 o consumo médio do brasileiro foi de 104.326 GWh.
    em 2013 o consumo foi de 127.755 GWh.
    Você deve determinar a taxa de crescimento anual para diferentes situações
    e previsões futuras, considerando o fato deste crescimento ser linear.
    Nesse caso, a taxa foi de 7.809,66 GWh/ano.

    Entrada
    A primeira linha da entrada contém um número inteiro N (1 ≤ N ≤ 1000)
    representando o total de casos de testes.

    As N linhas seguintes são compostas de 4 números inteiros A, B (B > 0), C,
    D (D > 0) separados por espaço. O número A representa o ano, o número B
    representa o consumo do ano A. O número C representa um outro ano e o número
    D representa o consumo de C.

    Saída
    Para cada caso de teste deverá ser impresso a taxa de crescimento anual com
    apenas duas casas decimais, separadas por vírgula e truncadas, ou seja, sem
    arredondamentos.
    :return:
    """
    n = int(input())
    dados = []
    for i in range(n):
        dado = list(map(int, input().split()))
        dados.append(dado)
        x1 = dados[i][1]
        y1 = dados[i][0]
        x2 = dados[i][3]
        y2 = dados[i][2]
        a = (x2 - x1) / (y2 - y1)
        consumo_anual = str(round(a, 3))
        if consumo_anual[-2:] == '.0':
            print(f"{consumo_anual[0:-2] + ',00'}")
        else:
            print(f"{consumo_anual[:-1].replace('.', ',')}")


planejando_a_energia()

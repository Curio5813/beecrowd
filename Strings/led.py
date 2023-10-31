def led():
    """
    João quer montar um painel de leds contendo diversos números.
    Ele não possui muitos leds, e não tem certeza se conseguirá
    montar o número desejado. Considerando a configuração dos leds
    dos números abaixo, faça um algoritmo que ajude João a descobrir
    a quantidade de leds necessário para montar o valor. A entrada
    contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número
    de casos de teste, seguido de N linhas, cada linha contendo um
    número (1 ≤ V ≤ 10100) correspondente ao valor que João quer
    montar com os leds. A saída para cada caso de teste, imprime
    uma linha contendo o número de leds que João precisa para montar
    o valor desejado, seguido da palavra "leds".
    :return:
    """
    leds = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
    digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    cont = 0
    n = int(input())
    for i in range(n):
        num = input()
        for k in num:
            digito = int(k)
            cont += leds[digitos.index(digito)]
        print(f"{cont} leds")
        cont = 0


led()

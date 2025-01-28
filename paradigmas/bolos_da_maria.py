def bolos_da_maria():
    """
    Dona Maria é uma senhora que está aposentada e faz doces. Ela
    começou a fazer bolos para complementar a renda da família.

    Para fazer um bolo, Dona Maria precisa de certa quantidade de alguns
    ingredientes diferentes. Cada ingrediente tem um custo fixo por unidade.
    Ela tem uma quantia de dinheiro D máxima para gastar na compra dos
    ingredientes. Dentre os tipos de bolos que existem, você deve escolher
    apenas um tipo, de maneira a maximizar a quantia de bolos.

    Calcule o número máximo de bolos de um único tipo que podem ser confeccionados.

    Entrada
    Na primeira linha terá um inteiro T (T ≤ 100) indicando o número de casos de teste.

    Para cada cada caso de teste, na primeira linha haverá três números inteiros D
    (1 ≤ D ≤ 109), I (1 ≤ I ≤ 100) e B (1 ≤ B ≤ 100) indicando o dinheiro que Dona
    Maria tem, o número de ingredientes existentes e a quantidade de tipo de bolos
    existentes, respectivamente. A próxima linha conterá I números inteiros indicando
    o preço da unidade de cada ingrediente. Seguem B linhas seguirão descrevendo cada
    bolo. O i-ésimo bolo é descrito da seguinte maneira: inicialmente há um número Qi
    (1 ≤ Qi ≤ 100) que indicará quantos ingredientes diferentes serão necessários.
    Logo em seguida teremos Qi pares de números indicando respectivamente o índice do
    ingrediente e a quantidade necessária, todos na mesma linha separados por espaços.

    A quantia de cada ingrediente em um bolo poderá variar de 1 até 1000. Cada unidade
    de um ingrediente custará entre 1 e 1000. Os ingredientes na descrição de cada bolo
    serão diferentes. Os identificadores de ingrediente vão de 0 até I-1.

    Saída
    Para cada caso imprima o número máximo de bolos do mesmo tipo que podem ser confeccionados.
    :return:
    """
    t = int(input())
    for i in range(t):
        d, i, b = map(int, input().split(" "))
        qtd = []
        ingredientes = list(map(int, input().split(" ")))
        for j in range(b):
            valor, bolos = 0, 0
            receita = list(map(int, input().split(" ")))
            for k in range(1, len(receita), 2):
                if k >= len(receita) - 1:
                    break
                valor += ingredientes[receita[k]] * receita[k + 1]
            bolos = d // valor
            qtd.append(bolos)
        print(max(qtd))


bolos_da_maria()

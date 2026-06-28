def jogando_cartas_fora():
    """
    Dada uma pilha de n cartas enumeradas de 1 até n com a carta 1 no topo
    e a carta n na base.  A seguinte operação é ralizada enquanto tiver 2
    ou mais cartas na pilha.

    Jogue fora a carta do topo e mova a próxima carta (a que ficou no topo)
    para a base da pilha.

    Sua tarefa é encontrar a sequência de cartas descartadas e a última carta
    remanescente.

    Cada linha de entrada (com exceção da última) contém um número n ≤ 50. A
    última linha contém 0 e não deve ser processada. Cada número de entrada
    produz duas linhas de saída. A primeira linha apresenta a sequência de
    cartas descartadas e a segunda linha apresenta a carta remanescente.

    Entrada
    A entrada consiste em um número indeterminado de linhas contendo cada uma um
    valor de 1 até 50. A última linha contém o valor 0.

    Saída
    Para cada caso de teste, imprima duas linhas. A primeira linha apresenta a sequência
    de cartas descartadas, cada uma delas separadas por uma vírgula e um espaço. A segunda
    linha apresenta o número da carta que restou. Nenhuma linha tem espaços extras no início
    ou no final. Veja exemplo para conferir o formato esperado.
    :return:
    """
    n = int(input())
    while n != 0:
        cartas, descarte = [], []
        for i in range(n, 0, -1):
            cartas.append(i)
        if len(cartas) == 1:
            print("Discarded cards:")
            print(f"Remaining card: {cartas[0]}")
        else:
            for i in range(0, len(cartas)):
                if len(cartas) == 1:
                    break
                a = cartas.pop()
                b = cartas[-1]
                descarte.append(a)
                cartas.insert(0, b)
                cartas.pop()
            print("Discarded cards:", end=" ")
            for i in range(0, len(descarte)):
                if i == len(descarte) - 1:
                    print(descarte[i])
                    break
                print(f"{descarte[i]},", end=" ")
            print(f"Remaining card: {cartas[0]}")
        n = int(input())


jogando_cartas_fora()

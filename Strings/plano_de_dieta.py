def plano_de_dieta():
    """
    O doutor deu a você a sua dieta, na qual cada caractere corresponde
    a algum alimento que você deveria comer. Você também sabe o que você
    tem comido no café da manha e no almoço, nos quais cada caractere
    corresponde a um tipo de alimento que você deveria ter comido aquele
    dia. Você decidiu que irá comer todo o restante de sua dieta durante
    o jantar, e você quer imprimi-la como uma String (ordenada em ordem
    alfabética). Se você trapaceou de algum modo (ou por comer muito de tipo
    de alimento, ou por comer algum alimento que não está no plano de dieta),
    você deveria imprimir a cadeia "CHEATER" (significa trapaceiro), sem
    as aspas.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de entrada contém um
    inteiro N que indica a quantidade de casos de teste. Cada caso de teste é
    composto por três linhas, cada uma delas com uma string com até 26 caracteres
    de 'A'-'Z' ou vazia, representando respectivamente os alimentos da dieta, do
    café da manhã e do almoço.

    Saída
    Para cada caso de teste imprima uma string que representa os alimentos que você
    deveria consumir no jantar, ou "CHEATER" caso você tenha trapaceado na sua dieta.
    :return:
    """
    n = int(input().strip())
    for i in range(n):
        dietas, jantar, comer, comeu, ceia, flag = [], [], [], "", "", 0
        for j in range(3):
            alimentos = input().strip()
            dietas.append(alimentos)
        for j in range(1, len(dietas)):
            for k in range(0, len(dietas[j])):
                if dietas[j][k] not in dietas[0]:
                    flag = 1
                    break
                if dietas[j][k] in dietas[0]:
                    jantar.append(dietas[j][k])
                    if jantar.count(dietas[j][k]) > dietas[0].count(dietas[j][k]):
                        flag = 1
                        break
            if flag == 1:
                print("CHEATER")
                break
        if flag == 0:
            jantar.sort()
            for j in jantar:
                comeu += j
            for j in range(0, len(dietas[0])):
                if dietas[0][j] not in comeu:
                    comer.append(dietas[0][j])
            comer.sort()
            for j in range(0, len(comer)):
                ceia += comer[j]
            print(ceia)


plano_de_dieta()

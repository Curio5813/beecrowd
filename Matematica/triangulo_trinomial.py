def triangulo_trinomial():
    """
    O triângulo trinomial é um triângulo numérico de coeficientes trinomiais.
    Ele pode ser obtido com uma linha contendo um único "1", a próxima linha
    contendo três 1 e cada elemento das linhas seguintes sendo calculado como
    a soma do elemento acima à esquerda, imediatamente acima e acima à direita:

    ![](https://resources.beecrowd.com/gallery/images/contests/tritri.png)

    A primeira linha do triângulo trinomial é numerada com zero, a segunda linha é
    a de número 1 e assim sucessivamente.

    Sua tarefa é, dado um número de linha R, escrever um programa que exiba a soma de
    seus elementos. Por exemplo, a soma dos elementos da linha 2 é 9 = 1 + 2 + 3 + 2 + 1.

    Entrada
    A entrada é o número de linha R (0 ≤ R ≤ 20).

    Saída
    A saída é a soma de todos os elementos da linha R. Não esqueça do caractere de fim-de-linha
    após exibir a soma.
    :return:
    """
    temp, triangulo, cont = [], [], 0
    r = int(input())
    if r == 0:
        triangulo = 1
        print(triangulo)
    else:
        for i in range(0, r + 1):
            if i == 0:
                temp.append(1)
                triangulo.append(temp)
                temp = []
            if i == 1:
                while cont < i + 2:
                    temp.append(i)
                    cont += 1
                triangulo.append(temp)
                temp = []
                cont = 0
            if i > 1:
                while cont < len(triangulo[i - 1]):
                    if cont == 0:
                        temp.append(1)
                    if cont == len(triangulo[i - 1]) - 1:
                        temp.append(1)
                        break
                    if cont == 1:
                        temp.append(0)
                    if cont == i:
                        temp.append(0)
                    else:
                        temp.append(0)
                    cont += 1
                triangulo.append(temp)
                temp = []
                cont = 0
        if r >= 2:
            for i in range(2, len(triangulo)):
                for j in range(1, len(triangulo[i])):
                    if j == len(triangulo[i]) - 2:
                        triangulo[i][j] = triangulo[i - 1][-1] + triangulo[i - 1][-2]
                        break
                    if j == 1:
                        triangulo[i][j] = triangulo[i - 1][0] + triangulo[i - 1][1]
                    if j > 1:
                        triangulo[i][j] = (triangulo[i - 1][j - 2] + triangulo[i - 1][j - 1] +
                                           triangulo[i - 1][j])
        soma = sum(triangulo[r])
        print(soma)


triangulo_trinomial()

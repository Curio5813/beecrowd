def coloque_tijolos_na_parede():
    """
    Não, não é "mais um tijolo na parede", é apenas um problema
    sobre somar números.

    Suponha que você tem uma parede com o formato de um triângulo,
    como a mostrada abaixo. A parede tem 9 linhas, e a i-ésima linha
    tem exatamente i tijolos, considerando que a linha mais acima é a
    1ª e que a mais abaixo é a 9ª. Alguns tijolos são rotulados com
    um número, enquanto os demais estão em branco. Os tijolos rotulados
    aparecem apenas em linhas ímpares, e ocupam posições ímpares dentro
    das suas linhas.

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_1426.png)

    O problema que você deve resolver consiste em rotular os tijolos em branco
    com números, de tal forma que a seguinte regra seja satisfeita: O número
    de um tijolo é igual à soma dos números dos dois tijolos abaixo dele.
    Obviamente, esta regra não é aplicada à 9ª linha. Todos os números devem
    ser inteiros.

    Nota: O exemplo de entrada contém dois casos de teste. O primeiro dele corresponde
    à parede mostrada acima.

    Entrada
    A primeira linha da entrada contém um inteiro N, indicando o número de casos de
    teste. Esta linha é seguida pelos casos de teste. Cada caso é descrito por 5
    linhas. Essas linhas correspondem às linhas ímpares da parede, de cima para baixo,
    como descrito acima. Cada linha contém os números nos tijolos já rotulados da linha
    correspondente na parede, da esquerda para a direita, separados por um espaço em branco.

    Você pode assumir que todo caso de teste é correto, isto é, existe uma solução
    para o problema descrito.

    Saída
    Para cada caso de teste, a saída deve ser formada por 9 linhas descrevendo os números
    de todos os tijolos da parede. Assim, a i-ésima linha deve conter os números correspondentes
    aos i tijolos da i-ésima linha da parede, da esquerda para a direita, separados por um espaço.
    :return:
    """
    n = int(input())
    for i in range(n):
        tijolos, temp = [], []
        for k in range(9):
            if k % 2 == 0:
                tijolo = list(map(int, input().split(" ")))
                if k == 0:
                    tijolos.append(tijolo)
                if k > 0:
                    for j in range(k + 1):
                        if j % 2 != 0:
                            tijolo.insert(j, 0)
                    tijolos.append(tijolo)
            if k % 2 == 1:
                for j in range(k + 1):
                    if j >= 8:
                        break
                    temp.append(0)
                tijolos.append(temp)
                temp = []
        for k in range(0, len(tijolos)):
            for j in range(0, len(tijolos[k]), 2):
                if k % 2 == 0 and k > 0:
                    if j > k - 2:
                        break
                    tijolos[k][j + 1] = int((tijolos[k - 2][j] - (tijolos[k][j] + tijolos[k][j + 2])) / 2)
                    tijolos[k - 1][j] = tijolos[k][j] + tijolos[k][j + 1]
                    tijolos[k - 1][j + 1] = tijolos[k][j + 1] + tijolos[k][j + 2]
        for k in range(0, len(tijolos)):
            print(*tijolos[k])


coloque_tijolos_na_parede()

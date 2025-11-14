def elevador_2():
    """
    Uma fábrica instalou um elevador composto de duas cabines ligadas
    por uma roldana, como na figura. Quando uma cabine sobe, a outra desce.
    No primeiro andar da fábrica existem algumas caixas de pesos diversos
    e precisamos levar todas as caixas para o segundo andar, usando o elevador.
    Apenas uma caixa pode ser colocada por vez dentro de uma cabine. Além disso,
    existe uma restrição de segurança importante: durante uma viagem do elevador,
    a diferença de peso entre as cabines pode ser no máximo de 8 unidades. De
    forma mais rigorosa, P − Q ≤ 8, onde P é o peso da cabine mais pesada e Q,
    o peso da cabine mais leve. O gerente da fábrica não está preocupado com o
    número de viagens que o elevador vai fazer. Ele apenas precisa saber se é
    possível ou não levar todas as caixas para o segundo andar. No exemplo da
    figura, podemos levar todas as três caixas usando a seguinte sequência de
    seis viagens do elevador:

    Sobe a caixa de peso 4, desce a outra cabine vazia; (diferença de 4)
    Sobe a caixa de peso 10, desce a caixa de peso 4; (diferença de 6)
    Sobe a caixa de peso 15, desce a caixa de peso 10; (diferença de 5)
    Sobe a caixa de peso 4, desce a outra cabine vazia; (diferença de 4)
    Sobe a caixa de peso 10, desce a caixa de peso 4; (diferença de 6)
    Sobe a caixa de peso 4, desce a outra cabine vazia. (diferença de 4)
    Dados os pesos de N caixas no primeiro andar, seu programa deve dizer se é
    possível ou não levar todas as N caixas para o segundo andar.

    [imagem] (https://resources.beecrowd.com/gallery/images/problems/UOJ_2835.png)

    Entrada
    A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 104) indicando o número
    de caixas. A segunda linha da entrada contém N inteiros representando os pesos
    das caixas. O peso das caixas está entre 1 e 105 , inclusive.

    Saída
    Imprima uma linha na saída. A linha deve conter o caracter S caso seja possível,
    ou N caso não seja possível levar todas as caixas até o segundo andar da fábrica.
    :return:
    """
    n = int(input())
    caixas = sorted(list(map(int, input().split())))
    flag = True
    for i in range(0, len(caixas)):
        for j in range(i + 1, len(caixas)):
            if i == 0 and caixas[i] > 8:
                flag = False
                break
            if caixas[j] - caixas[i] > 8:
                flag = False
                break
            if caixas[j] - caixas[i] <= 8:
                break
        if not flag:
            print("N")
            break
    if flag:
        print("S")


if __name__ == '__main__':
    elevador_2()

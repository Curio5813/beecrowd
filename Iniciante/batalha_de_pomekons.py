def main():
    """
    Depois de capturar muitos Pomekons, Dabriel e Guarte resolveram batalhar. A forma de
    duelo é simples, cada treinador coloca um Pomekon na batalha e vence quem tem o
    Pomekon com maior valor de golpe, que é definido da seguinte maneira:


                ValorGolpe = (Ataque + Defesa) / 2  + Bonus


    O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par.

    Neste problema será dado a você o valor do bônus aplicado, os valores de ataque e
    defesa do Pomekon de Dabriel e Guarte e seus respectivos níveis, cabe a você informar
    o ganhador da batalha.

    Entrada
    A entrada é composta por diversas instâncias. A primeira linha da entrada contém um
    inteiro T indicando o número de instâncias. Cada instância começa com um inteiro B
    (0 ≤ B ≤ 100), que indica o valor do bônus aplicado. Nas duas linhas seguintes terão
    três inteiros Ai, Di e Li (1 ≤ Ai, Di ≤ 100, 1 ≤ Li ≤ 50), representado o valor de
    ataque do Pomekon, o valor de defesa e o level do treinador. A primeira linha representa
    o Pomekon de Dabriel e a segunda o de Guarte.

    Saída
    Para instância na entrada você deverá imprimir o nome do treinador que irá vencer a
    batalha, em caso de empate imprima: "Empate", sem aspas.
    """
    t = int(input())
    for k in range(t):
        b = int(input())
        a1, d1, l1 = input().split()
        a1, d1, l1 = int(a1), int(d1), int(l1)
        a2, d2, l2 = input().split()
        a2, d2, l2 = int(a2), int(d2), int(l2)
        valorgolpe1 = (a1 + d1) / 2
        if l1 % 2 == 0:
            valorgolpe1 += b
        valorgolpe2 = (a2 + d2) / 2
        if l2 % 2 == 0:
            valorgolpe2 += b
        if valorgolpe1 > valorgolpe2:
            print('Dabriel')
        elif valorgolpe2 > valorgolpe1:
            print('Guarte')
        elif valorgolpe1 == valorgolpe2:
            print('Empate')


if __name__ == '__main__':
    main()

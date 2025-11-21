def museu_virtual_3d():
    """
    Vasya e Petya estão visitando o museu virtual 3D da história da capital
    da Nlogônia. No meio de tanta diversão, decidiram pregar uma peça. A peça
    consiste em danificar M modelos dentre os N expostos. Vasya baixa ilegalmente
    o arquivo do modelo, Petya o abre em um editor 3D e subtitui detalhes
    históricos por números na sequência de Fibonacci, e o coloca de volta no museu.

    Toda vez que um modelo é danificado, seu valor se torna nulo. Como a dupla é
    extremamente malvada, decidiram causar o maior dano possível. Dados N, M e o
    valor de todas os modelos expostos, faça um programa que calcule o maior prejuízo
    que pode ser causado.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de cada caso contém dois
    número inteiros, N (0 ≤ N ≤ 103) e M (0 ≤ M ≤ N), respectivamente. A segunda linha
    contém N inteiros (entre 0 e 1000), os valores de cada modelo (em dólares nlogônios),
    em ordem não decrescente.

    A entrada termina com fim-de-arquivo (EOF).

    Saída
    Para cada caso de teste, imprima uma linha com um único número indicando o maior prejuízo
    a ser causado.
    :return:
    """
    while True:
        try:
            n, m = map(int, input().split())
            valores_modelos = list(map(int, input().split()))
            valores_modelos.reverse()
            a, b, p = 0, 1, 1
            fibonacci = []
            for i in range(1001):
                fibonacci.append(a)
                if a > 1000:
                    break
                a = b
                b = p
                p = a + b
            valor_total, cont = 0, 0
            fibonacci.reverse()
            while True:
                for i in range(len(valores_modelos)):
                    if valores_modelos[i] in fibonacci:
                        valor_total += valores_modelos[i]
                        valores_modelos[i] = 0
                        cont += 1
                        if cont == m:
                            break
                if cont == m:
                    break
            print(valor_total)
        except EOFError:
            break


if __name__ == '__main__':
    museu_virtual_3d()


"""
4 2
0 0 2 3
7 1
33 44 55 789 790 791 987
5 2
4 7 55 55 56
"""
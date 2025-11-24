def qual_e_a_altura():
    """
    Nick é um cientista que viaja por diversos universos paralelos,
    juntamente com o seu neto, Mory. Em um desses universos, havia
    um programa de televisão, que premiava quem adivinhasse as alturas
    máximas de arremessos de frutas. Neste local, a massa da fruta não
    influenciava na altura máxima do arremesso. Nick calculava o ângulo
    do arremesso, que formava sempre uma parábola, e extraía uma função
    de segundo grau da trajetória. Ajude Nick e Mory a ganhar muitos
    prêmios neste programa.

    Entrada
    A entrada é composta por vários casos de teste. A primeira linha contém
    um número inteiro T (2 <= T <= 99) relativo ao número de casos de teste.
    As T linhas seguintes possuem três valores inteiros A (A < 0), B e C
    (-100 <= B, C <= 100), representando os coeficientes de uma função de segundo
    grau, na forma ax2 + bx + c.

    Saída
    Para cada caso de teste de entrada do seu programa, você deve imprimir um
    número real, com aproximação de duas casas decimais, a altura máxima do
    arremesso de uma fruta.
    :return:
    """
    n = int(input())
    while n > 0:
        a, b, c = map(int, input().split())
        x = -b / (2 * a)
        y = a * x ** 2 + b * x + c
        print(f"{y:.2f}")
        n -= 1


if __name__ == '__main__':
    qual_e_a_altura()

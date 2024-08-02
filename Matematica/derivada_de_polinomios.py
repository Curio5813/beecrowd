def derivada_de_polinomios():
    """
    A fórmula de cálculo de uma derivada de uma função na forma xn é definida por:

    f(x) = xn    →     f(x)’ = n.xn-1

    Veja um exemplo:

    f(x) = 4x3 + 3x2    →     f(x)’ = 12x2 + 6x

    Escreva um programa que, dado um polinômio simples, calcule a sua derivada.

    Entrada
    Haverá diversos casos de teste. Cada caso de teste é formado por um número inteiro
    T, que representa a quantidade de termos que o polinômio possui. Na linha seguinte,
    há o polinômio propriamente dito, formado por T (1 ≤ T ≤ 100) termos, todos separados
    por um espaço, um sinal de soma e outro espaço, e cada um contendo um inteiro
    C (2 ≤ C ≤ 100), a letra x e um inteiro E (2 ≤ E ≤ 100), sendo C o coeficiente e E o
    expoente do termo. A entrada termina com fim de arquivo.

    Saída
    Para cada caso de teste, imprima o polinômio com a derivada aplicada.
    :return:
    """
    while True:
        try:
            t = int(input())
            numeros, derivada = [], ""
            termos = list(input().split(" "))
            for i in range(0, len(termos)):
                if i >= len(termos) - 1:
                    numeros = list((map(int, (termos[i].split("x")))))
                    coeficiente = numeros[0] * numeros[1]
                    potencia = numeros[1] - 1
                    if potencia == 1:
                        potencia = ""
                    derivada += str(coeficiente) + "x" + str(potencia)
                    break
                if termos[i] != "+":
                    numeros = list((map(int, (termos[i].split("x")))))
                    coeficiente = numeros[0] * numeros[1]
                    potencia = numeros[1] - 1
                    if potencia == 1:
                        potencia = ""
                    derivada += str(coeficiente) + "x" + str(potencia) + " + "
            print(derivada)
        except EOFError:
            break


derivada_de_polinomios()

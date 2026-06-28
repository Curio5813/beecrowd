from math import lcm


def soma_de_fracoes():
    """
    Joãozinho está aprendendo a somar frações na escola e quer sua ajuda
    para escrever um programa que dadas duas frações imprima a soma delas
    em sua forma irredutível. Assim ele vai poder conferir as respostas
    dos exercícios que está fazendo.

    A forma irredutível de uma fração é quando o divisor (número de baixo) é
    o menor possível. Por exemplo, 10⁄3 é uma fração irredutível, pois 10 e 3
    não têm nenhum divisor em comum. Mas 10⁄6 não é, pois ela pode ser simplificada
    para 5⁄3, dividindo-se 10 e 6 por 2.

    Dados quatro inteiros a, b, c, d, escreva um programa que calcule a⁄b + c⁄d
    na sua forma irredutível.

    Entrada
    A única linha da entrada contém quatro inteiros a, b, c, d, (1 ≤ a, b, c, d ≤ 100)
    respectivamente dividendo e divisor da primeira fração e dividendo e divisor da segunda
     fração.

    Saída
    Seu programa deve imprimir uma única linha contendo dois inteiros, dividendo e divisor
    da fração irredutível formada pela soma das duas frações dadas.
    :return:
    """
    numeros = list(map(int, input().split(" ")))
    denominador_comum = lcm(numeros[1], numeros[3])
    numerador1 = numeros[0] * (denominador_comum / numeros[1])
    numerador2 = numeros[2] * (denominador_comum / numeros[3])
    numerador = int(numerador1 + numerador2)
    for i in range(2, denominador_comum + 1):
        while numerador % i == 0 and denominador_comum % i == 0:
            numerador //= i
            denominador_comum //= i
    print(int(numerador), int(denominador_comum))


soma_de_fracoes()

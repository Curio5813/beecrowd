def sequencia_espelho():
    """
    Imprimir números em sequência é uma tarefa relativamente
    simples. Mas, e quando se trata de uma sequência espelho?
    Trata-se de uma sequência que possui um número de início e
    um número de fim, e todos os números entre estes, inclusive
    estes, são dispostos em uma sequência crescente, sem espaços
    e, em seguida, esta sequência é projetada de forma invertida,
    como um reflexo no espelho. Por exemplo, se a sequência for de
    7 a 12, o resultado ficaria 789101112211101987

    Escreva um programa que, dados dois números inteiros, imprima a
    respectiva sequência espelho.

    Entrada
    A entrada possui um valor inteiro C indicando a quantidade de
    casos de teste. Em seguida, cada caso apresenta dois valores
    inteiros, B e E (1 ≤ B ≤ E ≤ 12221), indicando o início e o fim
    da sequência.

    Saída
    Para cada caso de teste, imprima a sequência espelho correspondente.
    :return:
    """
    c = int(input())
    for i in range(c):
        str_numero = ""
        b, e = map(int, input().split(" "))
        for j in range(b, e + 1):
            if j <= e + 1:
                str_numero += str(j)
        reverso = str_numero[::-1]
        str_numero += reverso
        print(str_numero)


sequencia_espelho()

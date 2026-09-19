from math import sqrt


def quantos_primos():
    """
    JoãoPin é seu amigo e sabe que você é apaixonado por números primos
    e entende muitas propriedades sobre eles. Recentemente ele te mandou
    um desafio por e-mail com N perguntas do tipo: Quantos números primos
    existem no intervalo [A, B] (inclusive)?

    Exemplo: Seja A = 3 e B = 11, existem 4 números primos no intervalo [3, 11],
    são eles: 3, 5, 7 e 11.

    JoãoPin prometeu te presentear com um pacote de bolachinhas de goiaba, caso
    você acerte todas as N perguntas.

    Com isso, sua tarefa neste exercício é simples, acertar todas as perguntas para
    ganhar o prêmio que você tanto gosta.

    Atenção: Lembre-se que os números primos são números naturais maiores que 1 que
    possuem apenas dois divisores, 1 e ele mesmo.


    Entrada
    A primeira linha de entrada contém o inteiro N (1 ≤ N ≤ 104), indicando quantas
    perguntas JoãoPin te fez.

    Cada uma das próximas N linhas representa uma pergunta feita pelo seu amigo e contém
    os inteiros A e B (1 ≤ A ≤ B ≤ 107).


    Saída
    Para cada pergunta feita por JoãoPin, responda corretamente a quantidade de números
    primos existentes no intervalo [A, B] (inclusive).

    OBS: Existem 16 números primos no intervalo [1000, 1100], são eles: 1009, 1013, 1019,
    1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097.
    :return:
    """

    perguntas = int(input())
    for i in range(perguntas):
        entrada = list(map(int, input().split()))
        num1 = entrada[0]
        num2 = entrada[1]
        cont, a = 0, 2
        for j in range(num1, num2 + 1):
            limite = int(sqrt(j))
            for k in range(a, limite + 1):
                if j % k == 0 and j != k:
                    a = 2
                    break
            else:
                cont += 1
        print(cont)


quantos_primos()

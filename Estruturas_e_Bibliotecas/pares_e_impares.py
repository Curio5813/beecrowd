def pares_e_impares():
    """
    Considerando a entrada de valores inteiros não negativos, ordene estes
    valores segundo o seguinte critério:

    Primeiro os Pares
    Depois os Ímpares
    Sendo que deverão ser apresentados os pares em ordem crescente e depois
    os ímpares em ordem decrescente.

    Entrada
    A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 10^5)
    Este é o número de linhas de entrada que vem logo a seguir. As próximas N
    linhas conterão, cada uma delas, um valor inteiro não negativo.

    Saída
    Apresente todos os valores lidos na entrada segundo a ordem apresentada acima.
    Cada número deve ser impresso em uma linha, conforme exemplo abaix
    :return:
    """
    n = int(input())
    numeros, pares, impares = [], [], []
    for i in range(n):
        numero = int(input())
        numeros.append(numero)
    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            pares.append(numeros[i])
        if numeros[i] % 2 == 1:
            impares.append(numeros[i])
    pares.sort()
    impares.sort()
    impares.reverse()
    for i in range(len(pares)):
        print(pares[i])
    for i in range(len(impares)):
        print(impares[i])


if __name__ == '__main__':
    pares_e_impares()

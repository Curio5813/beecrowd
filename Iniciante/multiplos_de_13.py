def main():
    """
    Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos
    de 13 entre X e Y, incluindo ambos.
    """
    cont = 0
    x = int(input())
    y = int(input())
    if x >= y:
        for k in range(y, x + 1):
            if k % 13 != 0:
                cont += k
    elif x <= y:
        for k in range(x, y + 1):
            if k % 13 != 0:
                cont += k
    print(cont)


if __name__ == '__main__':
    main()

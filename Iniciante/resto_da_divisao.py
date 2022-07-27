def main():
    """
    Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da
    divisão dele por 5 for igual a 2 ou igual a 3.
    """
    x = int(input())
    y = int(input())
    if x > y:
        for k in range(y + 1, x):
            if k % 5 == 2 or k % 5 == 3:
                print(k)
    elif y > x:
        for k in range(x + 1, y):
            if k % 5 == 2 or k % 5 == 3:
                print(k)


if __name__ == '__main__':
    main()

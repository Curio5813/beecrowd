def main():
    """
    Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
    teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada
    para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor
    tem peso 3 e o terceiro valor tem peso 5.
    """
    medias, a = [], 0
    n = int(input())
    while a < n:
        n1, n2, n3 = input().split(' ')
        n1, n2, n3, = float(n1), float(n2), float(n3)
        media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
        medias.append(media)
        a += 1
    for k in range(0, len(medias)):
        print(f'{medias[k]:.1f}')


if __name__ == '__main__':
    main()

def main():
    """
    Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
    """
    numeros = []
    for k in range(0, 100):
        num = int(input())
        numeros.append(num)
    print(f'{max(numeros)}\n'
          f'{numeros.index(max(numeros)) + 1}')


if __name__ == '__main__':
    main()

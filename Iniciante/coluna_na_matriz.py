def main():
    """
    Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação
    deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos
    os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos
    que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada
    do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser considerados na
    operação.
    """
    matriz, soma = [], 0
    c = int(input())
    t = input().upper()
    for linha in range(12):
        for coluna in range(12):
            valor = float(input())
            matriz.append(valor)
    if t == 'S':
        for k in range(c, len(matriz), 12):
            soma += matriz[k]
        print(f'{soma:.1f}')
    elif t == 'M':
        for k in range(c, len(matriz), 12):
            soma += matriz[k]
        print(f'{(soma / 12):.1f}')


if __name__ == '__main__':
    main()

def main():
    """
     Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação
     deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos
     os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos
     elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o
     caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser
     considerados na operação.
    """
    val, soma = [], 0
    lin = int(input())
    t = input().upper()
    for linha in range(12):
        for coluna in range(12):
            valor = float(input())
            val.append(valor)
    if t == 'S':
        for k in range(lin * 12, lin * 12 + 12):
            soma += val[k]
        print(f'{soma:.1f}')
    elif t == 'M':
        for k in range(lin * 12, lin * 12 + 12):
            soma += val[k]
        print(f'{(soma / 12):.1f}')


if __name__ == '__main__':
    main()

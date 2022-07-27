def main():
    """
    Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores
    positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito,
    pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito
    ou não.
    """
    casos, y, divisores = 0, 1, []
    n = int(input())
    while casos < n:
        x = int(input())
        while y < x:
            if x % y == 0:
                divisores.append(y)
            y += 1
        if sum(divisores) == x:
            print(f'{x} eh perfeito')
        else:
            print(f'{x} nao eh perfeito')
        divisores = []
        y = 1
        casos += 1


if __name__ == '__main__':
    main()

def main():
    """
    Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos
    para Cino resolver. Desta vez, Bino gerou uma lista de números e perguntou ao
    Cino quantos números da lista são múltiplos de 2, 3, 4 e 5.

    Esse desafio pode parecer simples, porém, quando a lista contém muitos números,
    Cino se confunde e acaba errando alguns cálculos. Para ajudar Cino, faça um programa
    para resolver o desafio de Bino.

    Entrada
    A primeira linha da entrada consiste em um inteiro N (1 ≤ N ≤1000), representando
    a quantidade de números na lista de Bino.

    A segunda linha contém N inteiros Li (1 ≤ Li ≤ 100), representando os números da
    lista de Bino.

    Saída
    Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista.
    Observe a formatação da saída nos exemplos, pois ela deve ser seguida rigorosamente.
    """
    n2, n3, n4, n5 = 0, 0, 0, 0
    n = int(input())
    lista = [int(x) for x in input().split()]
    for k in range(0, len(lista)):
        if lista[k] % 2 == 0:
            n2 += 1
        if lista[k] % 3 == 0:
            n3 += 1
        if lista[k] % 4 == 0:
            n4 += 1
        if lista[k] % 5 == 0:
            n5 += 1
    print(f'{n2} Multiplo(s) de 2\n'
          f'{n3} Multiplo(s) de 3\n'
          f'{n4} Multiplo(s) de 4\n'
          f'{n5} Multiplo(s) de 5')


if __name__ == '__main__':
    main()

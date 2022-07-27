def main():
    from statistics import mean
    """
    Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo.
    O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a 
    idade média deste grupo de indivíduos.
    """
    lista = []
    idade = int(input())
    while idade >= 0:
        lista.append(idade)
        idade = int(input())
    print(f'{mean(lista):.2f}')


if __name__ == '__main__':
    main()

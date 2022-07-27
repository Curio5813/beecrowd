def main():
    """
    O MacPRONALTS está com uma super promoção, exclusivo para os competidores da
    primeira Seletiva do MaratonaTEC. Só que teve um problema, todos os maratonistas
    foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande. O pior
    é que a moça do caixa estava sem calculadora ou um programa para ajudá-la a calcular
    com maior agilidade, eis que surge você para fazer um programa para ajudar a coitada
    e aumentar a renda do MacPRONALTS. Segue o cardápio do dia contendo o número do
    produto e seu respectivo valor.

    1001 | R$ 1.50

    1002 | R$ 2.50

    1003 | R$ 3.50

    1004 | R$ 4.50

    1005 | R$ 5.50

    Entrada
    A primeira entrada informada é a quantidade de produtos comprados (1 <= p <= 5).
    Para cada produto segue a quantidade (1 <= q <= 500) que o consumidor comprou.

    Obs.: não poderão ser informados números de produtos repetidos.

    Saída
    Você deve imprimir o valor da compra com duas casas decimais.
    """
    codes, prices, value = [1001, 1002, 1003, 1004, 1005], [1.50, 2.50, 3.50, 4.50, 5.50], 0
    n = int(input())
    for k in range(0, n):
        order = [int(x) for x in input().split()]
        if order[0] == codes[0]:
            value += prices[0] * order[1]
        elif order[0] == codes[1]:
            value += prices[1] * order[1]
        elif order[0] == codes[2]:
            value += prices[2] * order[1]
        elif order[0] == codes[3]:
            value += prices[3] * order[1]
        elif order[0] == codes[4]:
            value += prices[4] * order[1]
    print(f'{value:.2f}')


if __name__ == '__main__':
    main()

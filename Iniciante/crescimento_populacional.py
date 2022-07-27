def main():
    """
    Mariazinha quer resolver um problema interessante. Dadas as informações de população e a taxa de
    crescimento de duas cidades quaisquer (A e B), ela gostaria de saber quantos anos levará para que
    a cidade menor (sempre é a cidade A) ultrapasse a cidade B em população. Claro que ela quer saber
    apenas para as cidades cuja taxa de crescimento da cidade A é maior do que a taxa de crescimento
    da cidade B, portanto, previamente já separou para você apenas os casos de teste que tem a taxa de
    crescimento maior para a cidade A. Sua tarefa é construir um programa que apresente o tempo em anos
    para cada caso de teste.
    Porém, em alguns casos o tempo pode ser muito grande, e Mariazinha não se interessa em saber exatamente
    o tempo para estes casos. Basta que você informe, nesta situação, a mensagem "Mais de 1 seculo.".
    """
    n = 0
    t = int(input())
    for k in range(0, t):
        pa, pb, g1, g2 = input().split(' ')
        pa, pb, g1, g2 = int(pa), int(pb), float(g1), float(g2)
        while pa <= pb:
            pa += int((pa * (g1 / 100)))
            pb += int((pb * (g2 / 100)))
            n += 1
            if n > 100:
                print('Mais de 1 seculo.')
                break
        if n <= 100:
            print(f'{n} anos.')
        n = 0


if __name__ == '__main__':
    main()

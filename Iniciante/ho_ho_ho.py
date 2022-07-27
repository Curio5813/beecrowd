def main():
    """
    Papai Noel está brincando com seus duendes para entretê-los durante a véspera do Natal.
    A brincadeira consiste nos elfos escreverem números em pedaços de papel e colocarem no
    gorro do Papai Noel. Após todos terminarem de colocar os números Noel sorteia um papel
    e aquele número representa quantos "Ho" o Noel deve falar.

    Seu trabalho é ajudar o Papai Noel montando um problema que mostre todos os "Ho" que ele
    deve falar dado o número sorteado.
    """
    n = int(input())
    print(f'Ho ' * (n - 1) + 'Ho!')


if __name__ == '__main__':
    main()

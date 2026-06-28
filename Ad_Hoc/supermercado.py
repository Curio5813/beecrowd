def supermercado():
    """
    Maria está participando de um programa de intercâmbio no reino
    da Nlogônia. Ela está gostando muito da experiência, e decidiu
    fazer um churrasco para suas novas amigas da escola. Como não
    tem muito dinheiro, Maria vai fazer uma pesquisa para comprar
    carne no supermercado mais barato que encontrar.

    No entanto ela está um pouco confusa para saber qual supermercado
    tem o menor preço. O dinheiro na Nlogônia é o Bit, abreviado por B$,
    mas não é esse o problema. O problema é que o costume na Nlogônia é
    informar o preço de uma maneira diferente do que Maria está acostumada.
    Os preços são anunciados como “X Bits por Y gramas do produto”.

    Por exemplo o preço de um dado produto é anunciado como sendo B$ 24,00 por
    250 gramas em um supermercado, B$ 16,00 por 100 gramas em outro supermercado,
    B$ 19,00 por 120 gramas em outro supermercado, e assim por diante.

    Você pode ajudar Maria? Dados os preços anunciados pelos supermercados no bairro
    em que Maria mora, determine o menor valor que Maria deve gastar para comprar
    1 kilograma (1000 gramas) de carne.

    Entrada
    A primeira linha contém um número inteiro N, o número de supermercados próximos
    à casa de Maria. Cada uma das N linhas seguintes indica o preço da carne em um
    supermercado e contém um número real P e um número inteiro G, indicando que G
    gramas de carne custam P Bits.

    Saída
    Seu programa deve produzir uma única linha, com apenas um número real, o menor
    preço para comprar 1 kilograma de carne. O resultado deve ser escrito com exatamente
    dois dígitos após o ponto decimal.

    Restrições

    • 1 ≤ N ≤ 100

    • 0 < P ≤ 1000.00, representado com dois dígitos após o ponto decimal.

    • 1 ≤ G ≤ 1000
    :return:
    """
    n = int(input())
    precos = []
    for i in range(n):
        p, g = input().split(" ")
        p, g = float(p), int(g)
        preco = (p / g) * 1000
        precos.append(preco)
    print(f"{min(precos):.2f}")


supermercado()

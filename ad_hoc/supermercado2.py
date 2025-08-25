def supermercado2():
    """
    Sr. Jones é um marido exemplar. Todo sábado de manhã a Sra. Jones
    lhe dá uma lista de itens a serem comprados no supermercado e ele
    compra exatamente o que lhe foi pedido, sempre escolhendo as marcas
    com os menores preços. Mas Sr. Jones odeia ir ao mercado nos sábados,
    visto que seus corredores estão lotados de carregadores. Ele deseja
    mudar o jeito com que ele faz compras. Ao invés de ir para lá e para
    cá para comprar os produtos na lista de sua esposa, ele vai tentar
    comprar os itens passando apenas uma vez por cada corredor, pegando
    os produtos na ordem exata dada na lista. Então ele pediu a você para
    escrever um programa que o ajude com seu novo estilo de fazer compras.

    Dada as informações sobre os produtos disponíveis no supermercado junto
    com seus preços na ordem em que aparecem na lista de Sr. Jones e a lista
    de produtos dada pela sua mulher, seu programa deve determinar o menor
    preço que ele pagaria.

    Sr. Jones compra os produtos na ordem em que eles aparecem em sua lista e
    ele nunca volta atrás enquanto anda pelos corredores. Portanto, se ele
    compra o i-ésimo produto no seu caminho para o j-ésimo item da lista, o próximo
    produto a ser comprado é o (j+1)-ésimo item da lista – e deve ser comprado dos
    produtos que vem depois de i em seu caminho. A figura abaixo mostra um exemplo
    onde produtos são identificados por inteiros. Note que diferentes marcas do mesmo
    produto poder aparecer separadamente. No exemplo Sr. Jones deve comprar os
    produtos 1, 1, 2, 20 (note que o produto 1 aparece duas vezes na lista). Para o
    exemplo, o custo mínimo que Sr. Jones pode conseguir, seguindo suas limitações,
    é 21.30. Note também que com esse novo estilo de fazer comprar pode ser impossível
    para Sr. Jones comprar todos os itens da sua lista; neste caso, seu programa deve
    alertar Sr. Jones.

    [imagem](https://resources.beecrowd.com/gallery/images/novos/Supermarket.png)


    (a) Lista da Sra. Jones   (b) Lista de produtos com seus respectivos preços e ordem
    em que aparecem na direção de Sr. Jones pelos corredores.

    Entrada
    Seu programa deverá processar dados para diversos casos de teste (sessões de compra). A
    primeira linha na descrição de uma sessão de compra contém dois inteiros M e N; M indica
    o número de itens na lista da Sra. Jones (1 ≤ M ≤ 100) e N representa o número total de
    produtos disponíveis no supermercado (1 ≤ N ≤ 100,000). A próxima linha contém M inteiros
    Xi, representando a lista de produtos da lista da Sra. Jones (1 < Xi ≤ 100000, 1 ≤ i ≤ M).
    Seguem N linhas, representando os produtos do supermercado na ordem em que eles aparecem
    no caminho do Sr. Jones. Cada uma destas linhas contém um inteiro K e um número real P,
    que representam, respectivamente, um identificador de produto e seu preço (1 ≤ K ≤ 100,000).
    O fim da entrada é indicado por M = N = 0.

    Para cada sessão de compra da entrada, seu programa deve produzir uma linha de saída,  contendo
    o menor custo que Sr. Jones pode conseguir. Se não é possível comprar todos os itens da sessão,
    imprima “Impossible”. O custo deve ser impresso como um número real com precisão de duas casas
    decimais, e o último dígito decimal deve ser arredondado. A entrada não vai conter casos de teste
    onde diferenças de arredondamento são significantes.
    :return:
    """
    entrada = list(map(int, input().strip().split()))
    m, n = entrada[0], entrada[1]
    while m != 0 and n != 0:
        lista_compra = list(map(int, input().strip().split()))
        corredor_supermercado, preco, maior, montante, montantes, usados = [], [], 0, 0, [], []
        for i in range(n):
            supermercado = list(input().strip().split())
            corredor_supermercado.append(int(supermercado[0]))
            preco.append(float(supermercado[1]))
        for i in range(n):
            j = 0
            for k in range(i, n):
                if corredor_supermercado[k] == lista_compra[j]:
                    if preco[k] < maior and lista_compra[j] == usados[-1]:
                        montante -= maior
                        maior = preco[k]
                        montante += maior
                        usados.append(lista_compra[j])
                    else:
                        maior = preco[k]
                        montante += preco[k]
                        usados.append(lista_compra[j])
                        j += 1
                        if j == len(lista_compra):
                            j -= 1
            if montante > 0 and j >= len(lista_compra) - 1 and list(set(usados)) == list(set(lista_compra)):
                montantes.append(montante)
            montante = 0
            maior = 0
        if len(montantes) > 0:
            print(f'{min(montantes):.2f}')
        else:
            print("Impossible")
        entrada = list(map(int, input().strip().split()))
        m, n = entrada[0], entrada[1]


supermercado2()


"""
4 8
1 1 2 20
2 0.29
1 0.30
20 0.15
1 1.00
1 0.05
2 10.00
20 20.00
20 10.00
"""

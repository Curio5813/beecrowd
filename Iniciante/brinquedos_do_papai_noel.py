def brinquedos_do_papai_noel():
    """
    Papai Noel todo ano lê as cartinhas de Natal para saber o
    que dar de presente para cada criança. O problema é que
    muitas crianças não mandam suas cartinhas para o Papai Noel.
    Então ele decidiu que, para poupar o seu tempo, ele irá dar
    o mesmo presente para crianças que não mandaram cartinhas.
    Assim, ele decidiu que para os meninos ele irá dar um carrinho
    de brinquedo e para as meninas, uma boneca. A entrada a primeira
    linha possui um inteiro N (0 < N ≤ 1000), o número de crianças
    que não enviaram sua cartinha para o Papai Noel. As próximas
    N linhas consistem em duas strings, a primeira é o nome da
    criança, e a segunda é uma letra, que pode ser ‘M’, para dizer
    que é um menino, ou ‘F’ se for uma menina. A saída consiste em
    2 linhas. A primeira linha deve conter o número de carrinhos que
    o papai noel deve fazer, seguido pela palavra “carrinhos”, e na
    segunda linha, o número de bonecas seguido pela palavra “bonecas”.
    :return:
    """
    n = int(input())
    carrinhos, bonecas = 0, 0
    for i in range(n):
        crianca = input().split(" ")
        if crianca[1] == "M":
            carrinhos += 1
        elif crianca[1] == "F":
            bonecas += 1
    print(f"{carrinhos} carrinhos")
    print(f"{bonecas} bonecas")


brinquedos_do_papai_noel()

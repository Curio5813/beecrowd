def indecisao_das_renas():
    """
    Esta função printa uma string que é o nome da rena que
    deve ser a primeira entre elas a puxar o trenó de Papai
    Noel depois que a última bola neve, que elas fizeram,
    ficar com a rena vencedora.
    :return:
    """
    renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]
    a = list(map(int, input().split()))
    soma = sum(a)
    while soma > 9:
        soma -= 9
    print(renas[soma - 1])


indecisao_das_renas()

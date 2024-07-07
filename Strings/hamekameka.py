def hamekameka():
    """
    O Hamekameka foi inventado por Mestre Hame praticado por cinquenta anos
    antes de conhecer Kogu. Chamando sua energia latente nas palmas de suas
    mãos, Hame consegue lançar um raio explosivo de energia. Kogu aprende
    após ver Mestre Hame usando-o para apagar as chamas na casa de um Rei.
    Para a surpresa de Hame, Kogu consegue performar a técnica de primeira,
    embora seja apenas forte o suficiente para destruir o carro que Chamya
    deu para Mulba. Kogu descobriu que há um padrão na pronúncia correta
    deste ataque, de modo que, se não for pronunciado corretamente, o mesmo
    não acontece.

    Escreva um programa que, dada a parte inicial de um Hamekameka, faça a
    finalização ideal para que o ataque seja realizado com sucesso.

    Entrada
    A entrada começa com um valor C, indicando a quantidade de casos de teste.
    Em seguida, temos C linhas, cada uma com o início de um ataque, com, no máximo,
    200 letras.

    Saída
    Para cada caso de teste, imprima a finalização adequada, para que o ataque se
    concretize.
    :return:
    """
    c = int(input())
    for i in range(c):
        cont, a = 0, ""
        ataque = input()
        ataques, flag = [], 1
        for j in ataque:
            if j == "a":
                cont += 1
                flag = 0
            else:
                if flag == 0:
                    ataques.append(cont)
                    cont = 0
                    flag = 1
        qtd = ataques[0] * ataques[1]
        while len(a) < qtd:
            a += "a"
        print(f"k{a}")


hamekameka()

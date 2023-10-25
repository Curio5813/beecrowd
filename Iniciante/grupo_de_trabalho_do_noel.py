def grupo_de_trabalho_do_noel():
    """
    Todo ano, Papai Noel faz o recrutamento de elfos e gnomos para a
    sua equipe de preparação natalina. O setor de sua produção que mais
    tem alterações ao longo do ano é o da fabricação dos presentes, pois
    ele contrata elfos temporários, que trabalham uma determinada quantidade
    de horas H com ele. Além disso, cada elfo é contratado para um dos 4
    diferentes grupos de trabalho, onde cada um dos grupos possui uma quantidade
    de horas para produzir os presentes do tipo do grupo:

    Grupo dos bonecos: 8 horas;
    Grupo dos arquitetos: 4 horas;
    Grupo dos musicos: 6 horas;
    Grupo dos desenhistas: 12 horas.

    Note que os trabalhadores do grupo dos bonecos só produzem bonecos, o dos
    arquitetos, casas, e assim sucessivamente. Mas cada tipo de presente conta como
    um presente completo no final do dia. O Papai Noel possui uma lista dos nomes
    dos elfos escolhidos esse ano, com a quantidade de horas e em que grupo que eles
    podem trabalhar. Sabendo da sua habilidade com programação, o Noel quer uma forcinha
    sua para dizer para ele quantos presentes ele vai conseguir ter pronto, por dia,
    de acordo com a quantidade de elfos que ele contratou.

    A entrada consite é um valor inteiro N (1 ≤ N ≤ 1000), indicando a quantidade
    de elfos que o Papai Noel contratou. As N linhas seguintes possuem três valores
    E, G e H (1 ≤ H ≤ 24), indicando respectivamente o nome do elfo, em qual grupo
    ele vai trabalhar (em letras minúsculas) e quantas horas por dia ele irá ajudar
    (em valor inteiro). A saída deverá ser um inteiro P, a quantidade total de presentes
    produzida por dia pela fábrica do Papai Noel.
    :return:
    """
    n = int(input())
    b, a, m, d = 0, 0, 0, 0
    for i in range(n):
        e, g, h = input().split(" ")
        h = int(h)
        if g == "bonecos":
            b += h
        elif g == "arquitetos":
            a += h
        elif g == "musicos":
            m += h
        elif g == "desenhistas":
            d += h
    b_t = b // 8
    a_t = a // 4
    m_t = m // 6
    d_t = d // 12
    total = b_t + a_t + m_t + d_t
    print(total)


grupo_de_trabalho_do_noel()

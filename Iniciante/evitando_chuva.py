def evitando_chuva():
    """
    Esta função calcula o números de guarda-chuvas comprado
    por Rafael seguindo a regra que quando sai de casa para
    o trabalho, se estiver fazendo sol, não compra o guarda-
    chuva nem leva para o trabalho. Caso esteja chovendo e
    não estiver guarda-chuva em casa, ele compra um gurada-
    chuva, caso tenha, ele não compra e leva o que tem. A
    mesma regra vale quando está no trabalho.
    :return:
    """
    n = int(input())
    g_casa, g_trab, comp_casa, comp_trab = 0, 0, 0, 0
    for i in range(n):
        sd, sn = input().split(" ")
        if sd == "sol" and sn == "sol":
            continue
        elif sd == "chuva" and sn == "chuva":
            if g_casa == 0:
                comp_casa += 1
                comp_trab += 0
                g_casa += 1
                g_trab += 0
            elif g_casa > 0:
                continue
        elif sd == "sol" and sn == "chuva":
            if g_trab == 0:
                comp_casa += 0
                comp_trab += 1
                g_casa += 1
                g_trab += 0
            elif g_trab > 0:
                comp_casa += 0
                comp_trab += 0
                g_casa += 1
                g_trab -= 1
        elif sd == "chuva" and sn == "sol":
            if g_casa == 0:
                comp_casa += 1
                comp_trab += 0
                g_casa += 0
                g_trab += 1
            elif g_casa > 0:
                comp_casa += 0
                comp_trab += 0
                g_casa -= 1
                g_trab += 1
    print(f"{comp_casa} {comp_trab}")


evitando_chuva()

def entrada_e_saida_de_numeros_inteiros():
    """
    Esta função recebe como entrada 3 números inteiros e tem
    como saida os seguintes critérios:
    Crie três variáveis para armazenar números inteiros;
    Leia o primeiro número, que pode ser um valor na faixa de: -10000 ≤ A ≤ 10000;
    Leia o segundo número, que pode ser um valor na faixa de: 0 ≤ B ≤ 99;
    Leia o terceiro número, que pode ser um valor na faixa de: 0 ≤ C ≤ 999;
    Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco,
    o número armazenado na primeira variável, uma virgula, um espaço em branco,
    a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número
    armazenado na segunda variável, uma virgula, um espaço em branco, a letra C, um
    espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na
    terceira variável. Não esqueça de pular linha;
    Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e
    justificado a direita;
    Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e
    preenchido com zeros;
    Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e
    justificado a esquerda.
    :return:
    """
    a = input()
    a_int = int(a)
    b = input()
    c = input()
    str_0 = ""
    l_b = ""
    l_c = ""
    print(f"A = {int(a)}, B = {int(b)}, C = {int(c)}")
    print(f"A = {int(a):>10}, B = {int(b):>10}, C = {int(c):>10}")
    if a_int < 0:
        while len(str_0) < 10 - (len(a) - 1):
            if a_int < 0 and len(str_0) == 0:
                str_0 += "-0"
            elif len(str_0) > 0:
                str_0 += "0"
    elif a_int > 0:
        while len(str_0) < 10 - len(a):
            str_0 += "0"
    d = b
    e = c
    x = len(d.lstrip("0"))
    y = len(e.lstrip("0"))
    if x == len(b):
        l_b = "0" * (10 - len(b))
    elif x < len(b):
        diff_x = 10 - x
        l_b = "0" * diff_x
    if y == len(c):
        l_c = "0" * (10 - len(c))
    elif y < len(c):
        diff_y = 10 - y
        l_c = "0" * diff_y
    print(f"A = {str_0}{a.strip('-')}, B = {l_b}{int(b)}, C = {l_c}{int(c)}")
    print(f"A = {int(a):<10}, B = {int(b):<10}, C = {int(c):<10}")


entrada_e_saida_de_numeros_inteiros()

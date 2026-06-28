def desafio_do_maior_numero():
    """
    Está função calcula o maior número dentro de uma sequência de números
    fornecidos pelo usuário que termina a sequência com o número zero printando
    o maior número da sequência.
    :return:
    """
    l1 = []
    num = input().split(" ")
    for i in range(0, len(num)):
        if num[i] == "0":
            break
        else:
            num[i] = int(num[i])
            l1.append(num[i])
    l1.sort()
    if len(l1) > 0:
        print(max(l1))
    else:
        print(0)


desafio_do_maior_numero()

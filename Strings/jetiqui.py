def jetiqui():
    """
    Uma empresa de cosméticos, chamada Jetiqui, tinha um programa de
    televisão que premiava consultores e clientes. Este programa se
    chamava Gira a Roda. Neste programa, havia uma palavra secreta,
    e a cada rodada, a roda era girada, com vários prêmios, passa a
    vez e perde tudo. Se caísse no perde tudo, um participante perdia
    tudo que tinha arrecadado de premiação até o momento e passava a
    vez para outro participante. Se caísse no passa a vez, não perdia
    nada, mas passava a vez para outro participante tentar acertar a
    palavra secreta. Se caísse em algum prêmio de valor, o participante
    poderia dizer uma letra, e se esta fizesse parte da palavra secreta,
    apenas uma delas seria revelada. Ou seja, se a palavra fosse batata,
    teria que rodar 3 vezes e dizer a 3 vezes para revelar todos os A da
    palavra. Um dia, Pasqualito, com um grande conhecimento sobre as palavras,
    foi participar deste programa. Sempre quando faltavam duas letras a
    serem reveladas, ele tinha um ótimo palpite, dentre duas possibilidades,
    qual seria a possível resposta. Ele queria saber se existia a possibilidade
    de arriscar uma letra que definisse qual das duas palavras seria a correta,
    pois não queria arriscar mais uma rodada, com receio de passar a vez. Por
    exemplo, a palavra exibida era _or_e, ou seja, a primeira e a penúltima letra
    não tinham sido reveladas ainda, e as duas palavras que ele achava eram sorte
    e torre. Neste caso, ele conseguiria sanar a dúvida dele, falando a letra T.
    Se a letra aparecesse no início, a palavra seria torre, se aparecesse na
    penúltima, a palavra seria sorte.

    Escreva um programa que, dada a palavra incompleta e as duas possibilidades, diga
    se é possível que Pasqualito descubra a palavra certa na rodada atual.

    Entrada
    A primeira linha contém um inteiro C representando a quantidade de casos de teste.
    Cada caso de teste possui três palavras, sendo as duas primeiras, as palavras que
    Pasqualito está em dúvida, e a terceira é a palavra incompleta. As palavras têm,
    no máximo, 15 letras.

    Saída
    Para cada caso de teste, imprima Y se for possível resolver a dúvida, ou N se não
    for possível.
    :return:
    """
    c = int(input())
    for i in range(c):
        palavras, letras, diffs, flag1, flag2 = [], [[], []], [[], []], 1, 0
        for j in range(3):
            palavra = input()
            palavras.append(palavra)
        if palavras[0] == palavras[1]:
            print("Y")
            flag1 = 0
        if flag1 != 0:
            for j in range(0, len(palavras[0])):
                if palavras[2][j] == "_":
                    letras[0].append(palavras[0][j])
                    letras[1].append(palavras[1][j])
                if palavras[2][j] != "_":
                    diffs[0].append(palavras[0][j])
                    diffs[1].append(palavras[1][j])
            for j in range(0, len(diffs)):
                if diffs[0] != diffs[1]:
                    print("Y")
                    break
                else:
                    flag2 = 1
            if flag2 == 1:
                for j in range(0, len(letras[0])):
                    if letras[0][0] != letras[1][0] and letras[0][0] == letras[0][1]:
                        print("Y")
                        break
                    if letras[1][0] != letras[0][0] and letras[1][0] == letras[1][1]:
                        print("Y")
                        break
                    if letras[0][0] != letras[1][0] and letras[0][0] == letras[1][1]:
                        print("Y")
                        break
                    if letras[0][1] != letras[1][1] and letras[0][1] == letras[1][0]:
                        print("Y")
                        break
                    if letras[0][1] != letras[1][1] and letras[0][1] == letras[1][0]:
                        print("Y")
                        break
                    if letras[0][0] == letras[1][1] and letras[0][1] != letras[1][0]:
                        print("Y")
                        break
                    if letras[0][0] != letras[1][1] and letras[0][1] == letras[1][0]:
                        print("Y")
                        break
                    else:
                        print("N")
                        break


jetiqui()

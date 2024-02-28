from time import sleep


def plagio_musical():
    """
    As notas musicais são unidades básicas da música ocidental tradicional.
    Cada nota está associada a uma frequência. Duas notas musicais cujas
    frequêcias fundamentais tenham uma relação de potência de 2 (uma metade
    da outra, uma duas vezes a outra, etc.) são percebidas como muito similar.
    Por isso, todas as notas com esse tipo de relação recebem o mesmo nome,
    como descrito a seguir.

    Há doze notas básicas, em uma sequência crescente de frequências, cada
    nota separada da anterior por uma mesma distância na escala musical
    (essa distância é chamada de meio-tom). Sete dessas doze notas são
    representadas por letras do alfabeto (A, B, C, D, E, F e G). A tabela
    abaixo mostra a distância, em meio-tons, entre essas notas.

    ----------------------------------------------------------------------|
    |   Notas                   | A-B | B-C | C-D | D-E | E-F | F-G | G-A |
    |---------------------------------------------------------------------|
    | Números de meios-tons     | 2   |  1  |  2  |  2  |  1  |  2  |  2  |
    |---------------------------------------------------------------------|

    Note que há cinco notas que não são representadas pelas letras do alfabeto:
    as que estão entre A e B, entre C e D, entre D e E, entre F e G e entre G e A.

    As notas podem ser modificadas por duas alterações cromáticas: sustenido e bemol,
    representadas respectivamente pelos símbolos ‘#’ e ‘b’. Sustenido altera a nota
    em meio tom para cima, e bemol altera a nota em meio tom para baixo. Uma nota
    com alteração cromática é denotada pelo nome da nota seguida pelo símbolo da
    alteração. Note que com esse esquema conseguimos representar todas as doze notas.

    Uma melodia pode ser representada por uma sequência de notas musicais. Por exemplo,

    A   A   D   C#   C#   D   E   E   E   F#   A   D   G#   A

    é uma melodia muito conhecida. Note no entanto que, como as distâncias entre os
    meios-tons são sempre iguais, a mesma melodia pode ser escrita iniciando em outra
    nota (dizemos que a melodia está em outro tom):

    B   B   E   D#   D#   E   Gb   Gb   Gb   G#   B   E   A#   B

    Sua vizinha é uma famosa compositora que suspeita que tenham plagiado uma de suas músicas.
    Ela pediu a sua ajuda para escrever um programa que, dada a sequência de notas da melodia
    de sua música, e a sequência de notas de um trecho de melodia suspeito, verifique se o trecho
    supeito ocorre, em algum tom, na música dada.

    Entrada
    A entrada é composta por vários casos de teste. A primeira linha de um caso de teste contém
    dois inteiros M e T (1 ≤ M ≤ 100000, 1 ≤ T ≤ 10000, T ≤ M ), indicando respectivamente o número
    de notas da música e do trecho suspeito de ter sido plagiado. As duas linhas seguintes contém M e T
    notas, respectivamente, indicando as notas da música e do trecho suspeito.

    As notas em cada linha são separadas por espaço; cada nota é uma dentre ‘A’, ‘B’, ‘C’, ‘D’, ‘E’, ‘F’
    ou ‘G’, possivelmente seguida de um modificador: ‘#’ para um sustenido ou ‘b’ para um bemol.

    O último caso de teste é seguido por uma linha que contém apenas dois números zero separados por um
    espaço em branco.

    Saída
    Para cada caso de teste, imprima uma única linha contendo um caractere: ‘S’ caso o trecho realmente
    tenha sido plagiado pela música ou ‘N’ caso contrário.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    m, t = entrada[0], entrada[1]
    while m != 0 and t != 0:
        notacoes_musicais, semi_tons_naturais, n1, n2, comeco, fim, coda,\
            verificar1, verificar2, trechos_musica, aux = [], [], 0, 0, 0, 0, 0, [], [], [], []
        notas = ["A", "B", "C", "D", "E", "F", "G"]
        for i in range(0, len(notas)):
            notacoes_musicais.append(notas[i] + "b")
            notacoes_musicais.append(notas[i])
            notacoes_musicais.append(notas[i] + "#")
        musica = input().split(" ")
        trecho = input().split(" ")
        # print(notacoes_musicais)
        # print(musica)
        # print(trecho)
        semi_tons_naturais.append(notacoes_musicais.index("E#"))
        semi_tons_naturais.append(notacoes_musicais.index("F"))
        semi_tons_naturais.append(notacoes_musicais.index("B"))
        semi_tons_naturais.append(notacoes_musicais.index("Cb"))
        # print(semi_tons_naturais)
        for i in range(0, len(trecho)):
            for k in range(0, len(notacoes_musicais)):
                if i >= len(trecho) - 1:
                    break
                comeco = notacoes_musicais.index(trecho[i])
                fim = notacoes_musicais.index(trecho[i + 1])
                if fim >= comeco:
                    cont = fim - comeco
                    for j in range(comeco, fim + 1):
                        aux.append(notacoes_musicais.index(notacoes_musicais[j]))
                    for j in range(0, len(semi_tons_naturais)):
                        if semi_tons_naturais[j] in aux and trecho[i] != trecho[i + 1]:
                            coda -= 1
                    cont += coda
                    verificar1.append(cont)
                    coda = 0
                    aux = []
                    break
                if comeco > fim:
                    cont = len(notacoes_musicais) - comeco + fim
                    for j in range(comeco, len(notacoes_musicais)):
                        aux.append(notacoes_musicais.index(notacoes_musicais[j]))
                    for j in range(0, len(semi_tons_naturais)):
                        if semi_tons_naturais[j] in aux:
                            coda -= 1
                    cont += coda
                    coda = 0
                    aux = []
                    for j in range(0, fim + 1):
                        aux.append(notacoes_musicais.index(notacoes_musicais[j]))
                    for j in range(0, len(semi_tons_naturais)):
                        if semi_tons_naturais[j] in aux:
                            coda -= 1
                    cont += coda
                    verificar1.append(cont)
                    coda = 0
                    aux = []
                    break
        for i in range(0, len(musica)):
            for k in range(n2, len(notacoes_musicais)):
                if k >= len(musica) - 1:
                    break
                comeco = notacoes_musicais.index(musica[k])
                fim = notacoes_musicais.index(musica[k + 1])
                if fim >= comeco:
                    cont = fim - comeco
                    for j in range(comeco, fim + 1):
                        aux.append(notacoes_musicais.index(notacoes_musicais[j]))
                    for j in range(0, len(semi_tons_naturais)):
                        if semi_tons_naturais[j] in aux and musica[k] != musica[k + 1]:
                            coda -= 1
                    cont += coda
                    # print(cont)
                    # sleep(5)
                    trechos_musica.append(cont)
                    coda = 0
                    aux = []
                if comeco > fim:
                    cont = len(notacoes_musicais) - comeco + fim
                    for j in range(comeco, len(notacoes_musicais)):
                        aux.append(notacoes_musicais.index(notacoes_musicais[j]))
                    for j in range(0, len(semi_tons_naturais)):
                        if semi_tons_naturais[j] in aux:
                            coda -= 1
                    cont += coda
                    # print(f"Ok1! {cont}")
                    # sleep(3)
                    coda = 0
                    aux = []
                    for j in range(0, fim + 1):
                        aux.append(notacoes_musicais.index(notacoes_musicais[j]))
                    for j in range(0, len(semi_tons_naturais)):
                        if semi_tons_naturais[j] in aux:
                            coda -= 1
                    cont += coda
                    # print(f"Ok2! {cont}")
                    # sleep(3)
                    trechos_musica.append(cont)
                    coda = 0
                    aux = []
                if len(trechos_musica) == len(verificar1):
                    verificar2.append(trechos_musica)
                    trechos_musica = []
                    n2 += 1
                    break
        # print(verificar1)
        # print(verificar2)
        if verificar1 in verificar2:
            print("S")
        else:
            print("N")
        entrada = list(map(int, input().strip().split(" ")))
        m, t = entrada[0], entrada[1]


plagio_musical()

"""
14 14
A A D C# C# D E E E F# A D G# A
B B E D# D# E Gb Gb Gb G# B E A# B
"""
def arremesso_de_bolas():
    """
    Seus amigos inventaram uma nova competição: Arremesso de bolas. O objetivo
    é simples, basta arremessar uma bola de forma que ela caia dentro de um
    buraco N metros a sua frente.

    Quando a bola é arremessada, digamos que à uma velocidade inteira V, ela
    permanece no ar por V metros e então quica. Ela repete esse processo V vezes.
    Após ela quicar V vezes, ela muda sua velocidade para V-1, e o processo anterior
    se repete, até que a velocidade seja igual a 0.

    Por exemplo, se a bola for arremessada a uma velocidade igual a 3, ela quicará nos
    seguintes pontos: 3, 6, 9, 11, 13, 14; conforme pode ser visto na imagem.

    [Imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_1532.png)

    Você consegue arremessar a bola à uma velocidade inteira menor ou igual a V.
    Dada a distância do buraco, diga se é possível que você arremesse a bola e que
    ela quique exatamente no buraco, acertando-o.

    Entrada
    Haverá diversos casos de teste. Cada caso de teste contém dois inteiros, N e V
    (1 ≤ N ≤ 1000, 1 ≤ V ≤ 30), representando a distância do buraco e a velocidade
    máxima com a qual você consegue arremessar a bola.

    O último caso de teste é indicado quando N = V = 0, o qual não deverá ser processado.

    Saída
    Para cada caso de teste, imprima uma linha contendo a palavra “possivel” (sem aspas),
    caso seja possível arremessar a bola a uma velocidade menor ou igual a V de forma que
    ela quique no buraco, ou “impossivel”, caso contrário.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, v = int(entrada[0]), int(entrada[1])
    while n != 0 and v != 0:
        parametro, flag = v, False
        for i in range(parametro, -1, -1):
            v, cont, distancia = i, 0, 0
            while v > 0:
                while cont < v:
                    distancia += v
                    if distancia == n:
                        flag = True
                        break
                    cont += 1
                v -= 1
                cont = 0
                if distancia == n or flag == True:
                    flag = True
                    print("possivel")
                    break
            if flag:
                break
        if not flag:
            print("impossivel")
        entrada = list(map(int, input().strip().split(" ")))
        n, v = int(entrada[0]), int(entrada[1])


arremesso_de_bolas()

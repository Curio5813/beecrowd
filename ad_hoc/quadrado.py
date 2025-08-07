def quadrado():
    """
    Um quadrado quase mágico, de dimensões N × N, é um quadrado que obedece à seguinte condição.
    Existe um número inteiro positivo M tal que: para qualquer linha, a soma dos números da linha
    é igual a M; e para qualquer coluna, a soma dos números da coluna é também igual a M. O quadrado
    seria mágico, e não apenas quase mágico, se a soma das diagonais também fosse M. Por exemplo,
    a figura abaixo, parte (a), apresenta um quadrado quase mágico onde M = 21.

    Imagem(https://resources.beecrowd.com/gallery/images/contests/UOJ_178_I.png)

    Laura construiu um quadrado quase mágico e alterou, propositalmente, um dos números! Nesta tarefa,
    você deve escrever um programa que, dado o quadrado quase mágico alterado por Laura, descubra qual
    era o número original antes da alteração e qual número foi colocado no lugar. Por exemplo, na parte
    (b) da figura, o número original era 1, que Laura alterou para 7.

    Entrada
    A primeira linha da entrada contém apenas um número N (3 ≤ N ≤ 50), representando a dimensão do
    quadrado. As N linhas seguintes contêm, cada uma, N números inteiros (entre 1 e 10000), definindo
    o quadrado. A entrada é garantidamente um quadrado quase mágico onde exatamente um número foi
    alterado.

    Saída
    Seu programa deve imprimir apenas uma linha contendo dois números: primeiro o número original e
    depois o número que Laura colocou no seu lugar.
    :return:
    """
    n = int(input())
    quase_magico, colunas, temp, somas_linhas, somas_colunas, soma = [], [], [], [], [], 0
    for i in range(n):
        quase_magico.append(list(map(int, input().strip().split(" "))))
    for i in range(0, len(quase_magico)):
        for j in range(0, len(quase_magico[i])):
            temp.append(quase_magico[j][i])
        colunas.append(temp)
        temp = []
    for i in range(0, len(quase_magico)):
        somas_linhas.append(sum(quase_magico[i]))
        somas_colunas.append(sum(colunas[i]))
    for i in somas_linhas:
        if somas_linhas.count(i) >= 2:
            soma = i
            break
    cont, erro = 0, []
    for i in range(0, len(somas_linhas)):
        for j in range(0, len(somas_linhas)):
            if somas_linhas[i] != somas_linhas[j]:
                cont += 1
                if cont >= 2:
                    temp.append(i)
                    break
        cont = 0
        if len(temp) > 0:
            erro.append(*temp)
            break
    cont, temp = 0, []
    for i in range(0, len(somas_colunas)):
        for j in range(0, len(somas_colunas)):
            if somas_colunas[i] != somas_colunas[j]:
                cont += 1
                if cont >= 2:
                    temp.append(i)
                    break
        cont = 0
        if len(temp) > 0:
            erro.append(*temp)
            break
    numero_errado = quase_magico[erro[0]][erro[1]]
    quase_magico[erro[0]][erro[1]] = 0
    numero_certo = soma - sum(quase_magico[erro[0]])
    print(numero_certo, numero_errado)


quadrado()

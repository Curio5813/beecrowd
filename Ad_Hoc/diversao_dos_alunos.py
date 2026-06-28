def diversao_dos_alunos():
    """
    Juilherme e Jogério, gostam muito de jogos matemáticos.
    Juilherme acabou de criar mais um jogo matemático para
    eles se divertirem enquanto assistem essa competição online.

    O jogo consiste nos seguintes passos:

    1) Juilherme escolhe um número N e Jogério escolhe um número M.
    2) Juilherme e Jogério devem então achar dois números primos P1 e
    P2, de tal forma que eles sejam o mais próximo possível do que numero
    N e M, respectivamente. Além disso P1 deve ser menor ou igual a N e
    P2 deve ser menor ou igual a M.
    3) A resposta final do desafio é encontrar a multiplicacão de P1 e P2.
    Quem achar a resposta primeiro é o vencedor.

    Como eles irão tentar achar a resposta o mais rápido possível, algumas
    vezes chegando a resultados incorretos, eles precisam de um programa
    que entregue a resposta final do jogo, para que possa ser comparada
    com a resposta encontrada por eles.

    Usando as informacoes do jogo, faça um programa que dado os números N e M
    imprima o resultado final.

    Entrada
    A entrada do programa consiste de apenas uma linha com N e M (2 <= N, M <= 1000).

    Saída
    A saída do seu programa deve conter apenas uma linha informando a resposta final
    do jogo.
    :return:
    """
    p1, p2 = map(int, input().split(" "))
    primos1, primos2 = [], []
    for i in range(2, p1 + 1):
        for k in range(2, p1 + 1):
            if i % k == 0 and i == k:
                primos1.append(i)
            if i % k == 0 and i != k:
                break
    for i in range(2, p2 + 1):
        for k in range(2, p2 + 1):
            if i % k == 0 and i == k:
                primos2.append(i)
            if i % k == 0 and i != k:
                break
    maior1 = primos1[-1]
    maior2 = primos2[-1]
    print(maior1 * maior2)


diversao_dos_alunos()

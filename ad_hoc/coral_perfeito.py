from time import sleep


def coral_perfeito():
    """
    A Maestrina do coral está planejando o espetáculo que apresentará
    na famosa Semana Brasileira de Corais. Ela pensou em preparar uma
    nova música, definida da seguinte maneira:

    • cada um dos integrantes do coral inicia cantando uma nota, e somente
    muda de nota quando determinado pela Maestrina;

    • ao final de cada compasso, a Maestrina determina que exatamente dois
    integrantes alterem a nota que cantam: um integrante passa a cantar a nota
    imediatamente acima da nota que cantava, e o outro integrante passa a
    cantar a nota imediatamente abaixo da nota que cantava;

    • a música termina ao final do primeiro compasso em que todos os integrantes
    do coral cantam a mesma nota.

    A Maestrina já tem várias ideias de como distribuir as notas no início da música
    entre os integrantes do coral, de forma a criar o efeito desejado. No entanto,
    ela está preocupada em saber se, dada uma distribuição de notas entre os integrantes,
    é possível chegar ao final da música da forma desejada (todos cantando a mesma nota)
    e, caso seja possível, qual o número mínimo de compassos da música. Você pode ajudá-la?

    Entrada
    A primeira linha de um caso de teste contém um inteiro N (2 ≤ N ≤ 104) indicando o número
    de integrantes do coral. As notas serão indicadas por números inteiros. A segunda linha
    contém N números inteiros, indicando as notas iniciais (−105 ≤ notai ≤105), onde 0 ≤ i ≤ N−1,
    que cada integrante deve cantar. As notas são dadas em ordem não decrescente de altura (notai ≤notai+1).

    Saída
    Para cada caso de teste imprima uma linha contendo um único número inteiro indicando o número
    mínimo de compassos que a música terá. Se não é possível terminar a música com todos os integrantes
    cantando a mesma nota, imprima o valor−1.
    :return:
    """
    while True:
        try:
            n = int(input())
            compare, cont, resp = {()}, 1, 0
            compare.discard(())
            notas = list(map(int, input().split(" ")))
            j = len(notas) - 1
            if sum(notas) % n == 0:
                if len(set(notas)) == 1:
                    print(cont)
                    break
                elif len(notas) == 2 and notas[0] != notas[1] and abs(notas[0] - notas[1]) == 2:
                    cont += 1
                    resp = 1
                elif len(notas) == 3 and notas[1] - notas[0] == 1 and notas[2] - notas[1] == 1:
                    cont += 1
                    resp = 1
                elif len(notas) == 4 and notas[0] == notas[1] and notas[2] == notas[3] \
                        and notas[2] - notas[1] == 2:
                    cont += 1
                    resp = 1
                else:
                    for i in range(0, notas[-1]):
                        for k in range(0, len(notas) - 1):
                            if notas[k] < notas[k + 1]:
                                while notas[k] <= notas[j] and k + 1 < j:
                                    notas[k] += 1
                                    notas[j] -= 1
                                    cont += 1
                                    if len(set(notas)) == 3:
                                        resp = 2
                                        break
                                if resp == 2:
                                    break
                            elif len(set(notas)) == 3:
                                for m in range(0, notas[-1]):
                                    for n in range(0, len(notas) - 1):
                                        if notas[n] > notas[j]:
                                            break
                                        if len(set(notas)) == 1:
                                            cont += 1
                                            resp = 1
                                            break
                                        notas[n] += 1
                                        notas[j] -= 1
                                        cont += 1
                                    if resp == 1:
                                        break
                if resp == 1:
                    print(cont)
                    print(notas)
                elif resp == 2:
                    print(cont)
                    print(notas)
                elif resp == 0:
                    print("O programa está incorreto!")
            else:
                print(-1)
        except EOFError:
            break


coral_perfeito()

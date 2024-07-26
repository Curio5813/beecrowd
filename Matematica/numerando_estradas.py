def numerando_estradas():
    """
    No meu país, as ruas não têm nomes, cada uma delas tem apenas
    um número como nome. Estes números devem ser únicos, mas nem
    sempre este é o caso. O governo local aloca alguns inteiros
    para citar as estradas e, em muitos casos, o número de inteiros
    alocados é menor do que o número total de estradas. Nesse caso,
    para que os nomes das estradas sejam único, alguns sufixos de
    caracteres únicos são utilizados. Assim, as estradas são nomeadas
    como 1, 2, 3, 1A, 2B, 3C etc. É claro que o número de sufixos também
    é sempre limitado a 26 (A, B, …, Z). Por exemplo, se existem 4 estradas
    e dois inteiros diferentes são alocados para nomear, então algumas
    declarações de nomes possíveis podem ser:

    1, 2, 1A, 2B
    1, 2, 1A, 2C
    3, 4, 3A, 4A
    1, 2, 1B, 1C

    Dado o número de estradas (R) e os números de inteiros alocados para a
    nomeação (N), o seu trabalho é determinar o número mínimo de sufixos
    diferentes necessários (de todas as nomeações possíveis) para nomear
    as ruas, assumindo que não existam duas ruas com o mesmo nome.

    Entrada
    O arquivo de entrada pode conter até 10002 linhas de entrada. Cada linha
    contém dois inteiros R e N (R < 10001, 0 < N). Aqui R é o número total de
    ruas a serem nomeadas e N indica o número de inteiros alocados para a nomeação.
    A entrada termina com "0 0" que não deve ser processado.


    Saída
    Para cada linha de entrada, você de produzir uma linha de saída. Esta linha
    contém o número de série de saída, seguido por um inteiro D que indica o número
    mínimo de sufixos necessários para nomear as ruas. Se não é possível nomear todas
    as ruas, você deve imprimir “impossible” no lugar (sem as aspas).
    :return:
    """
    caso = 0
    while True:
        sufixos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        r, n = map(int, input().strip().split(" "))
        inteiros, cont, str_sufx, flag, sufixos_usados, sufx_mais = [], 1, "", 0, [], []
        if r == 0 and n == 0:
            break
        caso += 1
        for i in range(1, n + 1):
            inteiros.append(i)
        sufx_mais = inteiros.copy()
        if len(inteiros) >= r:
            print(f"Case {caso}: 0")
        else:
            for i in range(0, len(sufixos)):
                for j in range(0, len(inteiros)):
                    str_sufx = str(inteiros[j]) + sufixos[i]
                    sufx_mais.append(str_sufx)
                    if sufixos[i] not in sufixos_usados:
                        sufixos_usados.append(sufixos[i])
                    if len(sufx_mais) == r:
                        flag = 1
                        print(f"Case {caso}: {len(sufixos_usados)}")
                        break
                if len(sufixos_usados) >= 26 or flag == 1:
                    break
            if flag == 0:
                # print(inteiros)
                print(f"Case {caso}: impossible")


numerando_estradas()

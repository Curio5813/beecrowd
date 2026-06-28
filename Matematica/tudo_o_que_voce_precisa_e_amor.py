from math import gcd


def tudo_o_que_voce_precisa_e_amor():
    """
    Foi inventado um novo dispositivo poderoso pela Beautifull Internacional
    Machines Corporation chamado de "Máquina do amor!". Dada uma string feita
    de dígitos binários, a máquina do amor responde se isto é feito somente de
    amor, ou seja, se tudo o que você irá precisar para construir aquela string
    for somente amor. A definição de amor para a Máquina do amor é outra string
    de dígitos binários, fornecida por um operador humano. Vamos supor que nós
    temos uma string L que representa "love" e forneçamos uma string S para a
    máquina do amor. Diremos então que tudo o que você precisa é amor para construir
    S se pudermos repetidamente subtrair L de S até que sobre apenas L. A subtração
    definida aqui é a mesma subtração aritmética binária na base 2. Por definição
    é fácil de ver que L > S (em binário), então S não é feito de amor. Se S = L então
    S é obviamente feito de amor.

    Por exemplo, suponha S = "11011" e L = "11". Se repetidamente subtrairmos L de S,
    obteremos: 11011, 11000, 10101, 10010, 1111, 1100, 1001, 110, 11. Portanto, dado
    este L, tudo o que você necessita é amor para construir S. Devido a algumas
    limitações da Máquina do Amor, não será possível lidar com strings com zero à
    esquerda. Por exemplo "0010101", "01110101", "011111" etc. são string Inválidas.
    Strings que contenham apenas um dígito também são strings inválidas (isto é outra
    limitação).

    Sua tarefa para este problema é: dadas duas strings binárias válidas, S1 e S2, veja
    se é possível ter uma string L válida tal que ambas, S1 e S2 possam ser feitas apenas
    de L (i.e. dadas duas strings válidas S1 e S2, indique se existe pelo menos uma string
    L válida tal que ambas S1 e S2 sejam feitas apenas de L). Por exemplo, para S1 = 11011
    e S2 = 11000, nós podemos ter L = 11 tal que S1 e S2 são feitas ambas somente de L (como
    pode ser visto no exemplo abaixo).

    Entrada
    A primeira linha de entrada contém um valor inteiro positivo N (N < 10000) que indica
    o número de casos de teste. Então, 2*N linhas vem a seguir. Cada par de linhas consiste
    de um caso de teste. Cada par de linhas contém respectivamente S1 e S2 que serão
    inseridas como entrada para a máquina do amor. Nenhuma string conterá menos do que 2
    ou mais do que 30 caracteres. Você pode assumir que as strings de entrada serão válidas
    e estarão de acordo com as regras acima.

    Saída
    Para cada par de strings, seu programa deve imprimir uma das seguintes mensagens:

    Pair #p: All you need is love!
    Pair #p: Love is not all you need!

    Onde p representa o número do par de entrada (que inicia em 1). Seu programa deve imprimir
    a primeira mensagem no caso de existir pelo menos uma string L válida tal que ambas strings
    S1 e S2 possam ser feitas somente de L. Caso contrário, imprima a segunda linha.
    :return:
    """
    n = int(input())
    cont = 0
    for i in range(n):
        s1 = "0b" + input()
        s2 = "0b" + input()
        s1_int = int(s1, 2)
        s2_int = int(s2, 2)
        cont += 1
        num = gcd(s1_int, s2_int)
        if num > 1:
            print(f"Pair #{cont}: All you need is love!")
        if num == 1:
            print(f"Pair #{cont}: Love is not all you need!")


tudo_o_que_voce_precisa_e_amor()

def numeros_primos():
    """
    Esta função retorna uma lista de números primos até que um
    limite predefinido. Este algoritmo usa a ideia "O crivo
    de Eratóstenes".
    :return:
    """
    primos, n_p, lim = [], set(), 100_000 + 1
    for i in range(2, lim):
        if i in n_p:
            continue
        for k in range(i * 2, lim, i):
            n_p.add(k)
        primos.append(i)
    return primos


def as_moedas_de_robbie(primos):
    """
    Esta função calcula o resultado de um jogo das moedas de Robbie, onde M é a
    quantidade de moedas que Robbie tem guardadas dentro de seu cilindro. Glória
    deve escolher a quantidade de moedas no cilindro de Robbie e um passo, pulando
    na sequência númerica, sempre começando em 1. se a soma dos valores das moedas
    for igual a um número primo, a função deve printar "You’re a coastal aircraft,
    Robbie, a large silver aircraft. Caso não seja numero primo deve imprimir
    "Bad boy! I’ll hit you."
    :return:
    """
    while True:
        l1, soma = [], 0
        try:
            m = int(input())
            for i in range(m):
                v = int(input())
                l1.append(v)
            l1 = l1[::-1]
            p = int(input())
            if 1 <= p <= m:
                for i in range(0, len(l1), p):
                    soma += l1[i]
                if soma in primos:
                    print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
                elif soma not in primos:
                    print("Bad boy! I’ll hit you.")
        except EOFError:
            break


as_moedas_de_robbie(numeros_primos())

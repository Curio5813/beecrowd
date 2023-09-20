from time import time

start = time()


def jogo_das_aranhas():
    """
    Esta função calcula e imprime um inteiro positivo k < 10^16,
    que satisfaz o jogo das aranhas criados por Arthur e Merlin,
    onde somente as aranhas-marrons venenosas são mortas, que
    estão dipostas em um circulo com com as inofensivas
    aranhas-vermelhas, dado como entrada um numero inteiro
    que é número de aranhas-marrons e, por conseguinte, de
    aranhas vermelhas, sendo que as aranhas-marrons vêm primereiro
    no círculo. Merlin tem que dizer um número onde somente as
    aranhas-marrons são mortas, para assim, vencer o jogo. Um vez
    morta uma aranhas, deves-se     contar somente com as aranhas
    restantes.
    :return:
    """
    n = int(input())
    aranhas, marrons, vermelhas, aux, k = [], [], [], [], 5

    for i in range(1, n * 2 + 1):
        aranhas.append(i)
        aux.append(i)
        if i <= n:
            vermelhas.append(i)
        if i > n:
            marrons.append(i)
    for k in range(n + 1, 2_000_000_000 + 1):
        j = k
        while True:
            if len(aranhas) == n:
                break
            while k <= len(aranhas):
                aranhas.pop(k - 1)
                k += j
            k = k - len(aranhas) - 1
        if aranhas == vermelhas:
            return print(k)
        elif aranhas != vermelhas:
            aranhas = aux


jogo_das_aranhas()
end = time()
print(f"{(end - start) / 60}")

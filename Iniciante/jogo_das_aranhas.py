from copy import deepcopy


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
    aranhas = [x for x in range(1, n * 2 + 1)]
    aux_aranhas = deepcopy(aranhas)
    i = n
    aux = i
    while True:
        aux += 1
        i = aux
        aranhas_mortas = []
        aranhas = deepcopy(aux_aranhas)
        while True:
            if i > len(aranhas):
                i -= len(aranhas)
                while i > len(aranhas):
                    i -= len(aranhas)
                    if i <= 0:
                        while i <= 0:
                            i += 1
            if len(aranhas_mortas) == n and all(a in aux_aranhas[n:] for a in aranhas_mortas):
                return print(aux)
            if aranhas[i - 1]  <= n:
                break
            aranhas_mortas.append(aranhas[i - 1])
            aranhas.remove(aranhas[i - 1])
            i -= 1
            if i <= 0:
                i += aux
            if i > len(aranhas):
                while i > len(aranhas):
                    i -= len(aranhas)
            i += aux
        aranhas_mortas.sort()


if __name__ == '__main__':
    jogo_das_aranhas()

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
    aranhas_mortas = []
    while aranhas_mortas != aux_aranhas[n:]:
        aux += 1
        i = aux
        aranhas_mortas = []
        aranhas = [x for x in range(1, n * 2 + 1)]
        while True:
            if len(aranhas) == n:
                break
            if i >= len(aranhas):
                while i >= len(aranhas):
                    i -= n
            # print(aux, i, aranhas_mortas, aranhas)
            aranhas_mortas.append(aranhas[i])
            aranhas.pop(i - 1)
            print(aux, i, aranhas_mortas, aranhas)
            i += n
        aranhas_mortas.sort()
        print(aux, aranhas_mortas)
    print(aux)


if __name__ == '__main__':
    jogo_das_aranhas()



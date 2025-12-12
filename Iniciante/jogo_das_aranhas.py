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
        aranhas = deepcopy(aux_aranhas)
        while True:
            if i >= len(aranhas):
                i = len(aranhas)
                cont = i - 1
                while cont < aux:
                    i += 1
                    if i >= len(aranhas):
                        i = 0
                    cont += 1
            if len(aranhas_mortas) == n:
                break
            aranhas_mortas.append(aranhas[i - 1])
            aranhas.remove(aranhas[i - 1])
            cont = 0
            while cont < aux:
                i += 1
                if i >= len(aranhas):
                    i = 0
                cont += 1
            print(aux, aranhas_mortas, aranhas, i)
        aranhas_mortas.sort()
        print(aux, aranhas_mortas)
    print(aux)


if __name__ == '__main__':
    jogo_das_aranhas()



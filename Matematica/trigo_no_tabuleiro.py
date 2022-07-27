def trigo_tabuleiro():
    lista = []
    n = int(input())
    for k in range(1, n + 1):
        casa = int(input())
        quilo = ((1/12)/1000) * 2 ** casa
        lista.append(int(quilo))
    for k in range(0, len(lista)):
        print(f'{lista[k]} kg')


trigo_tabuleiro()

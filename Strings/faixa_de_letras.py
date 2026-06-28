def faixa_de_letras():
    """
    Uma faixa de letras é um conjunto de letras minúsculas
    alfabeticamente consecutivas tomadas de 'a' até 'z'.
    A menor e maior letras da faixa, separadas por dois pontos
    (o caractere ':'), são usadas para representar a faixa de
    letras. Por exemplo, a faixa "a:c" representa as letras
    consecutivas 'a', 'b' e 'c'. (as aspas não fazem parte da faixa).
    A faixa "w:z" representa as letras 'w', 'x', 'y' e 'z'. A faixa
    "m:m" representa apenas a letra 'm'.

    Entrada
    Cada linha de entrada é um caso de teste. Cada caso de teste contém
    uma string, que pode ser vazia e cujas letras podem não estar em
    ordem alfabética, de letras minúsculas (a-z) e espaços.

    A string conterá entre 0 e 50 caracteres, inclusive.

    Saída
    Para cada caso de teste de entrada, seu programa deverá imprimir as
    faixas de letras ordenadas alfabeticamente pelo menor valor de cada
    faixa. Faixas de letras a serem impressas devem representar a maior
    sequencia possível de letras de entrada em ordem crescente. Ignore
    espaços e letras duplicadas contidas na entrada.


    Se a string for vazia, apenas imprima uma nova linha.


    Por exemplo, a string "fb xee ac" tem três faixas de letras, "a:c"
    (as letras 'a', 'b' e 'c'), "e:f" (as letras 'e' e 'f') e "x:x"
    (a letra 'x'). Por favor, recorra aos exemplos.
    :return:
    """
    letras = input()
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']
    for i in letras:
        if i == ' ':
            letras = letras.replace(' ', '')
    lista = list(letras)
    lista = sorted(set(lista))
    print(lista)
    idx, inicio, fim = 0, '', ''
    for i in range(0, len(alfabeto)):
        if i > len(lista) - 1:
            break
        if i == 0:
            inicio = lista[idx]
        if i > 0:
            if lista[idx] == alfabeto[i]:
                pass
            else:
                fim = lista[idx - 1]
                print(f'{inicio}:{fim},', end=' ')
                inicio = lista[i]


faixa_de_letras()
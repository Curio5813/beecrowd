def justificador():
    """
    Nós temos algumas palavras e queremos justificá-las à direita, ou seja,
    alinhar todas elas à direita. Crie um programa que, após ler várias
    palavras, reimprima estas palavras com suas linhas justificadas à direita.

    Entrada
    A entrada contém diversos casos de testes. A primeira linha de cada caso de
    teste conterá um inteiro N (1 ≤ N ≤ 50), que indicará o número de palavras
    que virão a seguir. Cada uma das N palavras contém no mínimo uma letra e no
    máximo 50 letras maiúsculas (‘A’-‘Z’). O fim da entrada é indicado por N = 0.

    Saída
    Para cada caso de teste imprima as palavras inserindo tantos espaços quanto forem
    necessários à esquerda de cada palavra, para que elas apareçam todas alinhadas à
    direita e na mesma ordem da entrada. Deixe uma linha em branco entre os casos
    de teste. Não deixe espaços sobrando no final de cada linha nem imprima espaços
    desnecessários à esquerda, de modo que pelo menos uma das linhas impressa em cada
    texto inicie com uma letra.
    :return:
    """
    primeiro = True
    while True:
        palavras, maior = [], 0
        n = int(input())
        if n == 0:
            break
        for i in range(n):
            palavra = input()
            if len(palavra) > maior:
                maior = len(palavra)
            palavras.append(palavra)
        if not primeiro:
            print()
        for i in range(len(palavras)):
            print(f"{palavras[i]:>{maior}}")
        primeiro = False


justificador()

"""
3
BOB
TOMMY
JIM
4
JOHN
JAKE
ALANa
BLUE
4
LONGEST
A
LONGER
SHORT
0
"""

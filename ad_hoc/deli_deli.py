def deli_deli():
    """
    Sra. Deli está trabalhando em uma casa de mercearias finas "Deli Deli".
    No ano passado, a Sra. Deli decidiu expandir seu negócio e construir
    uma loja online. Ela contratou um programador que implementou a loja online.

    Recentemente alguns de seus novos clientes online reclamaram das notas fiscais
    eletrônicas. O programador esqueceu-se de usar o plural, no caso em que um item
    é comprado várias vezes. Infelizmente o programador da Sra. Deli está de férias
    e agora é sua tarefa de implementar esse recurso para a Sra. Deli. Aqui está
    uma descrição de como fazer o plural:

    Se a palavra está na lista de palavras irregulares substitua-a com o plural dado.
    Senão se a palavra termina em uma consoante seguida por "y", substitua "y" por "ies".
    Senão se a palavra termina em "o", "s", "ch", "sh" ou "x", acrescente "es" à palavra.
    Senão acrescente "s" à palavra.

    Entrada
    A primeira linha do arquivo de entrada consiste de dois inteiros L e N (0 ≤ L ≤ 20,
    1 ≤ N ≤ 100). As seguintes L linhas contém a descrição das palavras irregulares e
    sua forma plural. Cada linha é composta de duas palavras separadas por um caractere
    de espaço, onde a primeira palavra é o singular, a segunda palavra é a forma plural de
    uma palavra irregular. Depois da lista de palavras irregulares, as N linhas seguintes
    contém uma palavra cada, que você tem que transformar para o plural. Você pode assumir
    que cada palavra é composta de no máximo 20 letras minúsculas do alfabeto Inglês ('a' a 'z').

    Saída
    Imprima N linhas na saída, onde a i-ésima linha é a forma plural da i-ésima palavra de entrada.
    :return:
    """
    l, n = map(int, input().split(" "))
    irregulares = []
    for i in range(l):
        irregular = input().split(" ")
        irregulares.append(irregular)
    for i in range(n):
        flag = 0
        palavra = input()
        for j in range(0, len(irregulares)):
            if palavra in irregulares[j][0]:
                print(irregulares[j][1])
                flag = 1
                break
        if flag == 0:
            if palavra[-2] not in "aeiou" and palavra[-1] == "y":
                print(palavra[0:-1] + "ies")
                flag = 1
            if (palavra[-1] == "o" or palavra[-1] == "s" or palavra[-1] == "x"
                    or palavra[-2::] == "ch" or palavra[-2::] == "sh"):
                print(palavra + "es")
                flag = 1
            if flag == 0:
                print(palavra + "s")


deli_deli()

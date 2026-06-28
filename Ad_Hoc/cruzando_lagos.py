def cruzando_lagos():
    """
    O polo norte vem enfrentando um problema de logística devido ao aquecimento
    global. Isso se deve ao fato de que a fabrica e o armazém de brinquedos
    encontram-se em margens opostas de um lago que costumava estar congelado
    durante o ano inteiro. Entretanto com o aumento da temperatura nos últimos anos
    o gelo que cobre o lago vem ficando cada vez menos espesso. Para contornar o problema
    Balladug ,um gnomo élfico muito esperto, criou um radar que consegue mapear a espessura
    do gelo. Assim Balladug entregou o mapa do lago para os gnomos élficos encarregados
    do transporte. Tais gnomos conseguem pular numa distância máxima de 2 metros. Com o
    mapa em mãos, os gnomos de saber se é possível cruzar o lago de gelo com seus pulos e
    se for possível eles gostariam de saber quantos pulos terão que dar para tal.

    Entrada
    A entrada consiste de um número inteiro N (0<N<101) que representa a quantidade de linhas
    do mapa. As próximas N linhas contem até 10 caracteres onde o caractere "-" representa
    uma região de gelo firme e o caractere "." representa uma região de gelo fino que irá
    quebrar caso seja pisado. Cada linha representa um metro de largura no mapa.Considere
    que os gnomos iniciam no canto superior esquerdo e devem cruzar todo o lago até chegarem
     em qualquer posição da margem oposta que se encontra após a última linha do mapa.Uma
     linha sempre será composta inteiramente pelo mesmo caractere.

    Saída
    A saída consiste de um inteiro inteiro indicando o número de pulos para percorrer o lago
    ou do caractere "N"caso seja impossível cruzar o lago. Não esqueça de deixar uma linha
    em branco após a resposta.
    :return:
    """
    n = int(input())
    gelo = []
    for i in range(n):
        gelo.append(input())
    largura, pulos, flag = 0, 0, False
    for i in range(len(gelo)):
        if gelo[i][0] == "-" and flag == True and largura <= 2:
            pulos += 1
            largura = 0
            flag = False
        if gelo[i][0] == ".":
            largura += 1
            if largura >= 3:
                flag = True
                break
            flag = True
    if flag and largura >= 3:
        print("N")
    if not flag or largura <= 2:
        if pulos == 0:
            print(f"{pulos + 1}")
        else:
            print(f"{pulos}")


if __name__ == "__main__":
    cruzando_lagos()

def cultivando_strings():
    """
    Gene e Gina possuem um tipo peculiar de fazenda. Ao invés de criar
    animais e plantar vegetais como acontece em fazendas normais, eles
    cultivam strings. Uma string é uma sequência de caracteres. As strings,
    ao crescerem, adicionam caracteres à esquerda e/ou à direita delas mesmas,
    mas nunca perdem caracteres nem inserem caracteres no meio. Gene e Gina
    possuem uma coleção de fotos de algumas strings durante diferentes etapas
    de seus crescimentos. O problema é que a coleção não é rotulada, portanto
    eles esqueceram a qual string pertence cada uma das fotos. Eles querem montar
    um painel para ilustrar os procedimentos do cultivo de strings, mas eles
    necessitam sua ajuda para encontrar uma sequência de fotos apropriada.
    Cada foto ilustra uma string. A sequência de fotos precisa ter a seguinte
    propriedade: se Si aparece imediatamente antes de Si+1 na sequência, então
    Si+1 é uma string que pode ter crescido a partir de Si (ou seja, si é uma
    substring contígua de Si+1). Além disso, eles não querem usar fotos repetidas,
    portanto todas as strings na sequência devem ser diferentes. Dado um conjunto
    de strings representando todas as fotos disponíveis, sua tarefa é calcular o
    tamanho da maior sequência que pode ser produzida com as restrições acima.
    Cada caso de teste se estende por várias linhas. A primeira linha contém um
    inteiro N representando o número de strings no conjunto (1 ≤ N ≤ 104). Cada
    uma das próximas N linhas contém uma string não-vazia e única com no máximo
    1000 caracteres minúsculos do alfabeto inglês. Em cada caso de teste, a soma
    dos tamanhos das strings é no máximo 10^6. O último caso de teste é seguido
    de uma linha contendo um zero. A saída para cada caso de teste, imprime uma
    única linha com um único inteiro representando o tamanho da maior sequência
    de fotos que pode ser produzida.
    :return:
    """
    while True:
        n = input()
        n = int(n)
        if n == 0:
            break
        strs, tam, tams, cont, bol = [], 0, [], 1, 0
        for i in range(n):
            chars = input()
            strs.append(chars)
        for i in range(0, len(strs)):
            for k in range(0, len(strs)):
                if strs[i - 1].count(strs[i]) > 0:
                    bol = 1
                if bol == 1 and strs[k].count(strs[i]) > 0:
                    tam += 1
                else:
                    break
                cont += 1
            tams.append(tam)
            tam = 0
            bol = 0
        print(max(tams))


cultivando_strings()

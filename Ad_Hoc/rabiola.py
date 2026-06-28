def rabiola():
    """
    Todo ano, os moradores da cidade de Pipacicaba organizam o campeonato
    municipal de pipas. Neste lugar, eles utilizam um tipo especial de cipó
    para usar como rabiola da pipa. Este cipó é formado por uma fita única,
    formado por folhas normais e folhas aderentes. Nos exemplos, as folhas
    normais serão representadas por uma letra ‘o’ e as folhas aderentes,
    formadas por uma letra ‘x’. Para aproveitar as diversas cores dos cipós,
    cada pipa do campeonato pode apenas colocar uma única fita. Cada folha
    aderente deverá ser colada em um ponto único na base da pipa. Com isto,
    filetes de folhas normais são formados. Os dois filetes mais externos
    ficam, normalmente, sem dobras. Os filetes internos, sempre formados por
    uma quantidade par de folhas, são dobrados: Abaixo, temos um exemplo de
    cipó, e sua colocação na pipa:

    Cipó: ooxooooooxo

    Após colar as folhas aderentes, a rabiola ficará assim:

    ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1876.png)

    Os filetes aparecem separados na imagem para melhor visualização. Na verdade,
    os filetes ficam sobrepostos. Sua missão é fazer um algoritmo que, dado um
    cipó, informe o tamanho do maior filete de rabiola feito com o mesmo.

    Entrada
    A entrada possui múltiplos casos de teste. Cada caso de teste é dado em uma
    linha, que contém uma única palavra P composta apenas pelas letras ‘o’ ou ‘x’,
    representando um cipó. Essa palavra possui no máximo 100 caracteres. A entrada
    termina com o fim do arquivo.

    Saída
    Para cada caso de teste, imprima uma linha contendo um único inteiro N, que é
    o tamanho do maior filete de rabiola formado por este cipó.
    :return:
    """
    while True:
        try:
            filetes = input()
            tamanho1, tamanho2, tamanhos, k, j = 0, 0, [], 0, 0
            for i in range(0, len(filetes)):
                if filetes[i] == 'x':
                    k += 1
            for i in range(0, len(filetes)):
                if i == 0 and filetes[i] == 'o':
                    tamanho1 += 1
                elif i == 0 and filetes[i] == 'x':
                    j += 1
                elif i > 0 and filetes[i] == 'o' and j < 1 < k:
                    tamanho1 += 1
                elif i > 0 and filetes[i] == 'o' and j < k and k > 1:
                    tamanho2 += 1
                    if tamanho2 % 2 == 0:
                        tamanho1 += 1
                elif i > 0 and filetes[i] == 'o' and j < k <= 1:
                    tamanho1 += 1
                elif i > 0 and filetes[i] == 'x':
                    tamanhos.append(tamanho1)
                    tamanho1 = 0
                    tamanho2 = 0
                    j += 1
                elif filetes[i] == 'o' and j >= k:
                    tamanho1 += 1
            tamanhos.append(tamanho1)
            if len(tamanhos) == 0 and tamanho1 == 0:
                print(0)
            if len(tamanhos) == 0 and tamanho1 > 0:
                print(tamanho1)
            if len(tamanhos) > 0:
                print(max(tamanhos))
        except EOFError:
            break


rabiola()

def dobradura():
    """
    Zezinho tem aulas de Iniciação Artística em sua escola, e
    recentemente aprendeu a fazer dobraduras em papel. Ele ficou
    fascinado com as inúmeras possibilidades de se dobrar uma
    simples folha de papel. Como Zezinho gosta muito de matemática,
    resolveu inventar um quebra-cabeça envolvendo dobraduras. Zezinho
    definiu uma operação de dobradura D que consiste em dobrar duas
    vezes uma folha de papel quadrada de forma a conseguir um quadrado
    com 1/4 do tamanho original, conforme ilustrado na figura.

    ![](https://resources.beecrowd.com/gallery/images/contests/UOJ_150_C_a.png)

    Depois de repetir N vezes esta operação de dobradura D sobre o papel, Zezinho
    cortou o quadrado resultante com um corte vertical e um corte horizontal,
    conforme a figura abaixo.

    ![](https://resources.beecrowd.com/gallery/images/contests/UOJ_150_C_b.png)

    Zezinho lançou então um desafio aos seus colegas: quem adivinha quantos pedaços
    de papel foram produzidos?

    Entrada
    A entrada é composta de vários conjuntos de teste. Cada conjunto de teste é
    composto de uma única linha, contendo um número inteiro N (-1 ≤ N ≤ 15) que indica
    o número de vezes que a operação de dobradura D foi aplicada. O final da entrada
    é indicado por  N = -1.

    Saída
    Para cada conjunto de teste da entrada seu programa deve produzir três linhas na
    saída. A primeira linha deve conter um identificador do conjunto de teste, no formato
    “Teste n”, onde n é numerado a partir de 1. A segunda linha deve conter o número de
    pedaços de papel obtidos depois de cortar a dobradura, calculado pelo seu programa.
    A terceira linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída,
    abaixo, deve ser seguida rigorosamente.
    :return:
    """
    n = int(input())
    cont = 1
    while n != -1:
        numeros_pedacos = (2 ** n + 1) ** 2
        print(f"Teste {cont}")
        print(numeros_pedacos)
        print("")
        n = int(input())
        cont += 1


dobradura()

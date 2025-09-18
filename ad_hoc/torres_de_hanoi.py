def torres_de_hanoi():
    """
    O quebra-cabeças Torres de Hanoi é muito antigo e conhecido, sendo
    constituído de um conjunto de N discos de tamanhos diferentes e três
    pinos verticais, nos quais os discos podem ser encaixados.

    [imagem](https://resources.beecrowd.com/gallery/images/contests/UOJ_151_F.png)

    Cada pino pode conter uma pilha com qualquer número de discos, desde que
    cada disco não seja colocado acima de outro disco de menor tamanho. A
    configuração inicial consiste de todos os discos no pino 1. O objetivo do
    quebra-cabeças é mover todos os discos para um dos outros pinos, sempre obedecendo
    à restrição de não colocar um disco sobre outro menor.

    Um algoritmo para resolver este problema é o seguinte.

    procedimento Hanoi(N, Orig, Dest, Temp)

       se N = 1 então

          mover o menor disco do pino Orig para o pino Dest;

       senão

          Hanoi(N-1, Orig, Temp, Dest);

          mover o N-ésimo menor disco do pino Orig para o pino Dest;

          Hanoi(N-1, Temp, Dest, Orig);

       fim-se

    fim

    Sua tarefa é escrever um programa que determine quantos movimentos de trocar
    um disco de um pino para outro serão executados pelo algoritmo acima para
    resolver o quebra-cabeça.

    Entrada
    A entrada possui vários conjuntos de teste. Cada conjunto de teste é composto
    por uma única linha, que contém um único número inteiro N (0 ≤ N ≤ 30), indicando
    o número de discos. O final da entrada é indicado por N = 0.

    Saída
    Para cada conjunto de teste, o seu programa deve escrever três linhas na saída. A
    primeira linha deve conter um identificador do conjunto de teste, no formato “Teste n”,
    onde n é numerado seqüencialmente a partir de 1. A segunda linha deve conter o número
    de movimentos que são executados pelo algoritmo dado para resolver o problema das Torres
    de Hanói com N discos. A terceira linha deve ser deixada em branco. A grafia mostrada
    no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.
    :return:
    """
    n = int(input())
    cont = 1
    while n != 0:
        print(f"Teste {cont}")
        print(2 ** n - 1)
        print("")
        n = int(input())
        cont += 1

torres_de_hanoi()

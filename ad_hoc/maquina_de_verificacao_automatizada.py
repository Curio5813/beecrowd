def maquina_de_verificacao_automatizada():
    """
    A Internet Computer Parts Company (ICPC) é uma loja on-line
    que vende peças de computador. Pares de conectores elétricos
    em linha estão entre as peças mais populares que ICPC vende.
    No entanto, elas também são uma das peças que são devolvidos
    com mais freqüência por clientes insatisfeitos, porque devido
    a erros na embalagem os conectores enviados para os clientes
    podem não ser compatíveis..

    Um conector em-linha é constituído por cinco pontos de ligação,
    marcadas de 1 a 5. Cada ponto de ligação de um conector pode ser
    ou um plugue ou uma tomada. Dizemos dois conectores são compatíveis
    se, para cada rótulo, um ponto de conexão é um plugue e outro ponto
    de ligação é uma tomada (em outras palavras, dois conectores são
    compatíveis se, para cada ponto de conexão com o mesmo rótulo, um
    plugue e uma tomada se encontram quando os dois conectores estão
    conectados).

    ICPC está introduzindo uma Máquina de Verificação Automártica (ACM) de
    última geração, com um verificador óptico, que vai verificar se os dois
    conectores embalados para um cliente são realmente compatíveis. O
    complexo e caro hardware do ACM está pronto, mas eles precisam de sua
    ajuda para terminar o software.

    Dadas as descrições de um par de conectores em linha, sua tarefa é determinar
    se os conectores são compatíveis.

    Entrada
    A primeira linha contém cinco números inteiros Xi (0 ≤ Xi≤ 1 para i = 1, 2,..., 5),
    que representa os pontos de conexão do primeiro conector do par. A segunda linha contém
    cinco números inteiros Yi (0 ≤ Yi ≤ 1 para i = 1, 2,..., 5), que representa os pontos
    de conexão do segundo conector. Na entrada, um 0 representa uma tomada e um 1 representa
    um plugue.

    Saída
    Apresente uma linha com um caractere que representa se os conectores são compatíveis ou
    não. Se eles são compatíveis escrever a letra maiúscula "Y"; caso contrário, escrever a
    letra maiúscula "N".
    :return:
    """
    rotulo1 = list(map(int, input().split(" ")))
    rotulo2 = list(map(int, input().split(" ")))
    bol = 0
    for i in range(0, len(rotulo1)):
        if rotulo1[i] == 1 and rotulo2[i] == 0 or rotulo1[i] == 0 and rotulo2[i] == 1:
            bol = 1
        else:
            bol = 0
            break
    if bol == 1:
        print("Y")
    if bol == 0:
        print("N")


maquina_de_verificacao_automatizada()

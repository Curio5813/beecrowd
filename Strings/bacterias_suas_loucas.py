from copy import deepcopy

def bacterias_suas_loucas():
    """
    Um grupo de bactérias apresenta um comportamento muito peculiar: cada
    uma se identifica como um de dois tipos, e grupos do mesmo tipo, a
    cada segundo, se juntam e se transformam em um padrão de duas bactérias,
    e este padrão é determinado somente pelo tipo e número das bactérias no
    grupo. Portanto, bactérias de um tipo sozinhas se dividem em duas, grupos
    de duas bactérias do mesmo tipo continuam como um grupo de duas bactérias,
    mas eventualmente mudam de tipo, e grupos de mais bactérias se juntam
    para formarem somente duas.

    Por exemplo, suponha que a linha esteja AABAAABABB. Nela, temos 6 grupos:
    AA, B, AAA, B, A, e BB. Portanto, após 1 segundo, elas se tornarão uma linha
    de 12 bactérias, pois cada grupo se transformará em 2. Note que temos dois
    grupos iguais, os dois primeiros do tipo B, e portanto eles se transformarão
    no mesmo padrão. Digamos que um grupo A se transforme em BB, B em BA, AA em
    AA, BB em AB, e AAA em AB. Então, após um segundo, a linha que estamos
    considerando terá se transformado em AABAABBABBAB. As regras que as bactérias
    seguem nunca mudam, então após mais um segundo a linha fica como AABAAAABBBABBBBA.

    Um cientista conseguiu isolar uma única bactéria do tipo A, mas como o grupo em
    que ela se torna vai mudando tão rapidamente, ele não consegue mais obter observações
    relevantes sobre o grupo. Você pode ajudá-lo?

    Entrada
    Na primeira linha contém N (1 <= N <= 20), o número de segundos desde que a bactéria
    A foi isolada, e M (1 <= M <= 200), o número de regras que as bactérias seguem. Para
    cada uma das M linhas seguintes, vem um regra, composta de duas strings separadas por
    um espaço: a primeira é composta de várias letras iguais, A ou B, e a segunda é AA, AB,
    BA, ou BB. Assim, uma regra que diz que grupos de 3 bactérias do tipo A se transformam
    em BA é representada como: AAA BA.

    É garantido que as regras em um caso de teste são suficientes para determinar o comportamento
    das bactérias até o instante N.

    Saída
    Dois números, separados por espaço, representando respectivamente o número de bactérias do
    tipo A e do tipo B após N segundos de iterações.
    :return:
    """
    dados = list(map(int, input().split(" ")))
    segundos, regra = int(dados[0]), int(dados[1])
    transformacoes = "A"
    regras = {}
    for i in range(regra):
        bacteria, transfromacao = input().split(" ")
        regras[bacteria] = transfromacao
    for i in range(segundos):
        if i == 0:
            for chave, valor in regras.items():
                if chave in transformacoes:
                    transformacoes = transformacoes.replace(chave, valor)
                    # print(transformacoes)
        else:
            chave, valor = list(regras.items())[1]
            if chave in transformacoes:
                transformacoes = transformacoes.replace(chave, valor)
                # print(transformacoes)
    print(transformacoes)
    print(transformacoes.count('A'), transformacoes.count('B'))


bacterias_suas_loucas()

from math import log2, ceil


def contando_uns():
    """
    Carl é agora a criança mais feliz do mundo: ele aprendeu esta manhã o que
    é o sistema binário. Ele aprendeu, por exemplo, que a representação binária
    de um inteiro positivo k é  uma string anan−1 · · · a1a0 onde cada ai é um
    dígito binário 0 ou 1, iniciando com an = 1, e de tal forma que k = Σni=0 ai × 2i.
    É realmente bom ver ele transformando números decimais em binários, e depois
    somá-los e multiplicá-los.

    César é o irmão mais velho de Cal, e ele não suporta ver o seu irmão menor tão
    feliz. Por isso ele preparou um desafio: "Olhe Carl, eu tenho uma pergunta fácil
    para você: eu te darei dois inteiros A e B, e você tem que me dize quantos dígitos
    1 existem na representação binária de todos os inteiros de A à B, inclusive. Se
    prepare!". Carl aceitou o desafio.

    Após alguns minutos, ele voltou com uma lista com a representação binária de todos os
    inteiros de 1 a 100. "César, eu estou pronto". César sorriu e disse: "Bom, deixe-me ver,
    eu escolho A = 1015
    e B = 1016. A sua lista não será útil".

    Carl odeia perder para o seu irmão então ele precisa de uma solução mais rápida. Você pode
    ajudá-lo?

    Entrada
    A entrada é composta por diversos casos de teste e termina com EOF. Cada caso de teste
    consiste de uma linha com dois inteiros A e B (1 ≤ A ≤ B ≤ 1016).

    Saída
    Para cada caso de teste, imprima uma linha contendo um inteiro que representa o número total
    de dígitos 1 na representação binária de todos os inteiros de A to B, inclusive.
    :return:
    """
    while True:
        try:
            inteiro = input().split(" ")
            a, b = int(inteiro[0]), int(inteiro[1])
            a_log = ceil(log2(a))
            print(a_log)
        except EOFError:
            break


contando_uns()

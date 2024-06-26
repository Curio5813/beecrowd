def conta_de_agua():
    """
    A empresa local de abastecimento de água, a Saneamento Básico da
    Cidade (SBC), está promovendo uma campanha de conservação de água,
    distribuindo cartilhas e promovendo ações demonstrando a importância
    da água para a vida e para o meio ambiente.

    Para incentivar mais ainda a economia de água, a SBC alterou os preços
    de seu fornecimento de forma que, proporcionalmente, aqueles clientes
    que consumirem menos água paguem menos pelo metro cúbico. Todo cliente
    paga mensalmente uma assinatura de R$ 7, que inclui uma franquia de 10 m³
    de água. Isto é, para qualquer consumo entre 0 e 10 m³ , o consumidor
    paga a mesma quantia de R$ 7 reais (note que o valor da assinatura deve
    ser pago mesmo que o consumidor não tenha consumido água). Acima de 10 m³
    cada metro cúbico subsequente tem um valor diferente, dependendo da faixa
    de consumo. A SBC cobra apenas por quantidades inteiras de metros cúbicos
    consumidos. A tabela abaixo especifica o preço por metro cúbico para cada
    faixa de consumo:

    ------------------------------------------------------------------------
    |       FAIXA DE CONSUMO (M³)             |         PREÇO (POR M³)     |
    -----------------------------------------------------------------------
    |            ATÉ 10                       |    INCLUÍDO NA FRANQUIA    |
    |           11 À 30                       |            R$ 1            |
    |           31 À 100                      |            R$ 2            |
    |         101 EM DIANTE                   |            R$ 3            |
    ------------------------------------------------------------------------

    Assim, por exemplo, se o consumo foi de 120 m³ , o valor da conta é:

    7 reais da assinatura básica;
    20 reais pelo consumo no intervalo 11 - 30 m³;
    140 reais pelo consumo no intervalo 31 - 100 m³;
    100 reais pelo consumo no intervalo 101 - 120 m³.
    Logo o valor total da conta de água é R$ 267.

    Escreva um programa que, dado o consumo de uma residência em m3, calcula o valor
    da conta de água daquela residência.

    Entrada
    A única linha da entrada contém um único inteiro N, indicando o consumo de água
    da residência, em m³ (0 ≤ N ≤ 10³).

    Saída
    Seu programa deve imprimir uma única linha, contendo o valor da conta de água
    daquela residência.
    :return:
    """
    n = int(input())
    valor = 0
    if n <= 10:
        valor = 7
        print(valor)
    if 11 <= n <= 30:
        valor += 7
        valor += n - 10
        print(valor)
    if 31 <= n <= 100:
        valor += 7
        valor += 20
        valor += (n - 30) * 2
        print(valor)
    if n >= 101:
        valor += 7
        valor += 20
        valor += 140
        valor += (n - 100) * 5
        print(valor)


conta_de_agua()

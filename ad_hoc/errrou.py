def errrou():
    """
    Tausfão apresenta um programa de televisão o qual dá prêmios
    aos participantes que respondem corretamente a cálculos matemáticos.
    Quando os participantes erram, ele ressalta o quão longe a resposta
    está da esperada. Levando em consideração somente as respostas erradas,
    ajude o Tausfão informando como deve ser a pronúncia do erro do participante.

    Entrada
    A entrada é composta por vários casos de teste. A primeira linha contém um
    número inteiro C, representando a quantidade de casos de teste. As próximas
    C linhas serão formadas por um número inteiro, seguido por um espaço, um
    caractere de operação (adição, subtração ou multiplicação), outro número
    inteiro, mais um espaço, um sinal de igualdade, outro espaço e, por fim,
    um número inteiro, representando o resultado dito pelo participante em relação
    ao referido cálculo do caso de teste.

    Saída
    Para cada caso de teste de entrada do seu programa, imprima a expressão “Errou!”,
    baseada na distância da resposta do participante em relação à resposta corre
    :return:
    """
    c = int(input())
    for i in range(c):
        cont = 0
        operacao = input().split(" ")
        num1 = int(operacao[0])
        sinal = operacao[1]
        num2 = int(operacao[2])
        resultado = int(operacao[4])
        errs = ""
        if sinal == '+':
            soma = num1 + num2
            diff = abs(soma - resultado)
            while cont < diff:
                errs += "r"
                cont += 1
            print(f"E{errs}ou!")
        if sinal == '-':
            sub = abs(num1 - num2)
            diff = abs(sub - resultado)
            while cont < diff:
                errs += "r"
                cont += 1
            print(f"E{errs}ou!")
        if sinal == 'x':
            mult = num1 * num2
            diff = abs(mult - resultado)
            while cont < diff:
                errs += "r"
                cont += 1
            print(f"E{errs}ou!")


errrou()

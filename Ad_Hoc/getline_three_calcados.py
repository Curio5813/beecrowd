def getline_three_calcados():
    """
    Agora que Mangojata resolveu alguns problemas que utilizavam getline,
    acha que está apta a dar um passo adiante. Ela está prestes a fazer
    um novo programa para auxiliar a sua irmã, Overlaine. Overlaine é
    vendedora de calçados e por um acidente, misturou todos os pares de
    calçados que tinha para vender. Ela quer informar um número qualquer
    N e contar quantos calçados de uma determinada caixa são deste tamanho
    (N). O problema é que Overlaine não tem a menor idéia de quantos calçados
    existem em cada caixa. A única coisa que sabe é que cada calçado pode
    ter numeração de 20 a 44, podendo ser masculino ou feminino.

    Entrada
    A entrada contém vários casos de teste e termina com EOF (Fim de Arquivo).
    Cada caso de teste consiste de duas linhas de entrada. A primeira linha
    contém uma numeração N (20 ≤ N ≤ 44) de calçado que Overlaine informa e
    a segunda linha contém o número de cada par que está dentro da caixa seguido
    de M ou F indicando se o par é de calçado Masculino ou Feminino.

    Saída
    Para cada caso de teste imprima quatro linhas, conforme exemplo abaixo.
    A primeira linha deve apresentar a mensagem “Caso n:”, onde n é o número
    do caso de teste. A segunda linha deve informar quantos pares da caixa
    de calçados são iguais ao número que Overlaine quer encontrar, com mensagem
    correspondente. Seguem duas linhas com a quantidade respectiva de calçados
    Femininos (F) e Masculinos (M), com mensagem correspondente.

    Imprima uma linha em branco entre as saídas de dois casos de teste consecutivos.
    :return:
    """
    cont = 0
    while True:
        try:
            n = input()
            qt_total, qt_f, qt_m = 0, 0, 0
            sapatos = input().split(" ")
            cont += 1
            if cont > 1:
                print("")
            for i in range(0, len(sapatos)):
                if i % 2 == 0 and sapatos[i] == n:
                    qt_total += 1
                    if sapatos[i + 1] == "F":
                        qt_f += 1
                    if sapatos[i + 1] == "M":
                        qt_m += 1
            print(f"Caso {cont}:")
            print(f"Pares Iguais: {qt_total}")
            print(f"F: {qt_f}")
            print(f"M: {qt_m}")
        except EOFError:
            break


getline_three_calcados()

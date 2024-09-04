def dividindo_com_fink():
    """
    A raposa Fink, muito esperta, precisa dividir meio a meio algumas
    comidas entre ele e Pica-Pau, mas ele está com muita fome e pensou
    em algo muito sagaz para sair ganhando nessa, a divisão vai ser da
    seguinte forma:

    Primeiro ele coloca tudo sobre a mesa e começa a dividir: Um pra você.
    Um pra mim. Dois pra você. Um, dois pra mim. Três pra você. Um, dois,
    três pra mim... Dessa forma, se a quantidade inicial de comida fosse 12,
    ele terminaria com 10 e Pica-Pau com 2. Obs: Caso Fink não consiga terminar
    a última divisão, ele pode roubar do Pica-Pau.

    ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_2171.jpg)

    Entrada
    A entrada consistirá de uma série de linhas, cada uma contendo o número de
    comidas N (1 ≤ N ≤ 100000). O fim da entrada é indicado pelo número zero (0).

    Saída
    Para cada linha de entrada, você deverá imprimir quanta comida ficou com Fink
    e Pica-Pau ao final da divisão, separadas por um espaço.
    :return:
    """
    while True:
        n = int(input())
        raposa, picapau, comida, usura, roubo, flag = 0, 0, n, 0, 0, 0
        for i in range(1, n + 1):
            picapau += 1
            if raposa + picapau >= comida:
                usura = comida - (raposa + picapau)
                flag = 1
                break
            for j in range(1, i + 1):
                raposa += j
                if raposa + picapau >= comida:
                    break
        # print(raposa, picapau, usura)
        usura *= -1
        picapau -= usura
        # print(raposa, picapau, usura)
        if flag == 1:
            while raposa <= comida or usura > 0:
                picapau -= 1
                raposa += 1
                usura -= 1
                if usura == 0 or picapau == 0:
                    break
                # print(raposa, picapau, usura)
        print(raposa, picapau)


dividindo_com_fink()

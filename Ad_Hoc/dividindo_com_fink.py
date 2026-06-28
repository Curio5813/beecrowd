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
        raposa, picapau, comida, flag, div_raposa, div_picapau = 0, 0, n, 0, 0, 0
        for i in range(1, n + 1):
            picapau += 1
            div_picapau = picapau
            for j in range(1, i + 1):
                if div_raposa + div_picapau > comida:
                    flag = 1
                else:
                    raposa += j
            if flag == 1:
                pass
            else:
                div_raposa = raposa
                raposa = 0
        while div_raposa + picapau > comida:
            picapau -= 1
        print(div_raposa, picapau)


dividindo_com_fink()

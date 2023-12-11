def velocidade_media():
    """
    Você comprou um carro para dirigir de Waterloo para uma cidade grande.
    O odômetro do seu carro está quebrado, então você não pode medir a distância.
    Mas o velocímetro e o Cruise Control (sistema que mantém a velocidade,
    previamente programada, do veículo constante) estão funcionando, de modo
    que o carro pode manter uma velocidade constante, que pode ser ajustada de
    tempos em tempos em resposta aos limites de velocidade, engarrafamentos ou
    filas nas fronteiras. Você tem um cronômetro e anota o tempo decorrido toda
    vez que a velocidade muda. De vez em quando você se pergunta: “O quão longe
    eu estou?”. Para resolver este problema, você deve escrever um programa para
    ser executado em seu computador portátil no banco do passageiro.

    Entrada
    A entrada padrão contém várias linhas de entrada: Cada alteração de velocidade
    é indicada por uma linha específica com o tempo decorrido desde o início da
    viagem (hh:mm:ss), seguido da nova velocidade em km/h. Cada consulta é indicada
    por uma linha que contém o tempo decorrido. No início da viagem o carro está parado.
    O tempo decorrido é dado em ordem não decrescente e há, no máximo, uma variação de
    velocidade por linha de entrada.

    Saída
    Para cada consulta na entrada padrão, você deve imprimir uma linha dando o tempo e
    a distância percorrida, no formato abaixo, utilizando o arredondamento padrão da
    linguagem.
    :return:
    """
    dist, v, cont1, cont2, cont3, seg1 = 0, 0, 0, 0, 0, 0
    while True:
        try:
            entrada = input().split(" ")
            if len(entrada) == 2 and cont2 == 0:
                hour, minutes, seg = entrada[0].split(":")
                hour, minutes, seg = int(hour), int(minutes), int(seg)
                seg1 = 60 * 60 * hour + 60 * minutes + seg
                v = float(entrada[1]) / 3.6
                cont1 = 1
                cont2 += 1
            elif len(entrada) == 2 and cont2 > 0:
                hour, minutes, seg = entrada[0].split(":")
                hour, minutes, seg = int(hour), int(minutes), int(seg)
                seg1 = 60 * 60 * hour + 60 * minutes + seg
                v = float(entrada[1]) / 3.6
                dist += (v * seg1) / 1000
                cont1 = 1
                cont2 += 1
            elif len(entrada) == 1:
                if cont1 == 1 and cont3 == 0:
                    hour, minutes, seg = entrada[0].split(":")
                    hour, minutes, seg = int(hour), int(minutes), int(seg)
                    seg = 60 * 60 * hour + 60 * minutes + seg - seg1
                    seg1 = seg
                    dist += (v * seg) / 1000
                    print(f"{entrada[0]} {dist:.2f} km")
                    cont3 += 1
                elif cont1 == 1 and cont3 > 0:
                    hour, minutes, seg = entrada[0].split(":")
                    hour, minutes, seg = int(hour), int(minutes), int(seg)
                    seg = 60 * 60 * hour + 60 * minutes - seg1
                    seg1 = seg
                    dist += (v * seg) / 1000
                    print(f"{entrada[0]} {dist:.2f} km")
                if cont1 == 0 and cont2 == 0:
                    hour, minutes, seg = entrada[0].split(":")
                    hour, minutes, seg = int(hour), int(minutes), int(seg)
                    seg = 60 * 60 * hour + 60 * minutes + seg - seg1
                    seg1 = seg
                    dist += (v * seg) / 1000
                    print(f"{entrada[0]} {dist:.2f} km")
        except EOFError:
            break


velocidade_media()

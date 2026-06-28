def relogio_binario():
    """
    Alguns programadores gostam de ser estranhos e usam relógios binários
    como o relógio da imagem abaixo:

    [imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_1561.jpg)

    Há também programadores que gostam de inventar questões para competições
    online, porém não gostam de escrever textos detalhados e longos para as
    questões.

    Sua tarefa nesse problema é desenhar o relógio da imagem em um dado horário.

    Entrada
    A entrada é composta por vários casos de teste. Cada caso de teste é composto
    por uma linha conténdo um horário no formato HH:MM (0 ≤ HH < 12 e 0 ≤ MM < 60).
    A entrada termina com final de arquivo (EOF).

    Saída
    Para cada teste, a saída é composta por um desenho do relógio no horário dado
    na entrada (o desenho deve seguir o mesmo formato dos desenho dos exemplos).
    Imprima uma linha em branco após cada desenho.
    :return:
    """
    while True:
        try:
            horario = list(map(int, input().strip().split(":")))
            horas = horario[0]
            minutos = horario[1]
            marca_hora = [" ", " ", " ", " "]
            marca_minutos = [" ", " ", " ", " ", " ", " "]
            binario_horas = [8, 4, 2, 1]
            binario_minutos = [32, 16, 8, 4, 2, 1]
            soma_horas = 0
            soma_minutos = 0
            if horas % 2 == 1:
                marca_hora[-1] = "o"
                soma_horas += 1
                for i in range(0, len(binario_horas) - 1):
                    if i == 0 and horas >= binario_horas[i]:
                        marca_hora[0] = "o"
                        soma_horas += binario_horas[i]
                        if soma_horas == horas:
                            break
                    if i == 0 and horas < binario_horas[i]:
                        pass
                    if i > 0:
                        soma_horas += binario_horas[i]
                        if soma_horas > horas:
                            soma_horas -= binario_horas[i]
                        elif soma_horas == horas:
                            marca_hora[i] = "o"
                            break
                        elif soma_horas < horas:
                            marca_hora[i] = "o"
            if horas % 2 == 0 and horas > 0:
                for i in range(0, len(binario_horas) - 1):
                    if i == 0 and horas >= binario_horas[i]:
                        marca_hora[0] = "o"
                        soma_horas += binario_horas[i]
                        if soma_horas == horas:
                            break
                    if i == 0 and horas < binario_horas[i]:
                        pass
                    if i > 0:
                        soma_horas += binario_horas[i]
                        if soma_horas > horas:
                            soma_horas -= binario_horas[i]
                        elif soma_horas == horas:
                            marca_hora[i] = "o"
                            break
                        elif soma_horas < horas:
                            marca_hora[i] = "o"
            if minutos % 2 == 1:
                marca_minutos[-1] = "o"
                soma_minutos += 1
                for i in range(0, len(binario_minutos) - 1):
                    if i == 0 and minutos >= binario_minutos[i]:
                        marca_minutos[0] = "o"
                        soma_minutos += binario_minutos[i]
                        if soma_minutos == minutos:
                            break
                    if i == 0 and minutos < binario_minutos[i]:
                        pass
                    if i > 0:
                        soma_minutos += binario_minutos[i]
                        if soma_minutos > minutos:
                            soma_minutos -= binario_minutos[i]
                        elif soma_minutos == minutos:
                            marca_minutos[i] = "o"
                            break
                        elif soma_minutos < minutos:
                            marca_minutos[i] = "o"
            if minutos % 2 == 0 and minutos > 0:
                for i in range(0, len(binario_minutos) - 1):
                    if i == 0 and minutos >= binario_minutos[i]:
                        marca_minutos[0] = "o"
                        soma_minutos += binario_minutos[i]
                        if soma_minutos == minutos:
                            break
                    if i == 0 and minutos < binario_minutos[i]:
                        pass
                    if i > 0:
                        soma_minutos += binario_minutos[i]
                        if soma_minutos > minutos:
                            soma_minutos -= binario_minutos[i]
                        elif soma_minutos == minutos:
                            marca_minutos[i] = "o"
                            break
                        elif soma_minutos < minutos:
                            marca_minutos[i] = "o"
            print(" ____________________________________________")
            print("|                                            |")
            print("|    ____________________________________    |_")
            print("|   |                                    |   |_)")
            print("|   |   8         4         2         1  |   |")
            print("|   |                                    |   |")
            print(f"|   |   {marca_hora[0]}         {marca_hora[1]}         {marca_hora[2]}         {marca_hora[3]}  |   |")
            print("|   |                                    |   |")
            print("|   |                                    |   |")
            print(f"|   |   {marca_minutos[0]}     {marca_minutos[1]}     {marca_minutos[2]}     {marca_minutos[3]}     {marca_minutos[4]}     {marca_minutos[5]}  |   |")
            print("|   |                                    |   |")
            print("|   |   32    16    8     4     2     1  |   |_")
            print("|   |____________________________________|   |_)")
            print("|                                            |")
            print("|____________________________________________|")
            print("")
        except EOFError:
            break


relogio_binario()

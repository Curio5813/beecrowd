from datetime import timedelta


def a_mudanca_continua():
    """
    Está função imprime um saudação de "Bom Dia", "Boa Tarde",
    "Boa Noite" ou "De Madrugada", e calcula a hora exata do dia,
    hora, minutos e segundos com base, medidos em graus da posição
    do sol ou da lua no céu.
    :return:
    """
    while True:
        try:
            graus = float(input())
            angulo_sec = (graus / (1/240) + 21600)
            horario = str(timedelta(seconds=angulo_sec))
            horario = horario.split(" ")
            if 0 <= graus < 90:
                print("Bom Dia!!")
                if len(horario[0]) == 8:
                    print(horario[0])
                elif len(horario) < 8:
                    print("0" + horario[0])
            elif 90 <= graus < 180:
                print("Boa Tarde!!")
                print(horario[0])
            elif 180 <= graus < 270:
                print("Boa Noite!!")
                print(horario[0])
            elif 270 <= graus <= 360:
                print("De Madrugada!!")
                if len(horario[2]) == 8:
                    print(horario[2])
                elif len(horario) < 8:
                    print("0" + horario[2])
        except EOFError:
            break


a_mudanca_continua()

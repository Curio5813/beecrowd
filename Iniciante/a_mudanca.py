def a_mudanca():
    """
    Esta função calcula em que hora do dia se encontra
    uma pessoa, dada os valores do angulo do sol e da lua, e
    retorna um printe com a saída uma saudação, conforme
    cada caso, "Bom Dia!!", "Boa Tarde!!", "Boa Noite!!" e
    "De Madrugada!!"
    :return:
    """
    while True:
        try:
            angulo = int(input())
            if angulo == 360 or 0 <= angulo < 90:
                print("Bom Dia!!")
            elif 90 <= angulo < 180:
                print("Boa Tarde!!")
            elif 180 <= angulo < 270:
                print("Boa Noite!!")
            elif 270 <= angulo < 360:
                print("De Madrugada!!")
        except EOFError:
            return


a_mudanca()

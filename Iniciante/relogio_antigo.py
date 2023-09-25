def relogio_antigo():
    """
    Esta função calcula a hora e o minuto baseado no angulo
    formado pelas horas e minutos e seus respectivos marcadores
    do relogio. Cada marcação do ponteiro equivale a 6°, tanto
    para horas, como para os minutos. A entrada consiste em
    vários casos de teste e é finalizada pelo fim de arquivo (EOF).
    Cada linha corresponde a um caso de teste e contém dois valores
    inteiros h e m (0 ≤ h, m < 360) que são, respectivamente, os
    ângulos medidos sobre os ponteiros de hora e de minuto. Na saída
    é imprimssa uma única linha com o valor da hora e do minuto no
    formato "hh:mm" (sem aspas).
    :return:
    """
    while True:
        try:
            h, m = map(int, input().split(" "))
            h = round((h * 12) / 360)
            m = round((m * 60) / 360)
            if m == 60:
                m = 0
            if h < 10:
                if m < 10:
                    print(f"0{h}:0{m}")
                elif m >= 10:
                    print(f"0{h}:{m}")
            elif h >= 10:
                if m >= 10:
                    print(f"{h}:{m}")
                if m < 10:
                    print(f"{h}:0{m}")
        except EOFError:
            break


relogio_antigo()

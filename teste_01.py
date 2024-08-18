from math import sqrt


def geometria_por_que_nao():
    """
    :return:
    """
    k = 0
    while True:
        caminhos = input()
        x, y, base_menor, base_maior, altura, area, cont, m, flag = 0, 0, 0, 0, 1, 0, 0, 1, 0
        if caminhos == "S":
            break
        else:
            k += 1
            for i in range(0, len(caminhos)):
                if caminhos[i] == "R":
                    x += 1
                if caminhos[i] == "U":
                    y += 1
            if x > 0:
                m = y / x
            if m > 0 and x > 0 and y > 0:
                base_menor = 3 - (1 / m)
                # print(base_menor)
                for i in range(0, len(caminhos)):
                    if caminhos[i] == "R" and caminhos[i + 1] == 'S' and flag == 1:
                        area -= 1
                        # print(round(base_maior, 3), round(base_menor, 3), round(altura), round(area, 3), "Ok-1")
                        break
                    if caminhos[i] == "R":
                        base_maior += 1
                        # print(round(base_maior, 3), round(base_menor, 3), round(altura), round(area, 3), "Ok0")
                    if caminhos[i] == "U":
                        base_menor = abs(base_maior - base_menor)
                        if base_menor == 0 and base_maior != altura:
                            altura = base_maior * m
                            area += base_maior * altura / 2
                           # print(round(base_maior, 3), round(base_menor, 3), round(altura), round(area, 3), "Ok1")
                            base_maior = altura
                        elif 0 < base_menor <= 2:
                            area += ((base_menor + base_maior) / 2)
                            # print(round(base_maior, 3), round(base_menor, 3), round(altura), round(area, 3), "Ok2")
                            base_maior = base_menor
                        elif 0 < base_menor <= 2 and base_menor == altura:
                            area += ((base_menor * base_maior) / 2)
                            # print(round(base_maior, 3), round(base_menor, 3), round(altura), round(area, 3), "Ok3")
                            base_maior = base_menor
                        elif base_menor > 0 and base_menor > 2:
                            flag = 1
                            area += 1
                            # print(round(base_maior, 3), round(base_menor, 3), round(altura), round(area, 3), "Ok4")
                            base_maior = altura
            else:
                area = 0
            print(f"{k}. {area:.3f}")


geometria_por_que_nao()


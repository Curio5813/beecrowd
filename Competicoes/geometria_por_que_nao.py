from math import sqrt


def geometria_por_que_nao():
    """
    :return:
    """
    k = 0
    while True:
        caminhos = input()
        (x, y, m, i, base, altura, area, reta_h,
         sobras1, sobras2, sobras3, pontos_y , achados) = (0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [])
        if caminhos == "S":
            break
        else:
            k += 1
            for j in range(0, len(caminhos)):
                if caminhos[j] == "R":
                    x += 1
                if caminhos[j] == "U":
                    y += 1
            if x > 0:
                m = round(y / x, 3)
            if m > 0 and x > 0 and y > 0:
                x, y = 0, 0
                while i < len(caminhos) - 1:
                    if caminhos[i] == "S":
                        break
                    if caminhos[i] == "R":
                        base += 1
                        x += 1
                        i += 1
                        while caminhos[i] == "R":
                            i += 1
                            if i >= len(caminhos) - 1:
                                break
                            base += 1
                            x += 1
                    if caminhos[i] == "U":
                        altura += 1
                        y += 1
                        i += 1
                        while caminhos[i] == "U":
                            i += 1
                            if i >= len(caminhos) - 1:
                                break
                            altura += 1
                            y += 1
                    reta_h = round(base * m, 3)
                    if reta_h > altura:
                        altura_menor = round(reta_h - altura, 3)
                        base_menor = round(altura_menor / m, 3)
                        area1 = round(((base_menor + base) * altura) / 2, 3)
                        area2 = round(altura_menor * base_menor / 2, 3)
                        area += round(area1 + area2, 3)
                        sobras1.append(area2)
                        # print(area, base, base_menor, reta_h, altura, altura_menor, "Ok0")
                        base = round(base_menor, 3)
                        altura = 0
                    if reta_h <= altura:
                        base = round(base, 3)
                        altura1 = round(base * m, 3)
                        area += altura1 * base / 2
                        area = round(area, 3)
                        base2 = round(base - altura1, 3)
                        base3 = round(base - base2, 3)
                        altura2 = round(base2 * m, 3)
                        altura3 = round(base3 * m, 3)
                        area3 = round(base3 * altura2, 3)
                        # print(area, area3, base, altura2, altura3, base2, base3, "Ok1")
                        sobras2.append(area3)
                        pontos_y.append(y)
                        altura2 = round(altura - altura1, 3)
                        altura -= altura2
                        altura = round(altura, 3)
                        # print(area, base, altura, altura1, altura2, x, y, "Ok3")
                        base = 0
                    if len(pontos_y) >= 2:
                        for n in range(0, len(pontos_y)):
                            if pontos_y.count(pontos_y[n]) >= 2 and pontos_y[n] not in achados:
                                sobras3.append(sobras2[pontos_y.index(pontos_y[n])])
                                achados.append(pontos_y[n])
                if len(sobras1) > 0:
                    area -= sum(sobras1)
                if len(sobras3) > 0:
                    area -= sum(sobras3)
                print(f"{k}. {area:.3f}")
            elif m == 0 or x == 0 or y == 0:
                area = 0
                print(f"{k}. {area:.3f}")


geometria_por_que_nao()

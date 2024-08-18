from math import sqrt


def geometria_por_que_nao():
    """
    :return:
    """
    k = 0
    while True:
        caminhos = input()
        (x, y, m, i, base, altura, area1, area, reta_h,
         sobras, sobras2, altura1, altura2, cont) = 0, 0, 0, 0, 0, 0, 0, 0, 0, [], [], 0, 0, 0
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
                m = y / x
            if m > 0 and x > 0 and y > 0:
                x, y = 0, 0
                while i < len(caminhos) - 1:
                    if caminhos[0] == "R":
                        base += 1
                        i += 1
                        x += 1
                        while caminhos[i] == "R":
                            base += 1
                            i += 1
                            x += 1
                    if caminhos[0] == "U":
                        altura += 1
                        i += 1
                        y += 1
                        while caminhos[i] == "U":
                            altura += 1
                            i += 1
                            y += 1
                    if i > 0:
                        if caminhos[i] == "R":
                            if caminhos[i] == "R":
                                base += 1
                                i += 1
                                x += 1
                                while caminhos[i] == "R":
                                    base += 1
                                    i += 1
                                    x += 1
                        if caminhos[i] == "U":
                            a = y
                            if caminhos[i] == "U":
                                altura += 1
                                i += 1
                                y += 1
                                while caminhos[i] == "U":
                                    altura += 1
                                    i += 1
                                    y += 1
                            if y == a:
                                cont += 1
                        reta_h = base * m
                        if cont < 2 and len(sobras2) > 0:
                            print(sobras2)
                            cont = 0
                        if reta_h > altura:
                            altura_menor = reta_h - altura
                            base_menor = altura_menor / m
                            area1 = ((base_menor + base) * altura) / 2
                            area2 = altura_menor * base_menor / 2
                            area += area1 + area2
                            sobras.append(area2)
                            print(area, base, base_menor, reta_h, altura, altura_menor, "Ok0")
                            base = base_menor
                            altura = 0
                        if reta_h < altura:
                            altura1 = base * m
                            area += altura1 * base / 2
                            base2 = base - altura1
                            base3 = base - altura1
                            altura2 = base2 * m
                            altura3 = base3 * m
                            area2 = base2 * altura2
                            print(area2, base, altura2, altura3, base2, base3, "Ok2.5")
                            sobras2.append(area2)
                            altura2 = altura - altura1
                            altura -= altura2
                            print(area, base, altura, altura1, altura2, x, y, "Ok3")
                            base = 0
            if len(sobras) > 0:
                print(sobras, sobras2)
                area -= sum(sobras) + sobras2[1]
                print(f"{k}. {area:.3f}")
            else:
                area = 0
                print(f"{k}. {area:.3f}")




geometria_por_que_nao()

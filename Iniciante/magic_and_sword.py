def magic_and_sword():
    """
    Esta função calcula se uma determinada magia, em um jogo de RPG,
    atinge ou não as unidades inimigas. Cada magia tem um determinado
    dano que é maior a cada nível, do 1 ao 3. A magia afeta as unidades
    inimigas se o raio da circunferenica, com o centro dado como
    entrada corta ou não as aretas de retangulo também dado pelo problema.
    :return:
    """
    t = int(input())
    for i in range(t):
        w, h, x0, y0 = map(int, input().split(" "))
        m, n, cx, cy = input().split(" ")
        n, cx, cy = int(n), int(cx), int(cy)
        if m == "fire":
            if n == 1:
                if n == 1:
                    if x0 < cx < x0 + w and y0 < cy < y0 + h:
                        print(200)
                    elif abs(cx - x0) > 20 or abs(cy - y0) > 20:
                        print(0)
                    elif abs(cx - x0 + w) > 20 or abs(cy - y0 + h) > 20:
                        print(0)
                    else:
                        print(200)
                elif n == 2:
                    if x0 < cx < x0 + w and y0 < cy < y0 + h:
                        print(200)
                    elif abs(cx - x0) > 30 or abs(cy - y0) > 30:
                        print(0)
                    elif abs(cx - x0 + w) > 30 or abs(cy - y0 + h) > 30:
                        print(0)
                    else:
                        print(200)
                elif n == 3:
                    if x0 < cx < x0 + w and y0 < cy < y0 + h:
                        print(200)
                    elif abs(cx - x0) > 50 or abs(cy - y0) > 50:
                        print(0)
                    elif abs(cx - x0 + w) > 50 or abs(cy - y0 + h) > 50:
                        print(0)
                    else:
                        print(200)
        elif m == "water":
            if n == 1:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(300)
                elif abs(cx - x0) > 10 or abs(cy - y0) > 10:
                    print(0)
                elif abs(cx - x0 + w) > 10 or abs(cy - y0 + h) > 10:
                    print(0)
                else:
                    print(300)
            elif n == 2:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(300)
                elif abs(cx - x0) > 25 or abs(cy - y0) > 25:
                    print(0)
                elif abs(cx - x0 + w) > 25 or abs(cy - y0 + h) > 25:
                    print(0)
                else:
                    print(300)
            elif n == 3:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(300)
                elif abs(cx - x0) > 40 or abs(cy - y0) > 40:
                    print(0)
                elif abs(cx - x0 + w) > 40 or abs(cy - y0 + h) > 40:
                    print(0)
                else:
                    print(300)
        elif m == "earth":
            if n == 1:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(300)
                elif abs(cx - x0) > 25 or abs(cy - y0) > 25:
                    print(0)
                elif abs(cx - x0 + w) > 25 or abs(cy - y0 + h) > 25:
                    print(0)
                else:
                    print(300)
            elif n == 2:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(300)
                elif abs(cx - x0) > 55 or abs(cy - y0) > 55:
                    print(0)
                elif abs(cx - x0 + w) > 55 or abs(cy - y0 + h) > 55:
                    print(0)
                else:
                    print(300)
            elif n == 3:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(300)
                elif abs(cx - x0) > 70 or abs(cy - y0) > 70:
                    print(0)
                elif abs(cx - x0 + w) > 70 or abs(cy - y0 + h) > 70:
                    print(0)
                else:
                    print(300)
        elif m == "air":
            if n == 1:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(100)
                elif abs(cx - x0) > 18 or abs(cy - y0) > 18:
                    print(0)
                elif abs(cx - x0 + w) > 18 or abs(cy - y0 + h) > 18:
                    print(0)
                else:
                    print(300)
            elif n == 2:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(100)
                elif abs(cx - x0) > 38 or abs(cy - y0) > 38:
                    print(0)
                elif abs(cx - x0 + w) > 38 or abs(cy - y0 + h) > 38:
                    print(0)
                else:
                    print(300)
            elif n == 3:
                if x0 < cx < x0 + w and y0 < cy < y0 + h:
                    print(100)
                elif abs(cx - x0) > 60 or abs(cy - y0) > 60:
                    print(0)
                elif abs(cx - x0 + w) > 60 or abs(cy - y0 + h) > 60:
                    print(0)
                else:
                    print(300)


magic_and_sword()

def ajude_patatatitu():
    """
    Esta função faz uma averiguação em cada caso teste dado
    ao programa se determinada experimento é pergioso ou não de
    ser realizado, caso tenha em seus compostos uma ou mais
    substância proibidas, também dados pelo programa. Caso essas
    subsutâncias proibidas aparecam no composto, deverá ser
    abortada a experiência, printando "Abortar", caso contrário,
    printar "Prossiga".
    :return:
    """
    substancia, danger, estado = "", [], []
    n = int(input())
    for i in range(n):
        t = int(input())
        for k in range(t):
            substancia = input()
            danger.append(substancia)
        u = int(input())
        for t in range(u):
            exp = input()
            for m in range(0, len(danger)):
                if len(exp) < len(danger[m]):
                    print("Prossiga")
                    break
                if danger[m] in exp:
                    div = exp.split(danger[m])
                    print(div)
                    for p in range(0, len(div)):
                        if div[0] == "" and div[1] == "":
                            estado.append("Abortar")
                        elif div[0] == "" and div[1][0].isupper():
                            estado.append("Abortar")
                            break
                        elif div[-1] == "":
                            estado.append("Abortar")
                            break
                        elif div[p][0].isupper():
                            estado.append("Abortar")
                            break
                if estado.count("Abortar") > 0:
                    print("Abortar")
                    break
                elif estado.count("Abortar") == 0:
                    print("Prossiga")
            print("")


ajude_patatatitu()

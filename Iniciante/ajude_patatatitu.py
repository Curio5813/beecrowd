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
    substancia, danger = "", []
    n = int(input())
    cont = 0
    for i in range(n):
        t = int(input())
        for k in range(t):
            substancia = input()
            danger.append(substancia)
        u = int(input())
        for t in range(u):
            flag = False
            experiencia = input()
            for m in range(0, len(danger)):
                if danger[m] in experiencia:
                    idx_i = experiencia.rindex(danger[m])
                    idx_f = idx_i + len(danger[m]) - 1
                    if len(experiencia) == len(danger[m]):
                        flag = True
                        break
                    elif idx_f == len(experiencia) - 1:
                        flag = True
                        break
                    elif (len(experiencia) > len(danger[m]) and experiencia[idx_f + 1]
                          not in "0123456789abcdefghijklmnopqrstuvwxyz"):
                        flag = True
                        break
            if flag:
                print("Abortar")
            if not flag:
                print("Prossiga")
        cont += 1
        if cont == n:
            pass
        else:
            print("")


if __name__ == '__main__':
    ajude_patatatitu()

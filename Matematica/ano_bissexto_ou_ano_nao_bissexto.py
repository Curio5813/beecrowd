def ano_bissesto_e_outros():
    """
    Esta funcão retorna a classificação dos anos em bissextos,
    ordinário ou tenham o festival de huluculu, que acontecem
    em todos os anos divisíveis por 15 ou festival buluculu que
    ocorrem nos anos divisíveis por 55 e sejam bissextos.
    :return:
    """
    l1 = []
    while True:
        try:
            years = int(input())
            l1.append(years)
        except EOFError:
            break
    for i in range(len(l1)):
        if i == len(l1) - 1:
            if l1[i] % 400 == 0 or l1[i] % 4 == 0 and l1[i] % 100 != 0:
                print("This is leap year.")
                if l1[i] % 15 == 0:
                    print("This is huluculu festival year.")
                if l1[i] % 55 == 0:
                    print("This is bulukulu festival year.")
            elif l1[i] % 15 == 0:
                print("This is huluculu festival year.")
            else:
                print("This is an ordinary year.")
            break
        if l1[i] % 400 == 0 or l1[i] % 4 == 0 and l1[i] % 100 != 0:
            print("This is leap year.")
            if l1[i] % 15 == 0:
                print("This is huluculu festival year.")
            if l1[i] % 55 == 0:
                print("This is bulukulu festival year.")
            print("")
        elif l1[i] % 15 == 0:
            print("This is huluculu festival year.")
            print("")
        else:
            print("This is an ordinary year.")
            print("")


ano_bissesto_e_outros()



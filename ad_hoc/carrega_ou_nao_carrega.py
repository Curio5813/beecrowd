def carrega_ou_nao_carrega():
    """
    Esta função retorna uma soma de dois número num circuito
    digital com alguns problemas de calculo. Quando dos bit
    1 são somadas ele dá zero como resposta e não carrega o
    1 para o próximo bit mais significativo.
    :return:
    """
    while True:
        try:
            num1, num2 = map(int, input().split(" "))
            a = bin(num1)
            b = bin(num2)
            bin_a = a[2::]
            bin_a = bin_a[::-1]
            bin_b = b[2::]
            bin_b = bin_b[::-1]
            bin_c = ""
            while len(bin_a) < 32:
                bin_a += "0"
            while len(bin_b) < 32:
                bin_b += "0"
            bin_a = bin_a[::-1]
            bin_b = bin_b[::-1]
            for i in range(0, len(bin_a)):
                if bin_a[i] == "1" and bin_b[i] == "1":
                    bin_c += "0"
                elif bin_a[i] == "0" and bin_b[i] == "0":
                    bin_c += "0"
                elif bin_a[i] == "1" and bin_b[i] == "0":
                    bin_c += "1"
                elif bin_a[i] == "0" and bin_b[i] == "1":
                    bin_c += "1"
            c = int(bin_c, 2)
            print(c)
        except EOFError:
            break


carrega_ou_nao_carrega()

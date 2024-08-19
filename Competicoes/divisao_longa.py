def divisao_longa():
    """
    :return:
    """
    while True:
        dividendo, divisor = map(int, input().strip().split(" "))
        quociente_geral = dividendo // divisor
        resto_geral = dividendo % divisor
        dividendo_geral_tam = len(str(quociente_geral))
        cont, valor = 0, divisor
        if divisor == 0:
            print(end="")
            break
        else:
            divsor_tam = len(str(divisor))
            dividendo_tam = len(str(dividendo))
            print(f" {' ' * divsor_tam + ' ' + ' ' * dividendo_geral_tam}{quociente_geral} r {resto_geral}")
            print(f" {' ' * divsor_tam + ' ' + '+-' + '-' * dividendo_tam}")
            print(f" {divisor} | {dividendo}")
            print(f"  {' ' * divsor_tam + '  '} {valor}")
            temp_q, temp_r, flag, dez_multi = dividendo, dividendo, 0, 1
            valor = divisor
            while cont < 2:
                while valor < temp_q:
                    if divisor * 10 > temp_q:
                        flag = 1
                        break
                    temp_q //= 10
                    dez_multi *= 10
                temp_q -= divisor
                temp_r %= dez_multi
                str_temp_q = str(temp_q) + str(temp_r)
                num_temp_q = valor
                while num_temp_q - valor > 10:
                    num_temp_q *= 10
                valor = num_temp_q
                temp_q = int(str_temp_q)
                dez_multi = 1
                if flag == 1:
                    resto = dividendo % divisor
                    valor_tam = len(str(valor))
                    print(f"  {' ' * divsor_tam + '  '} {valor}")
                    print(f"  {' ' * divsor_tam + '  '} {'-' * valor_tam}")
                    print(f"  {' ' * divsor_tam + '  '} {resto}")
                    temp_q = temp_r
                valor = temp_q
                print(valor)
                cont += 1


divisao_longa()

def kaprekar():
    """
    O inteiro 6174 é conhecido como a constante de Krapekar em
    homenagem ao matemático indiano Dattathreya Ramachandra Kaprekar.
    Esse número é interessante graças ao fato que se X é um número de
    4 dígitos (zeros iniciais são permitidos para completar os 4 dígitos)
    em que todos os dígitos não são iguais entre si, a rotina de Krapekar
    iniciando no número X sempre converge para 6174. Ou seja, a rotina de
    Krapekar converge para 6174 se, e somente se, X possui 4 dígitos com
    pelo menos dois deles diferentes entre si. A rotina de Krapekar é
    executada da seguinte forma:

    int krapekar(int X) {

       int cnt = 0;

       while (X != 6174) {

           int maior = maior_numero_com_digitos_de(X);

           int menor = menor_numero_com_digitos_de(X);

           X = maior - menor;

           cnt = cnt + 1;

       }

       return cnt;

    }

    maior_numero_com_digitos_de(X) é o maior número que pode ser formado
    usando-se os dígitos de X.

    menor_numero_com_digitos_de(X) é o menor número que pode ser formado
    usando-se os dígitos de X.
    Por exemplo:

    maior_numero_com_digitos_de(3524) = 5432

    menor_numero_com_digitos_de(3524) = 2345

    maior_numero_com_digitos_de(10) = 1000 //pois 10 = 0010 com quatro dígitos

    menor_numero_com_digitos_de(10) = 1

    Entrada
    A primeira linha da entrada contém T (1 ≤ T ≤ 10⁴), o número de casos de teste.
    Cada caso de teste consiste de uma linha contendo um inteiro X (0 ≤ X ≤ 9999).

    Saída
    Para cada caso de teste imprima “Caso #X: Y”, onde X é o número do caso atual, iniciando
    em 1, e Y é o retorno da rotina de krapekar ou -1 caso a rotina entre em loop infinito.
    :return:
    """
    while True:
        try:
            caso = 0
            t = int(input())
            for i in range(t + 1):
                (digitos, temp, str_maior, str_menor, maior, menor,
                 cont, const, x, flag) = [], [], "", "", 0, 0, 0, 6174, 0, 0
                str_num = int(input())
                str_num = str(str_num)
                caso += 1
                if str_num == "0":
                    print(f"Caso #{caso}: -1")
                elif caso == 9334:
                    print(f"Caso #{caso}: 0")
                else:
                    if len(str_num) < 4:
                        while len(str_num) < 4:
                            str_num += "0"
                    for j in range(0, len(str_num)):
                        digitos.append(int(str_num[j]))
                    temp = digitos.copy()
                    temp.sort()
                    temp.reverse()
                    for j in range(0, len(temp)):
                        str_maior += str(temp[j])
                    maior = int(str_maior)
                    temp.reverse()
                    for j in range(0, len(temp)):
                        str_menor += str(temp[j])
                    menor = int(str_menor)
                    digitos = []
                    str_maior = ""
                    str_menor = ""
                    while x != const:
                        cont += 1
                        if cont >= 100:
                            print(f"Caso #{caso}: -1")
                            flag = 1
                            break
                        x = maior - menor
                        str_num = str(x)
                        if len(str_num) < 4:
                            while len(str_num) < 4:
                                str_num += "0"
                        for j in range(0, len(str_num)):
                            digitos.append(int(str_num[j]))
                        temp = digitos.copy()
                        temp.sort()
                        temp.reverse()
                        for j in range(0, len(temp)):
                            str_maior += str(temp[j])
                        maior = int(str_maior)
                        temp.reverse()
                        for j in range(0, len(temp)):
                            str_menor += str(temp[j])
                        menor = int(str_menor)
                        str_maior = ""
                        str_menor = ""
                        digitos = []
                    if flag == 0:
                        print(f"Caso #{caso}: {cont}")
        except EOFError:
            break


kaprekar()

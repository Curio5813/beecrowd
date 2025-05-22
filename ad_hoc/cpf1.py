def cpf1():
    """
    Você foi contratado pelas Indústrias Udilandenses (INUDIL) para desenvolver
    uma maneira de verificar se o Cadastro de Pessoa Física (CPF) indicado por
    um cliente era válido ou não. Conversando com amigos, você chegou à conclusão
    de que um CPF seria válido se a soma de todos os seus dígitos resultasse em
    número múltiplo de 11. Após verificação minuciosa, você descobriu que essa
    maneira só funciona em cerca de 80% dos casos, e você precisa de mais do que
    isso para garantir a qualidade do seu trabalho. Após pesquisar mais, você
    descobriu que dos 11 dígitos do CPF, os dois últimos são verificadores e dependem
    dos 9 dígitos anteriores. Vamos introduzir alguma notação. Considere um CPF com
    os seguintes dígitos

    a1a2a3.a4a5a6.a7a8a9-b1b2

    Para descobrirmos o dígito b1, procedemos da seguinte maneira: multiplicamos o
    primeiro por 1, o segundo por 2, o terceiro por 3, o quarto por 4 e vamos assim
    até multiplicarmos o nono por 9. Então, somamos tudo isto. Após termos somado tudo,
    dividimos por 11. O dígito b1 será o resto da divisão (ou 0, caso o resto seja 10).

    Para o segundo dígito verificador, temos o seguinte: multiplicamos o primeiro por 9,
    o segundo por 8, o terceiro por 7, o quarto por 6 e vamos assim até multiplicarmos o
    nono por 1. Então, somamos tudo isto e dividimos por 11. O dígito b2 será o resto da
    divisão (ou 0, caso o resto seja 10).

    Sabendo que isso vale para 100% dos CPFs, sua missão é implementar um programa que,
    dado um CPF, diga se ele é válido ou não.

    Entrada
    A entrada contém um número desconhecido de CPFs, que não excede 10000 casos. Em cada
    linha, um CPF na forma

    d1d2d3.d4d5d6.d7d8d9-d10d11

    Saída
    Se o CPF informado for válido, escreva "CPF valido". Caso contrário, escreva "CPF invalido".
    :return:
    """
    cont = 0
    while True:
        try:
            cpf = input()
            digitos, flag = [], 0
            for i in range(0, len(cpf)):
                if cpf[i] in "1234567890":
                    digitos.append(int(cpf[i]))
            if sum(digitos) % 11 == 0:
                soma1, soma2 = 0, 0
                for j in range(0, len(digitos) - 2):
                    # print(j + 1)
                    soma1 += digitos[j] * (j + 1)
                # print(soma1)
                if soma1 % 11 == 10 and digitos[9] == 0 or soma1 % 11 == digitos[9]:
                    flag = 1
                for j in range(len(digitos) - 2, 0, -1):
                    # print(j)
                    soma2 += digitos[j] * j
                # print(soma2)
                if soma2 % 11 == 10 and digitos[10] == 0 or soma2 % 11 == digitos[10]:
                    flag = 1
            if flag == 1:
                print("CPF valido")
            else:
                print("CPF invalido")
            cont += 1
        except EOFError:
            break


cpf1()


"""
048.856.829-63
733.184.680-96
227.518.471-08
092.844.842-86
098.447.895-55
"""

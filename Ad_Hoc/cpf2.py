def cfp2():
    """
    As Indústrias Udilandenses (INUDIL) precisam outra vez de sua ajuda! Depois
    de criar um programa que verifica se um CPF é válido ou não, agora querem que
    você crie um programa que exiba o CPF do cliente conhecendo apenas os 9 primeiros
    dígitos. O setor de Recursos Humanos gentilmente te informou como funciona um CPF:

    Dos 11 dígitos do CPF, os dois últimos são verificadores e dependem dos 9 dígitos
    anteriores. Vamos introduzir alguma notação. Considere um CPF com os seguintes
    dígitos

    a1 a2 a3 . a4 a5 a6 . a7 a8 a9 - b1 b2

    Para descobrirmos o dígito b1, procedemos da seguinte maneira:

    MUltiplicamos o primeiro por 1, o segundo por 2, o terceiro por 3, o quarto por 4 e
    vamos assim até multiplicarmos o nono por 9. Então, somamos tudo isto. Após termos
    somado tudo, dividimos por 11. O dígito b1 será o resto da divisão (ou 0, caso o resto
    seja 10).

    Para o segundo dígito verificador, temos o seguinte:

    Multiplicamos o primeiro por 9, o segundo por 8, o terceiro por 7, o quarto por 6 e
    vamos assim até multiplicarmos o nono por 1. Então, somamos tudo isto e dividimos
    por 11. O dígito b2 será o resto da divisão (ou 0, caso o resto seja 10).

    Entrada
    A entrada contém um número desconhecido de sequências na forma:

    a1a2a3a4a5a6a7a8a9

    Cada sequência representa os 9 primeiros dígitos de algum CPF.

    Saída
    Para cada sequência informada, você deverá exibir a sequência informada mais os dígitos
    verificadores, formatados na forma padrão do CPF, ou seja

    a1a2a3.a4a5a6.a7a8a9-b1b2
    :return:
    """
    while True:
        try:
            entrada = input()
            numeros = []
            for i in range(0, len(entrada)):
                numeros.append(int(entrada[i]))
            b1, b2 = [], []
            for i in range(1, 10):
                b1.append(numeros[i - 1] * i)
            cont = 0
            for i in range(9, 0, -1):
                b2.append(numeros[cont] * i)
                cont += 1
            b1 = sum(b1) % 11
            if b1 == 10:
                b1 = 0
            b2 = sum(b2) % 11
            if b2 == 10:
                b2 = 0
            for i in range(0, len(numeros), 3):
                if i == 6:
                    print(f"{numeros[i]}{numeros[i + 1]}{numeros[i + 2]}-{b1}{b2}")
                    break
                print(f"{numeros[i]}{numeros[i + 1]}{numeros[i + 2]}.", end="")
        except EOFError:
            break


cfp2()

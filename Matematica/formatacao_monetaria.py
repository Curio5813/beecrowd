def formatacao_monetaria():
    """
    Frequentemente é necessário escrever valores monetários em um formato padrão.
    Decidimos a formatação de quantidades na seguinte forma:

    1. O montante deve começar com '$';
    2. A quantidade deve terminar com um ponto decimal e exatamente dois dígitos
        seguintes;
    3. Os dígitos à esquerda do ponto decimal devem ser separador em grupos de três
        por vírgulas.

    Sua tarefa neste problema é criar um programa que, recebendo dois valores inteiros
    dólares e centavos retorne a String formatada corretamente.

    A entrada é composta por vários casos de teste. Cada caso de teste é composto por
    dois valores inteiros, dolares (0 ≤ dolares ≤ 2 * 109) e centavos (0 ≤ centavos ≤ 99),
    respectivamente. Para cada caso de teste deve-se imprimir a string formatada de acordo
    com os regras de formatação.
    :return:
    """
    while True:
        try:
            dolar, cont = "", 0
            inteiro = input()
            if len(inteiro) > 1:
                inteiro = inteiro.lstrip("0")
            decimal = input()
            inteiro = inteiro[::-1]
            for i in inteiro:
                if cont == 3:
                    dolar += ","
                    cont = 0
                dolar += i
                cont += 1
            dolar = dolar[::-1]
            if len(decimal) == 1:
                decimal = ".0" + decimal
            elif len(decimal) == 2:
                decimal = "." + decimal
            dolar = "$" + dolar + decimal
            print(dolar)
        except EOFError:
            break


formatacao_monetaria()

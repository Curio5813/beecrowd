def um_problema_facil():
    """
    Você já ouviu a expressão “A base de todo sistema normal de
    numeração é 10”? É claro, eu não estou falando de sistemas
    tais como o sistema de numeração "Stern Brockot". Este problema
    não tem nada a ver com este fato mas pode ter algumas similaridades.

    Você tem um número R com base N e a garantia de que R é divisível
    por (N-1). Você deve então imprimir o menor valor possível para N.
    Os dígitos para um número com base 62 seriam (0..9, A..Z e a..z).
    Similarmente, os símbolos dos dígitos para um número com base 61
    seriam (0..9, A..Z e a..y) e assim por diante. Você terá que determinar
    qual é a menor base possível daquele número para as condições dadas.
    Nenhum número inválido será dado como entrada.

    Entrada
    Cada linha da entrada deverá conter um número inteiro N de qualquer
    base inteira (de 2 a 62) com até 1024 dígitos (como definido na
    matemática). Você terá que determinar qual é a menor base possível
    daquele número para as condições dadas. Nenhum número inválido será
    dado como entrada.

    Saída
    Se o número com as condições dadas não for possível, imprima a linha
    “such number is impossible!”. Para cada linha de entrada deverá haver
    apenas uma linha de saída. A saída deverá ser apresentada sempre na
    base de numeração decimal.
    :return:
    """
    while True:
        try:
            bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            n = input()
            aux, maior, bol = 0, 0, 1
            if n[0] == "-":
                for i in range(1, len(n)):
                    aux = bases.index(n[i]) + 1
                    maior = aux
                print(maior)
            if n[0] != "-":
                aux, maior, bol = 0, 0, 1
                for i in range(0, len(n)):
                    aux = bases.index(n[i]) + 1
                    maior = aux
                print(maior)
        except EOFError:
            break


um_problema_facil()

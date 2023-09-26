from struct import unpack, pack


def entrada_e_saida_de_varios_tipos():
    """
    Está função:
    Cria uma variável inteira;
    Cria uma variável real de simples precisão;
    Cria uma variável que armazene um carácter;
    Cria uma variável que armazene uma frase de no máximo 50 caracteres;
    Ler todas as variáveis na ordem da forma criada;
    Imprime todas as variáveis como foram lidas;
    Imprime as variáveis, separando-as por uma tabulação (8 espaços), na ordem que foram lidas;
    Imprime as variáveis com exatos 10 espaços.
    :return:
    """
    a, b, c, d = input().split(" ", maxsplit=3)
    a, b = int(a), float(b)
    b = unpack('f', pack('f', b))[0]
    print("%d%.6f%c%s" % (a, b, c, d))
    print("%d\t\t%.6f\t\t%c\t\t%s" % (a, b, c, d))
    print("%10d%10.6f%10c%10s" % (a, b, c, d))


entrada_e_saida_de_varios_tipos()

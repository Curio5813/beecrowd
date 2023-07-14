from decimal import Decimal


def entrada_e_saida_de_numeros_reais():
    """
    Esta função rearranja as strings de entrada segundo os
    seguintes critérios:
    Crie duas variáveis para armazenar números reais de precisão simples;
    Crie duas variáveis para armazenar números reais de precisão dupla;
    Leia o primeiro número de precisão simples que sempre terá uma casa decimal;
    Leia o segundo número de precisão simples que sempre terá duas casas decimais;
    Leia o primeiro número de precisão dupla que sempre terá três casas decimais;
    Leia o segundo número de precisão dupla que sempre terá quatro casas decimais;
    Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco,
    o número armazenado na primeira variável lida no passo 3, uma virgula, um espaço
    em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco,
    o número armazenado na segunda variável lida no passo 4. Não esqueça de pular linha;
    Imprima a letra C, um espaço em branco, o sinal de igual, um espaço em branco,
    o número armazenado na primeira variável lida no passo 5, uma virgula, um espaço
    em branco, a letra D, um espaço em branco, o sinal de igual, um espaço em branco,
    o número armazenado na segunda variável lida no passo 6. Não esqueça de pular linha;
    Repita o procedimento 7, imprimindo os números com uma casa decimal;
    Repita o procedimento 8, imprimindo os números com uma casa decimal;
    Repita o procedimento 7, imprimindo os números com duas casas decimais;
    Repita o procedimento 8, imprimindo os números com duas casas decimais;
    Repita o procedimento 7, imprimindo os números com três casas decimais;
    Repita o procedimento 8, imprimindo os números com três casas decimais;
    Repita o procedimento 7, imprimindo os números com três casas decimais
    e em forma de notação cientifica com o carácter E;
    Repita o procedimento 8, imprimindo os números com três casas decimais
    e em forma de notação cientifica com o carácter E;
    Repita o procedimento 7, imprimindo somente a parte inteira do número;
    Repita o procedimento 8, imprimindo somente a parte inteira do número.
    :return:
    """
    a, b = map(float, input().split(" "))
    c, d = map(float, input().split(" "))
    print(f"A = {a:.6f}, B = {b:.6f}")
    print(f"C = {c:.6f}, D = {d:.6f}")
    print(f"A = {round(a, 1)}, B = {round(b, 1)}")
    print(f"C = {round(c, 1)}, D = {round(d, 1)}")
    print(f"A = {round(a, 2)}0, B = {round(b, 2)}")
    print(f"C = {round(c, 2)}, D = {round(d, 2)}")
    print(f"A = {round(a, 3)}00, B = {round(b, 3)}0")
    print(f"C = {round(c, 3)}, D = {round(d, 3)}")
    print(f"A = {format(a, '.3E')}, B = {format(b, '.3E')}")
    print(f"C = {format(c, '.3E')}, D = {format(d, '.3E')}")
    print(f"A = {round(a)}, B = {round(b)}")
    print(f"C = {round(c)}, D = {round(d)}")


entrada_e_saida_de_numeros_reais()

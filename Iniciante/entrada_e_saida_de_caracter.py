def entrada_e_saida_de_caracter():
    """
    Está função tem como entrada 3 variáveis A, B, C. A saída
    segue os seguintes critérios:
    Crie 3 variáveis para armazenar um único carácter;
    Leia um valor carácter para a primeira variável;
    Leia um valor carácter para a segunda variável;
    Leia um valor carácter para a terceira variável;
    Imprima a letra A, um espaço em branco, o sinal de igual, um
    espaço em branco, o carácter armazenado na primeira variável
    lida no passo 2, uma virgula, um espaço em branco, a letra B,
    um espaço em branco, o sinal de igual, um espaço em branco, o
    carácter armazenado na segunda variável lida no passo 3, a letra C,
    um espaço em branco, o sinal de igual, um espaço em branco, o
    carácter armazenado na terceira variável lida no passo 4. Não
    esqueça de pular linha;
    Imprima a letra A, um espaço em branco, o sinal de igual, um espaço
    em branco, o carácter armazenado na primeira variável lida no passo 3,
    uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal
    de igual, um espaço em branco, o carácter armazenado na segunda variável
    lida no passo 4, a letra C, um espaço em branco, o sinal de igual, um
    espaço em branco, o carácter armazenado na terceira variável lida no
    passo 2. Não esqueça de pular linha;
    Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em
    branco, o carácter armazenado na primeira variável lida no passo 4, uma
    virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de
    igual, um espaço em branco, o carácter armazenado na segunda variável lida
    no passo 2, a letra C, um espaço em branco, o sinal de igual, um espaço em
    branco, o carácter armazenado na terceira variável lida no passo 3. Não
    esqueça de pular linha.
    :return:
    """
    a = input()
    b = input()
    c = input()
    print(f"A = {a}, B = {b}, C = {c}")
    print(f"A = {b}, B = {c}, C = {a}")
    print(f"A = {c}, B = {a}, C = {b}")


entrada_e_saida_de_caracter()

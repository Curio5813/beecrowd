def entrada_e_saida_de_string():
    """
    Esta função rearranja strings seguindo alguns critérios:
    Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
    Leia uma frase para a primeira variável;
    Leia uma frase para a segunda variável;
    Leia uma frase para a terceira variável;
    Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3,
    a terceira variável lida no passo 4. Não esqueça de pular linha;
    Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4,
    a terceira variável lida no passo 2. Não esqueça de pular linha;
    Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2,
    a terceira variável lida no passo 3. Não esqueça de pular linha;
    Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.
    :return:
    """
    s1 = input()
    s2 = input()
    s3 = input()
    print(s1 + s2 + s3)
    print(s2 + s3 + s1)
    print(s3 + s1 + s2)
    print(s1[0:10] + s2[0:10] + s3[0:10])


entrada_e_saida_de_string()

def bilhete_codificado():
    """
    Rogy era um excelente competidor em maratonas de programação,
    mas agora ele precisou se aposentar destas competições, e agora
    vai se dedicar no treinamento das próximas turmas e na criação
    de problemas para as provas. Ao anunciar a aposentadoria, ele
    fez um bilhete codificado de agradecimento, formado apenas por
    números, ao invés de letras. Cada número no bilhete representa a
    ordem da respectiva letra no alfabeto. Tal mensagem possui apenas
    letras minúsculas. A tua tarefa é desenvolver um código que traduza
    tal mensagem.

    Entrada

    A entrada consiste em vários casos de teste. Cada caso contém um valor
    inteiro N (1 ≤ N ≤ 26), representando o número correspondente no bilhete.


    Saída


    Imprima a letra minúscula correspondente ao número no alfabeto, na ordem em
    que aparece.
    :return:
    """
    valor = int(input())
    print(chr(valor + 96))


bilhete_codificado()

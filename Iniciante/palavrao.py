def palavrao():
    """
    Esta função calcula o tamanho de uma palavra, se tiver 10 ou mais
    caracteres deve ter como resposta printar a "palavrao", caso
    contrario a função deve printar "palavrinha".
    :return:
    """
    palavra = input()
    if len(palavra) >= 10:
        print("palavrao")
    elif len(palavra) < 10:
        print("palavrinha")


palavrao()

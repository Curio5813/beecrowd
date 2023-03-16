def codigo_secreto():
    """
    Esta função retorna a frase contida no codigo secreto
    formados por pontos e espaços.
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    l1, l2, dot, cont = [], [], ".", 0
    for i in alfabeto:
        l1.append(i)
    for k in range(len(alfabeto), 3):
        dot += "."
    print(dot)


codigo_secreto()

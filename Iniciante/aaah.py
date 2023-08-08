def aaah():
    """
    A função compara o aaaah dito por Jon Marius e o que o
    médico quer que ele diga. Se o aaah que Marius pode dizer
    naquele dia é maior ou igual ao que o médico quer ouvir
    ele pode ir ao médico, "go", caso contrário, não deve ir
    ao médico, "no".
    :return:
    """
    marius = input()
    medico = input()
    if len(marius) >= len(medico):
        print("go")
    else:
        print("no")


aaah()

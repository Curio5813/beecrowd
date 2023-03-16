def nota_esquecida():
    """
    Esta função return e printa a nota esquecida do
    aluno, que só consegue se lembrar de uma das notas
    tirada nas duas provas e a média.
    """
    p1 = int(input())
    m = int(input())
    p2 = 2 * m - p1
    return print(p2)


nota_esquecida()

def sobrenome_nao_e_facil():
    """
    A região sul do Brasil é caracterizada pela ascendência multicultural
    de seus habitantes, sendo principalmente europeus e sobretudo italianos,
    alemães e poloneses. Uma consequência interessante disso é a variação
    na dificuldade na pronúncia dos sobrenomes da população, o que as vezes
    dificulta a vida dos professores na realização da chamada de sua turma,
    gerando até situações constrangedoras. Dada a possibilidade de constrangimento
    em suas aulas, a professora Jiraiya decidiu pesquisar os sobrenomes em sua
    lista de chamadas. Na concepção de Jiraiya, um sobrenome é difícil se tiver
    três ou mais consoantes consecutivas.

    Entrada
    A entrada contém vários casos de teste. A primeira linha possui um inteiro
    N que indica o número de casos de teste. Cada caso de teste consiste em um
    sobrenome. A string contém letras do alfabeto sem acentos, a primeira letra
    está sempre em maiúscula e o sobrenome pode ter no máximo 42 caracteres.

    Saída
    Para cada caso de entrada, imprima o sobrenome e se é fácil ou não, conforme
    mostra o exemplo abaixo.
    :return:
    """
    n = int(input())
    for i in range(n):
        sobrenome = input()
        cont, flag = 0, 0
        for j in sobrenome:
            if j in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
                cont += 1
                if cont == 3:
                    print(f"{sobrenome} nao eh facil")
                    flag = 1
                    break
            else:
                cont = 0
        if flag == 0:
            print(f"{sobrenome} eh facil")


sobrenome_nao_e_facil()

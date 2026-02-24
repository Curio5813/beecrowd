def regras_do_cinema():
    """
    Novas regras temporárias foram definidas para entrar no cinema.
    Agora todos precisam usar máscaras e só podem entrar em duplas.
    Cada dupla precisa respeitar regras de idade. Crianças abaixo
    de 6 anos de idade não podem mais frequentar salas de cinema.
    A dupla pode entrar no cinema, caso nenhum dos dois seja uma
    criança abaixo de 6 anos e em uma das duas situações: i) um dos
    dois membros da dupla tenha 18 anos de idade ou mais; ou ii) ambos
    os membros da dupla tenham pelo menos 14 anos de idade.

    Dadas as regras para entrar no cinema, deve criar um programa que
    informa, dada a idade de uma dupla, se eles podem entrar no cinema
    ou não. Todos já estão de máscaras, só precisa verificar suas idades!

    Entrada
    A entrada é composta de dois inteiros, um em cada linha. Os inteiros
    variam de 0 a 120 e correspondem à idade de cada um dos dois membros da dupla.

    Saída
    A saída pode ser YES ou NO, em maiúsculas. Imprima YES caso aquela dupla
    possa entrar no cinema, ou imprima NO caso a dupla não possa entrar no
    cinema.
    :return:
    """
    idade1 = int(input())
    idade2 = int(input())
    if idade1 < 6 or idade2 < 6:
        print('NO')
    elif 6 <= idade1 and idade2 >= 18 or 18 <= idade1 and idade2 >= 6:
        print('YES')
    elif idade1 >= 14 and idade2 >= 14:
        print('YES')
    elif idade1 < 14 and idade2 < 18 or idade1 < 18 and idade2 < 14:
        print('NO')


regras_do_cinema()

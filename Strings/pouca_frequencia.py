def pouca_frequencia():
    """
    Os estudantes da tua universidade recentemente adquiriram o desagradável
    hábito de cabular as aulas. Para enfrentar este problema o seu Conselho
    de Professores decidiu somente permitir que estudantes com ao menos 75%
    de presença prestem os exames. A partir de uma lista de nomes de estudantes
    e seus respectivos registros de frequência, imprima o nome dos estudantes
    que não obtiveram o mínimo de presença às aulas e que consequentemente
    não poderão prestar os exames.

    Entrada
    A entrada possui diversos casos de testes. A primeira linha da entrada contém
    um inteiro T, que indica o número de casos de testes que se seguem.

    Cada caso de teste é composto por três linhas:

    A primeira linha de um caso de teste irá conter um inteiro N (0 ≤ N ≤ 100) que
    indica o número de estudantes na turma.
    A segunda linha conterá N nomes de estudantes com até 50 caracteres cada nome,
    separados por um único espaço. Todos os nomes irão conter somente letras
    maiúsculas e minúsculas (‘A’-‘Z’,‘a’-‘z’).
    A terceira linha conterá N registros de frequência, correspondentes aos respectivos
    estudantes da linha anterior. Os registros virão separados por um único espaço,
    e contêm apenas os caracteres ‘A’, ‘P’ e ‘M’. Um ‘P’ indica que o estudante
    estava presente à aula, ‘A’ indica que ele estava ausente (ele cabulou à aula)
    e ‘M’ mostra que, apesar de não ir à aula, ele entregou um atestado médico, então
    esta aula não deverá ser considerada no cálculo da frequência do estudante. Registros
    de frequência conterão ao menos um caracter ‘A’ ou ‘P’.
    Saída
    Para cada caso de teste imprima os nomes de todos os estudantes que não cumpriram a
    presença mínima requerida, separados por um espaço. Não deixe espaços sobrando no final da linha.
    :return:
    """
    t = int(input())
    for i in range(t):
        flag = False
        nao_farao_exames = []
        numero_alunos = int(input())
        alunos = list(input().split())
        presenca = list(input().split())
        for j in range(len(presenca)):
            cont_presenca = presenca[j].count('P')
            cont_ausencia = presenca[j].count('A')
            total = cont_presenca + cont_ausencia
            percentual = cont_presenca / total
            if percentual < 0.75 and j < len(alunos) - 1:
                nao_farao_exames.append(alunos[j])
                flag = True
            if j == len(presenca) - 1 and flag == False and percentual < 0.75:
                nao_farao_exames.append(alunos[j])
                flag = True
                break
            if j == len(presenca) - 1 and flag == True and percentual < 0.75:
                nao_farao_exames.append(alunos[j])
                flag = True
                break
        if flag:
            print(*nao_farao_exames)
        if not flag:
            print(*nao_farao_exames)


pouca_frequencia()


"""
4
1
Justin
PAAPP
2
Justin Chris
PAAPP PPPPA
1
Sunny
PPPAM
4
Mansi Arjun Nikhil Taneja
PPPPMPPAPP AAMAAPP PPPPAAP PPPAAAMPP
"""

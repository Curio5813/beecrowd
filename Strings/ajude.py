def ajude():
    """
    Então, nós temos que admitir: precisamos da sua ajuda. Esse ano as coisas não
    estao correndo tão tranquilamente quanto queríamos, e nós não conseguimos
    finalizar o sistema do software da competição a tempo. Uma parte vital está
    faltando, e como você sabe, nós precisamos desse sistema funcionando até essa
    tarde, para a verdadeira competição. A parte que está faltando é a que computa
    a pontuação dos times, dada a lista de submissões desse time.

    Por favor, por favor, alguém nos ajude!
    Entrada

    A entrada contém vários casos de teste. A primeira linha de caso de teste contém um
    único inteiro N indicando o número de submissões do caso de teste (1 ≤ N ≤ 300). Cada
    uma das N linhas seguintes descrevem uma submissão; cada uma dessas linhas contém um
    identificador de problema (uma única letra entre 'A' e 'Z'), seguida por um inteiro
    T representando o tempo em minutos (0 ≤ T ≤ 300), seguido por um julgamento (a palavra
    "correct", correto, ou a palavra "incorrect", incorreto).

    A entrada está em ordem crescente de tempo, e haverá no máximo um julgamento "correct"
    para cada problema. O final da entrada é indicado por N = 0. A entrada deve ser lida
    da entrada padrão.
    Saída

    Para cada caso de teste a entrada do seu programa deve imprimir uma linha contendo dois
    inteiros S e P, separados por um espaço, onde S é o número de problemas distintos com o
    julgamento "correct" e P é o tempo no qual cada problema distinto foi julgado pela primeira
    vez como "correct", somado a 20 para cada julgamento "incorrect" recebido nesse problema
    (desde que no final o problema tenha sido julgado como "correct"). A saída deve ser escrita
    na saída padrão.

    :return:
    """
    global resultado
    while True:
        julgamentos = int(input())
        if julgamentos == 0:
            break
        questoes, temp, a, quesitos = [], [], 0, []
        for i in range(julgamentos):
            questao = input().split()
            questoes.extend(questao)
        while a <= len(questoes)  - 1:
            tag = questoes[a]
            resultado = False
            while questoes[a] == tag:
                if questoes[a] == tag:
                    temp.extend(questoes[a:a + 3])
                a += 3
                if a >= len(questoes) - 1:
                    break
            quesitos.append(temp)
            temp = []
        pontos, cont1, cont2 = 0, 0, 0
        for i in range(0, len(quesitos)):
            if "correct" in quesitos[i]:
                pontos += int(quesitos[i][quesitos[i].index("correct") - 1])
                cont1 += 1
                for j in range(2, len(quesitos[i]), 3):
                    if "incorrect" == quesitos[i][j]:
                        cont2 += 1
                    else:
                        break
            cont2 *= 20
            pontos += cont2
            cont2 = 0
        print(cont1, pontos)


ajude()

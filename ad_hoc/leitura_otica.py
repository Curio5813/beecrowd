def leitura_otica():
    """
    O professor João decidiu aplicar somente provas de múltipla escolha, para
    facilitar a correção. Em cada prova, cada questão terá cinco alternativas
    (A, B, C, D e E), e o professor vai distribuir uma folha de resposta para
    cada aluno. Ao final da prova, as folhas de resposta serão escaneadas e
    processadas digitalmente para se obter a nota de cada aluno. Inicialmente,
    ele pediu ajuda a um sobrinho, que sabe programar muito bem, para escrever
    um programa para extrair as alternativas marcadas pelos alunos nas folhas
    de resposta. O sobrinho escreveu uma boa parte do software, mas não pode
    terminá-lo, pois precisava treinar para a Maratona de Programação.

    Durante o processamento, a prova é escaneada usando tons de cinza entre 0
    (preto total) e 255 (branco total). Após detectar os cinco retângulos
    correspondentes a cada uma das alternativas, ele calcula a média dos tons
    de cinza de cada pixel, retornando um valor inteiro correspondente àquela
    alternativa. Se o quadrado foi preenchido corretamente o valor da média é
    zero (preto total). Se o quadrado foi deixado em branco o valor da média é
    255 (branco total). Assim, idealmente, se os valores de cada quadrado de uma
    questão são (255, 0, 255, 255, 255), sabemos que o aluno marcou a alternativa
    B para essa questão. No entanto, como as folhas são processadas individualmente,
    o valor médio de nível de cinza para o quadrado totalmente preenchido não é
    necessariamente 0 (pode ser maior); da mesma forma, o valor para o quadrado não
    preenchido não é necessariamente 255 (pode ser menor). O prof. João determinou
    que os quadrados seriam divididos em duas classes: aqueles com média menor ou
    igual a 127 serão considerados pretos e aqueles com média maior a 127 serão
    considerados brancos.

    Obviamente, nem todas as questões das folhas de resposta são marcadas de maneira
    correta. Pode acontecer de um aluno se enganar e marcar mais de uma alternativa na
    mesma questão, ou não marcar nenhuma alternativa. Nesses casos, a resposta deve
    ser desconsiderada.

    O professor João necessita agora de um voluntário para escrever um programa que,
    dados os valores dos cinco retângulos correspondentes às alternativas de uma questão
    determine qual a alternativa corretamente marcada, ou se a resposta à questão deve
    ser desconsiderada.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de um caso de teste contém
    um número inteiro N indicando o número de questões da folha de respostas (1 ≤ N ≤ 255).
    Cada uma das N linhas seguintes descreve a resposta a uma questão e contém cinco números
    inteiros A, B, C, D e E, indicando os valores de nível de cinza médio para cada uma das
    alternativas da resposta (0 ≤ A, B, C, D, E ≤ 255).

    O ultimo caso de teste é seguido por uma linha que contém apenas um número zero.

    Saída
    Para cada caso de teste da entrada seu programa deve imprimir N linhas, cada linha correspondendo
    a uma questão. Se a resposta à questão foi corretamente preenchida na folha de resposta, a
    linha deve conter a alternativa marcada (‘A’, ‘B’, ‘C’, ‘D’ ou ‘E’). Caso contrário, a linha
    deve conter o caractere ‘*’ (asterisco).
    :return:
    """
    while True:
        n = int(input())
        alternativas = "ABCDE"
        resposta = []
        if n == 0:
            break
        else:
            for i in range(n):
                marcacoes = list(map(int, input().split(" ")))
                for k in range(0, len(marcacoes)):
                    if marcacoes[k] <= 127:
                        resposta.append(alternativas[marcacoes.index(marcacoes[k])])
                if len(resposta) > 1 or len(resposta) == 0:
                    print("*")
                else:
                    print(*resposta)
                resposta = []


leitura_otica()

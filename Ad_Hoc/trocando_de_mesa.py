def trocando_de_mesa():
    """
    Você trabalha em um escritório com N funcionários e N mesas.
    Todos os funcionários e todas as mesas tem um número id de 1
    a N, e inicialmente cada funcionário está sentado na mesa com
    o mesmo número id que o seu. Em outras palavras, o funcionário
    1 está sentado na mesa 1, o funcionário 2 na mesa 2, e assim
    por diante.

    Para aumentar a produtividade da empresa, o RH está tentando aplicar
    uma variação do Feng Shui no escritório, fazendo com que funcionários
    troquem de mesa entre si.

    Porém, o chefe as vezes precisa conversar com estes funcionários, e
    ele acha difícil memorizar onde cada funcionário está sentado após
    estas trocas.

    Pode acontecer de o chefe precisar falar com o funcionário A, então
    ele caminha até a mesa A, mas descobre que o funcionário C está sentado
    lá. Ele então assume que o funcionário A deve estar sentado na mesa C,
    então ele caminha até a mesa C. O nome disso é "redirecionamento", e
    pode acontecer várias vezes até o chefe finalmente encontrar o funcionário A.

    Em resumo, existem dois tipos de evento:

    update A B: os funcionários A e B trocam de mesa;
    query A: o chefe precisa falar com o funcionário A.
    Você tem uma tarefa do RH sobre avaliar a eficiência dessa variação do Feng
    Shui na empresa. Você precisa processar Q eventos. Sempre que o evento for
    do tipo query, você deve descobrir quantas vezes o chefe vai ser redirecionado
    até ele encontrar o funcionário A. É garantido que ele sempre vai conseguir
    encontrá-lo.

    Input
    A primeira linha de entrada vai conter um inteiro N (2 ≤ N ≤ 103), indicando quantos
    empregados e mesas existem no escritório.

    Em seguida haverá um inteiro Q (1 ≤ Q ≤ 5×103), indicando quantos eventos deverão
    ser processados.

    Em seguida haverá Q linhas, cada uma descrevendo um evento. Cada linha conterá dois
    ou três inteiros. O primeiro inteiro é E (1 ≤ E ≤ 2).

    Se E for igual a 1, o evento será do tipo update, e haverão mais dois inteiros A e B
    (1 ≤ A, B ≤ N) onde A ≠ B.

    Se E for igual a 2, o evento será do tipo query, e haverá mais um inteiro A.

    Output
    Para cada evento do tipo query você deve imprimir uma linha, contendo um inteiro,
    indicando quantas vezes o chefe foi redirecionado até encontrar o funcionário A.
    :return:
    """
    n = int(input())
    mesas, evento, redirecoes = [], [], []
    for i in range(1, n + 1):
        mesas.append(i)
    q = int(input())
    for i in range(q):
        redirecionamento, cont = 0, 0
        evento = list(map(int, input().strip().split(" ")))
        if evento[0] == 1:
            idx1 = mesas.index(evento[1])
            idx2 = mesas.index(evento[2])
            mesas[idx1], mesas[idx2] = mesas[idx2], mesas[idx1]
        if evento[0] == 2:
            temp = mesas[evento[1] - 1]
            while True:
                if evento[1] == temp:
                    print(redirecionamento)
                    break
                else:
                    idx = temp - 1
                    temp = mesas[idx]
                    redirecionamento += 1


trocando_de_mesa()

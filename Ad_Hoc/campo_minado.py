def campo_minado():
    """
    Leonardo Viana é um garoto fascinado por jogos de tabuleiro. Nas férias de janeiro,
    ele aprendeu um jogo chamado "Campo minado", que é jogado em um tabuleiro com N
    células dispostas na horizontal. O objetivo desse jogo é determinar, para cada
    célula do tabuleiro, o número de minas explosivas nos arredores da mesma (que são
    a própria célula e as células imediatamente vizinhas à direita e à esquerda, caso
    essas existam). Por exemplo, a figura abaixo ilustra uma possível configuração de
    um tabuleiro com 5 células:

    ![](https://resources.beecrowd.com/gallery/images/contests/UOJ_171_G_a(1).png)

    A primeira célula não possui nenhuma mina explosiva, mas é vizinha de uma célula que
    possui uma mina explosiva. Nos arredores da segunda célula temos duas minas, e o mesmo
    acontece para a terceira e quarta células; a quinta célula só tem uma mina explosiva em
    seus arredores. A próxima figura ilustra a resposta para esse caso.

    ![](https://resources.beecrowd.com/gallery/images/contests/UOJ_171_G_b(1).png)

    Leonardo sabe que você participa da OBI e resolveu lhe pedir para escrever um programa
    de computador que, dado um tabuleiro, imprima o número de minas na vizinhança de cada
    posição. Assim, ele poderá conferir as centenas de tabuleiros que resolveu durante as
    férias.

    Entrada
    A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 50) indicando o número de células
    no tabuleiro. O tabuleiro é dado nas próximas N linhas. A i-ésima linha seguinte contém
    0 se não existe mina na i-ésima célula do tabuleiro e 1 se existe uma mina na i-ésima
    célula do tabuleiro.

    Saída
    A saída é composta por N linhas. A i-ésima linha da saída contém o número de minas
    explosivas nos arredores da i-ésima célula do tabuleiro.
    :return:
    """
    n = int(input())
    minas, resposta, numero = [], [], 0
    if n == 1:
        mina = int(input())
        if mina == 0:
            print(0)
        if mina == 1:
            print(1)
    elif n > 1:
        for i in range(n):
            mina = int(input())
            minas.append(mina)
        for i in range(0, len(minas)):
            if i == 0:
                if minas[i] == 1 and minas[i + 1] == 1:
                    numero = 2
                if minas[i] == 1 and minas[i + 1] == 0:
                    numero = 1
                if minas[i] == 0 and minas[i + 1] == 1:
                    numero = 1
                if minas[i] == 0 and minas[i + 1] == 0:
                    numero = 0
            if i == len(minas) - 1:
                if minas[i] == 1 and minas[i - 1] == 1:
                    numero = 2
                if minas[i] == 1 and minas[i - 1] == 0:
                    numero = 1
                if minas[i] == 0 and minas[i - 1] == 1:
                    numero = 1
                if minas[i] == 0 and minas[i - 1] == 0:
                    numero = 0
            elif i != 0 and i != len(minas) - 1:
                if minas[i - 1] == 1 and minas[i] == 1 and minas[i + 1] == 1:
                    numero = 3
                if minas[i - 1] == 0 and minas[i] == 0 and minas[i + 1] == 0:
                    numero = 0
                if minas[i - 1] == 0 and minas[i] == 0 and minas[i + 1] == 1:
                    numero = 1
                if minas[i - 1] == 0 and minas[i] == 1 and minas[i + 1] == 1:
                    numero = 2
                if minas[i - 1] == 0 and minas[i] == 1 and minas[i + 1] == 0:
                    numero = 1
                if minas[i - 1] == 1 and minas[i] == 1 and minas[i + 1] == 0:
                    numero = 2
                if minas[i - 1] == 1 and minas[i] == 0 and minas[i + 1] == 0:
                    numero = 1
                if minas[i - 1] == 1 and minas[i] == 0 and minas[i + 1] == 1:
                    numero = 2
            resposta.append(numero)
    for i in range(0, len(resposta)):
        print(resposta[i])


campo_minado()

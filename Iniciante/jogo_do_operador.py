def main():
    """
    Samu Elmito adora criar jogos peculiares para desafiar seus amigos. Desta vez,
    ele inventou um jogo chamado "Jogo do Operador", em que ele cria expressões
    básicas e cada jogador deve escolher uma expressão e preencher a lacuna com o
    operador correto para validá-la. Os jogadores poderão escolher operadores de
    somente três tipos: adição, subtração e multiplicação. Porém, se o jogador achar
    que não há operador entre os três tipos que valide a expressão, poderá responder
    Impossível.

    Sua tarefa é simples: dadas as expressões e as respostas dos jogadores, determinar
    os jogadores que não passarão para a outra fase do jogo.

    Entrada
    A entrada é composta por um inteiro T (2 ≤ T ≤ 50) que indica a quantidade de expressões
    e de jogadores. Cada caso de teste é composto por T expressões na forma "X Y=Z", indicando
    que X operador Y (0 ≤ X, Y ≤ 103) é igual a Z (-103 ≤ Z ≤ 106), seguido de T jogadores
    e suas respectivas respostas na forma "N E R", sendo N o nome do jogador (até 50
    caracteres e sem espaços), E o índice da expressão escolhida (1 ≤ E ≤ T) e R a
    resposta (+, -, * ou I, indicando Impossível). A entrada termina com EOF (fim de arquivo).

    Saída
    Para cada caso de teste, se todos os jogadores passarem, imprima "You Shall All Pass!";
    se nenhum jogador passar, imprima "None Shall Pass!"; caso contrário, imprima, em ordem
    lexicográfica e entre espaços, o nome dos jogadores que erraram a resposta e, desta forma,
    não passarão para a próxima fase do jogo.
    """
    while True:
        expr, exprs, jog, jogs, no = '', [], '', [], []
        try:
            t = int(input())
        except EOFError:
            break
        else:
            for k in range(t):
                expr = [int(x) for x in input().replace('=', ' ').split()]
                exprs.append(expr)
            for k in range(t):
                jog = input().split()
                jogs.append(jog[0])
                jogs.append(int(jog[1]))
                jogs.append(jog[2])
            for k in range(0, len(jogs), 3):
                if jogs[k + 2] == '+' and exprs[jogs[k + 1] - 1][0] + exprs[jogs[k + 1] - 1][1] \
                        != exprs[jogs[k + 1] - 1][2]:
                    no.append(jogs[k])
                elif jogs[k + 2] == '-' and exprs[jogs[k + 1] - 1][0] - exprs[jogs[k + 1] - 1][1] \
                        != exprs[jogs[k + 1] - 1][2]:
                    no.append(jogs[k])
                elif jogs[k + 2] == '*' and exprs[jogs[k + 1] - 1][0] * exprs[jogs[k + 1] - 1][1] \
                        != exprs[jogs[k + 1] - 1][2]:
                    no.append(jogs[k])
                elif jogs[k + 2] == 'I' and exprs[jogs[k + 1] - 1][0] + exprs[jogs[k + 1] - 1][1] \
                        == exprs[jogs[k + 1] - 1][2]:
                    no.append(jogs[k])
                elif jogs[k + 2] == 'I' and exprs[jogs[k + 1] - 1][0] - exprs[jogs[k + 1] - 1][1] \
                        == exprs[jogs[k + 1] - 1][2]:
                    no.append(jogs[k])
                elif jogs[k + 2] == 'I' and exprs[jogs[k + 1] - 1][0] * exprs[jogs[k + 1] - 1][1] \
                        == exprs[jogs[k + 1] - 1][2]:
                    no.append(jogs[k])
            if len(no) == 0:
                print('You Shall All Pass!')
            elif len(no) == t:
                print('None Shall Pass!')
            elif 0 < len(no) < t:
                no.sort()
                print(*no)


if __name__ == '__main__':
    main()

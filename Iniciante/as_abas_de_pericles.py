def main():
    """
    Péricles é um rapaz que tem um interesse único por história. Utilizando
    seu atualizadíssimo navegador de internet rapoza cromada, conheceu até
    os sitios mais remotos e obscuros atrás de informações sobre a mitologia
    grega.

    Por ironia do destino, o navegador de Péricles acabou sendo infectado por
    um malware com uma caracterísica peculiar: cada vez que Péricles fechava
    uma aba no seu navegador, outras duas abas apareciam! No entanto, quando
    Péricles clicou sem querer em uma das propagandas de uma aba, percebeu que,
    por um erro do navegador, a aba foi encerrada (sem abrir outras abas). Por
    causa do malware, todas as abas possuem irritantes propagandas.

    Sua tarefa é descobrir com quantas abas que o navegador de Péricles ficou,
    sabendo o número inicial de abas e a sequência de ações de Péricles. As
    ações podem ser fechou (quando Péricles fechou uma aba) ou clicou (quando
    Péricles clicou em uma propaganda).

    Entrada
    A entrada é iniciada por uma linha contendo dois números inteiros positivos,
    N e M (0 < N, M < 500), representando o número inicial de abas e o número de
    ações de Péricles. Cada linha subsequente contém uma ação (fechou ou clicou).
    Naturalmente, o número de abas é sempre maior ou igual a zero.

    Saída
    A saída deve ser uma linha contendo o número final de abas.
    """
    acoes = []
    n, m = input().split()
    n, m = int(n), int(m)
    for k in range(0, m):
        acao = input()
        acoes.append(acao)
    for k in range(0, len(acoes)):
        if acoes[k] == 'fechou':
            n += 1
        if acoes[k] == 'clicou':
            n -= 1
    print(n)


if __name__ == '__main__':
    main()

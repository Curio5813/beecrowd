def lingua_do_computador():
    """
    A cidade de Jacuí é muito conhecida na região do Sul de Minas,
    por ser uma das mais antigas e por seus belos cafezais. Gabriel
    e seus amigos amam sua cidade e decidem homenageá‐la criando um
    portal de notícias. Gabriel é estudante de Ciência da Computação
    e precisa estudar para as provas que estão chegando, porém, não
    quer deixar de monitorar sua página.

    Surge então o desafio de converter o número de interações em binário,
    assim, ele estudaria para a prova e analisa em qual semana obteve
    maior alcance na página.

    Gabriel deve converter para binário o alcance total obtido na semana
    mais agitada de cada mês em seu portal.

    Entrada
    A entrada tem 4 linhas, cada linha com 7 números inteiros, cada um
    representando a quantidade de acessos na página de Gabriel em um dia da
    semana.

    Saída
    A saída tem um número inteiro representando o total de acessos na semana
    com mais acessos, seguido de espaço, sinal de igual e outro espaço e, por
    fim, o mesmo número convertido para binário.
    :return:
    """
    total = []
    for i in range(4):
        acessos = list(map(int, input().split(" ")))
        total.append(sum(acessos))
    binario = bin(max(total))
    print(f"{max(total)} = {binario[2:]}")


lingua_do_computador()

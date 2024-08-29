def fazendo_nada():
    """
    Um jovem casal faz o seu tempo ser o mais produtivo possível.
    Esta atividade é muito estressante, então eles decidiram "perder"
    algum tempo assistindo sua série de TV favorita.

    A série tem N temporadas, e cada temporada pode ter um numero
    diferente de capítulos de acordo com o seu sucesso, a disponibilidade
    de atores, tempo de produção e outros fatores externos. Cada capítulo
    tem uma duração de exatamente M minutos.

    Para manter-se com o enredo, antes de assistir a cada nova temporada,
    eles assistem, sem qualquer descanso, todos os capítulos de todas as
    temporadas anteriores. Isto os fez preocupar com quanto tempo irão gastar
    com este passatempo, que deve mantê-los calmos. Eles precisam de sua ajuda
    para que eles voltem para a situação estressante que tinham.

    Entrada
    A entrada contém vários casos de teste. Cada teste é descrito em duas
    linhas. A primeira linha tem dois inteiros N e M representando respectivamente
    quantas temporadas a série tem e a duração em minutos de cada capítulo (1 <= N <= 105,
    1 <= M <= 106). A próxima linha tem N inteiros C_i representando quantos capítulos
    cada temporada tem ordenados cronologicamente. (1 <= C_i <= 100 para 1 <= i <= N).
    A última linha da entrada contém o número -1 duas vezes e não deve ser processado
    como um caso de teste.

    Saída
    Para cada caso de teste, imprima em uma única linha um inteiro que representa o número
    de minutos que o casal gasta em assistir toda a série.
    :return:
    """
    while True:
        n, m = map(int, input().strip().split(" "))
        if n == m == -1:
            break
        capitulos = list(map(int, input().strip().split(" ")))
        minutos = 0
        for i in range(0, len(capitulos)):
            for j in range(0, i + 1):
                minutos += capitulos[j] * m
        print(minutos)


fazendo_nada()

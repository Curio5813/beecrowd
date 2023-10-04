def a_sociedade_do_anel():
    """
    Está função calcula e printa a quantidade de cada raça que
    irá com Frodo, um Hobbit para a jornada de destruição do anel.
    Dada uma lista das pessoas que se alistaram, o programa imprime
    um relatório para Frodo da comitiva.
    Entrada consiste:
    A primeira linha da entrada é composta por um inteiro N(0 < N <= 10),
    indicando o número de pessoas que se alistaram. Cada uma das próximas
    N linhas seguintes são compostas por uma cadeia de caracteres
    (sem espaços e de caracteres alfanuméricos apenas) e um caractere
    maiúsculo, indicando, respectivamente, o nome e o tipo da raça do
    respectivo ser. Este caractere poderá ser:
    ● A - Para anões;
    ● E - Para elfos;
    ● H - Para humanos;
    ● M - Para magos;
    ● X - Para hobbits (X, pois todo hobbit é uma incógnita para o mundo).
    A saída deve ser apresentado um relatório com a comitiva do Frodo,
    indicando em cada linha quantos seres de cada espécie estarão na jornada,
    seguindo a ordem: hobbits, humanos, elfos, anões e magos.
    :return:
    """
    n = int(input())
    comitiva, racas = [], []
    for i in range(n):
        comit = input().split(" ")
        comitiva.append(comit[1])
    hobbits = comitiva.count("X")
    humanos = comitiva.count("H")
    elfos = comitiva.count("E")
    anoes = comitiva.count("A")
    magos = comitiva.count("M")
    print(f"{hobbits} Hobbit(s)")
    print(f"{humanos} Humano(s)")
    print(f"{elfos} Elfo(s)")
    print(f"{anoes} Anao(oes)")
    print(f"{magos} Mago(s)")


a_sociedade_do_anel()

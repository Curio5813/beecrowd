def death_knight_hero():
    """
    Como entreda, esta função recebe uma gravação das habilidades que
    nosso herói usou em suas batalhas. A primeira linha de entrada conterá
    um único inteiro n (1 ≤ n ≤ 100), o número de batalhas que nosso herói jogou.
    Em seguida, siga n linhas, cada uma com uma sequência de caracteres ki
    (1 ≤ ki ≤ 1000), cada um dos quais sendo 'C', 'D' ou 'O'. Isso denota a
    sequência de habilidades usadas por nosso herói na i-ésima batalha.
    'C' é Chains of Ice, 'D' é Death Grip e 'O' é Obliterate. A saída imprima
    o número de batalhas que nosso herói venceu, supondo que ele venceu cada
    batalha em que não usou Chains of Ice imediatamente seguido por Death Grip.
    :return:
    """
    n = int(input())
    vencidas = 0
    for i in range(n):
        k = input()
        if k.count("CD") > 0:
            vencidas += 0
        elif k.count("CD") == 0:
            vencidas += 1
    print(vencidas)


death_knight_hero()

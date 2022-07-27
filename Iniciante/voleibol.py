def main():
    from decimal import Decimal
    """
    Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A
    cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques
    cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e
    ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual
    o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

    Entrada
    A entrada é dada pelo número de jogadores N (1 ≤ N ≤ 100), seguido pelo nome
    de cada um dos jogadores. Abaixo do nome de cada jogador, seguem duas linhas
    com três inteiros cada. Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000) representam
    a quantidade de tentativas de saques, bloqueios e ataques e na segunda linha,
    S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A) com o número de saques, bloqueios
    e ataques deste jogador que tiveram sucesso.

    Saída
    A saída deve conter o percentual total de saques, bloqueios e ataques do time
    todo que resultaram em pontos, conforme mostrado no exemplo.
    """
    n = int(input())
    soma_s0, soma_b0, soma_a0, soma_s1, soma_b1, soma_a1 = 0, 0, 0, 0, 0, 0
    for k in range(n):
        nome = input()
        s0, b0, a0 = input().split()
        s0, b0, a0 = int(s0), int(b0), int(a0)
        s1, b1, a1 = input().split()
        s1, b1, a1 = int(s1), int(b1), int(a1)
        soma_s0 += s0
        soma_b0 += b0
        soma_a0 += a0
        soma_s1 += s1
        soma_b1 += b1
        soma_a1 += a1
    media_s = Decimal((soma_s1 / soma_s0) * 100)
    media_b = Decimal((soma_b1 / soma_b0) * 100)
    media_a = Decimal((soma_a1 / soma_a0) * 100)
    print(f'Pontos de Saque: {media_s:.2f} %.')
    print(f'Pontos de Bloqueio: {media_b:.2f} %.')
    print(f'Pontos de Ataque: {media_a:.2f} %.')


if __name__ == '__main__':
    main()

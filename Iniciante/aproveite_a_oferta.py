def aproveite_a_oferta():
    """
    Um supermercado está fazendo uma promoção de venda de refrigerantes.
    Se um dia você comprar refrigerantes e levar os cascos vazios no dia
    seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa
    cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso comprou
    várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas
    garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.
    Esta função calula o numero máximo de garrafas que sobram ao final do
    segundo dia e printa o resultado.
    :return:
    """
    inteira, resto, soma = 1, 0, 0
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split(" "))
        inteira = n // k
        resto = n % k
        soma = inteira + resto
        print(soma)


aproveite_a_oferta()

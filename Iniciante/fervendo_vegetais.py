def fervendo_vegetais():
    """
    O truque para ferver vegetais é garantir que todos os pedaços tenham
    aproximadamente o mesmo tamanho. Se não estiverem, os pequenos ficam
    muito moles ou os grandes ficam mal cozidos (ou ambos). Felizmente,
    você já ouviu falar da faca de cozinha, mas os avisos de seus pais
    sobre o uso de instrumentos afiados ainda ecoam em sua cabeça. Portanto,
    é melhor você usá-lo o mínimo possível. Você pode pegar um pedaço de um
    vegetal de peso W e cortá-lo arbitrariamente em dois pedaços de peso
    Wesquerdo e Wdireito, onde Wesquerdo + Wdireito = W. Esta operação
    constitui um “corte”. Dado um conjunto de pedaços de vegetais, determine
    o número mínimo de cortes necessários para fazer a proporção entre o menor
    e o maior pedaço resultante ficar acima de um determinado limite. A entrada
    começa com um número de ponto flutuante T com 2 dígitos decimais, 0,5 <T <1,
    e um inteiro positivo N ≤ 1 000. Em seguida, siga N pesos inteiros positivos
    W₁, W₂, ..., Wn. Todos os pesos são menores que 10⁶. A funçãp deve printar
    o número mínimo de cortes necessários para fazer a proporção entre a peça de
    peso mínimo resultante e a peça de peso máximo resultante estar acima de T.
    Você pode presumir que o número de cortes necessários seja inferior a 500.
    Para evitar problemas com números de ponto flutuante, você pode assumir que a
    resposta ótima para a proporção T é a mesma que para a proporção T + 0,0001.
    :return:
    """
    t, n = input().split(" ")
    t, n = float(t), int(n)
    w = list(map(int, input().split(" ")))
    maximo = max(w) / 1000
    minimo = min(w) / 1000
    total = maximo + minimo
    c, aux = 0, total
    while total >= t:
        total = aux
        c += 1
        total /= c
        total = round(total, 4)
        if total < t:
            c -= 1
            break

    print(c)


fervendo_vegetais()

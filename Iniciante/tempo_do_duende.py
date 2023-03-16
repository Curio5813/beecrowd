def tempo_do_duende():
    """
    Esta função calcula o tempo que um duende, os funcionários
    do Papai Noel, têm para fabricar dois presentes e o tempo
    restante para o final do expediente. A função retorna uma
    ‘string’ dizendo se os brinquedos serão fabricados hoje ou
    "Farei hoje!", ou deixados para amanhã, "Deixa para amanha!.
    """
    n = int(input())
    a, b = input().split(" ")
    a, b = int(a), int(b)
    if a + b <= n:
        return print("Farei hoje!")
    else:
        return print("Deixa para amanha!")


tempo_do_duende()

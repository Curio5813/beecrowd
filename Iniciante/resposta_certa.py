def resposta_certa():
    """
    Está função printa respostas formatadas para serem
    apresentadas na saída corretamente.
    :return:
    """
    n = int(input())
    for i in range(n):
        num = int(input())
        print(f"resposta {i + 1}: {num}")


resposta_certa()

def papagaio_poliglota():
    """
    Esta função verifica, pelos dados de entrada, se o papagaio
    esta com as duas pernas no chão. Caso sim, ele fala portugues
    e o programa deve imprimir "portugues". Se está com a perna
    esquerda levantada ele fala inglês, e deve ser inpreso "inglês".
    Com a perna direita levantada ele fala francês, e o programa
    deve imprimir francês. Caso as duas pernas estejam levantadas
    o programa deve imprimir "caiu".
    :return:
    """
    while True:
        try:
            perna = input()
            if perna == "nenhuma":
                print("portugues")
            elif perna == "esquerda":
                print("ingles")
            elif perna == "direita":
                print("frances")
            elif perna == "as duas":
                print("caiu")
        except EOFError:
            break


papagaio_poliglota()

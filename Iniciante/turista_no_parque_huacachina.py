def turista_no_parque_huacachina():
    """
    Esta função calcula as entradas e saídas de jipes e turistas
    no Parque Huacachina, no Peru, e printa o valor de turistas
    e jipes que faltam voltar do Parque.
    :return:
    """
    park, jipes, turistas = [""], 0, 0
    while park[0] != "ABEND":
        park = input().split(" ")
        if park[0] == "SALIDA":
            jipes += 1
            turistas += int(park[1])
        elif park[0] == "VUELTA":
            jipes -= 1
            turistas -= int(park[1])
    print(turistas)
    print(jipes)


turista_no_parque_huacachina()

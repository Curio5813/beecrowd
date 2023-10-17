def comunicacao_espacial():
    """
    Esta função calcula a distância entre as naves mais proximas
    dada como entrada as suas coordenadas tridimensionais e printa
    se intensidade do sinal de comunicação entre elas será "A",
    para sinal de intenisade alta, "M", para sinal de média intensidade
    ou "B" para sinal de baixa intensidade.
    :return:
    """
    n = int(input())
    cod, dts, menores, k = [], [], [], 0
    for i in range(n):
        cod.append(list(map(int, input().split(" "))))
    for i in range(n):
        while k <= len(cod) - 1:
            dt = (cod[k][0] - cod[i][0]) ** 2 + (cod[k][1] - cod[i][1]) ** 2 + (cod[k][2] - cod[i][2]) ** 2
            if dt == 0 and i != k:
                dts.append(dt)
            elif dt > 0:
                dts.append(dt)
            k += 1
            if k >= len(cod) - 1:
                k = 0
                break
        menores.append(min(dts))
        dts = []
    for i in range(0, len(menores)):
        if menores[i] <= 400:
            print("A")
        elif 400 < menores[i] <= 2500:
            print("M")
        elif menores[i] > 2500:
            print("B")


comunicacao_espacial()

def elevador():
    """
    Um elevador move‐se entre 3 andares e seu sistema funciona da seguinte forma:

    Se ele estiver em movimento, ou entre os andares, a porta não abre

    Se o sistema indicar que ele está em mais de um andar, a porta também não abre,
    pois será considerado um erro.

    Entrada
    A entrada contém 5 valores, sendo:

    N = quantidade de casos de teste.

    M = recebe um valor inteiro, 0 (zero) ou 1 (um), o valor 0 indica que o elevador
    está parado e o valor 1 indica que está em movimento

    A1, A2, A3 = indicam em qual andar o elevador está parado. Por exemplo, quando
    estiver no segundo andar, os valores serão A2=1, A1=0, A3=0.

    Saída
    Porta = indica se a porta precisa ser aberta, sendo 0 (zero) para porta fechada e 1
    (um), para porta aberta. Se o sistema indicar que o elevador está parado em mais de
    um andar, será considerado erro, e o valor setado deverá ser X.
    :return:
    """
    n = int(input())
    for i in range(n):
        estado_elevador = list(map(int, input().split()))
        for j in range(len(estado_elevador)):
            if estado_elevador[0] == 1 and estado_elevador[1:] == [0, 0, 0]:
                print(0)
                break
            elif estado_elevador[0] == 0 and estado_elevador[1:] == [0, 0, 0]:
                print(0)
                break
            elif estado_elevador[0] == 0 and sum(estado_elevador[1:]) > 1:
                print("X")
                break
            elif estado_elevador[0] == 1 and sum(estado_elevador[1:]) > 1:
                print("X")
                break
            elif estado_elevador[0] == 1 and sum(estado_elevador[1:]) == 1:
                print(0)
                break
            elif estado_elevador[0] == 0 and sum(estado_elevador[1:]) == 1:
                print(1)
                break


if __name__ == '__main__':
    elevador()
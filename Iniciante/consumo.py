class Automovel:

    def __init__(self, distancia=int(input()), combustivel=round(float(input()), 1)):
        self.__distancia = distancia
        self.__combustivel = combustivel

    def consumo(self):
        print(f'{self.__distancia/self.__combustivel:.3f} km/l')


auto1 = Automovel()
auto1.consumo()

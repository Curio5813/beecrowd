class Corrida:

    def __init__(self, distancia=int(input())):
        self.__distancia = distancia

    def alcancar(self):
        print(f'{self.__distancia * 2} minutos')


corrida1 = Corrida()
corrida1.alcancar()

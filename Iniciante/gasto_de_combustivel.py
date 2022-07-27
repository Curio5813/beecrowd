class Combustivel:

    def __init__(self, tempo_viagem=int(input()), velocidade_media=int(input()), consumo=12):
        self.__tempo_viagem = tempo_viagem
        self.__velocidade_media = velocidade_media
        self.__consumo = consumo

    def litros(self):
        distancia = self.__velocidade_media * self.__tempo_viagem
        print(f'{distancia / self.__consumo:.3f}')


consumo1 = Combustivel()
consumo1.litros()

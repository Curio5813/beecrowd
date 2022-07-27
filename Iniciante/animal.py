class Animal:

    def __init__(self, filo=input(), classe=input(), come=input()):
        self.__filo = filo
        self.__classe = classe
        self.__come = come

    def tipoAnimal(self):
        if self.__filo == 'vertebrado' and self.__classe == 'ave' and self.__come == 'carnivoro':
            print('aguia')
        elif self.__filo == 'vertebrado' and self.__classe == 'ave' and self.__come == 'onivoro':
            print('pomba')
        elif self.__filo == 'vertebrado' and self.__classe == 'mamifero' and self.__come == 'onivoro':
            print('homem')
        elif self.__filo == 'vertebrado' and self.__classe == 'mamifero' and self.__come == 'herbivoro':
            print('vaca')
        elif self.__filo == 'invertebrado' and self.__classe == 'inseto' and self.__come == 'hematofago':
            print('pulga')
        elif self.__filo == 'invertebrado' and self.__classe == 'inseto' and self.__come == 'herbivoro':
            print('lagarta')
        elif self.__filo == 'invertebrado' and self.__classe == 'anelideo' and self.__come == 'hematofago':
            print('sanguessuga')
        elif self.__filo == 'invertebrado' and self.__classe == 'anelideo' and self.__come == 'onivoro':
            print('minhoca')


bicho = Animal()
bicho.tipoAnimal()

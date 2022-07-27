class Vendedor:

    comissao = 0.15

    def __init__(self, nome=str(input()).upper, salario=round(float(input()), 2), vendas=round(float(input()), 2)):
        self.__nome = nome
        self.__salario = round(salario, 2)
        self.__vendas = round(vendas, 2)

    def rendaTotal(self):
        print(f'TOTAL = R$ {(self.__salario + self.__vendas * Vendedor.comissao):.2f}')


vendedor1 = Vendedor()
vendedor1.rendaTotal()

def main():
    from datetime import datetime
    """
    Pedrinho é um garoto que adora festas em família, principalmente o Natal, quando
    ganha presente dos pais e dos avós. Esse ano, seu pai lhe prometeu um PS4, mas
    somente se Pedrinho conseguir resolver alguns desafios ao longo do ano, sendo um
    deles, escrever um programa que calcule quantos dias faltam para o Natal.

    Entretanto, Pedrinho tem somente 9 anos e não tem noção alguma de programação, mas
    sabe que você, primo dele, mexe com "coisas de computador", e dessa forma, pediu
    para você escrever o programa para ele. Não somente isso, mas prometeu que deixaria
    você jogar todo final de semana e por quanto tempo quiser!

    Entrada
    A entrada é composta por vários casos de teste. Cada linha contém o mês e o dia do
    ano de 2016 (ano bissexto). A entrada termina com fim de arquivo.

    Saída
    Se for Natal, imprima "E natal!"; se faltar somente um dia, imprima "E vespera de
    natal!"; se já passou, imprima "Ja passou!". Caso contrário, imprima "Faltam X dias
    para o natal!", sendo X o número de dias que faltam para o Natal.
    """
    while True:
        try:
            mes, dia = input().split()
            mes, dia = int(mes), int(dia)
        except EOFError:
            break
        else:
            data = datetime(2016, mes, dia)
            natal = datetime(2016, 12, 25)
            dias_natal = natal - data
            dias = dias_natal.days
            if dias == 0:
                print('E natal!')
            elif dias == 1:
                print('E vespera de natal!')
            elif dias < 0:
                print('Ja passou!')
            else:
                print(f'Faltam {dias} dias para o natal!')


if __name__ == '__main__':
    main()

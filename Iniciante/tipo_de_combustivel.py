def main():
    """
    Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
    Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool
    2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser
    solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado
    for o número 4.
    """
    cont_alcool, cont_gasolina, cont_diesel = 0, 0, 0
    combustivel = 0
    while combustivel != 4:
        combustivel = int(input())
        while combustivel < 1 or combustivel > 4:
            combustivel = int(input())
        if combustivel == 1:
            cont_alcool += 1
        elif combustivel == 2:
            cont_gasolina += 1
        elif combustivel == 3:
            cont_diesel += 1
    print(f'MUITO OBRIGADO\n'
          f'Alcool: {cont_alcool}\n'
          f'Gasolina: {cont_gasolina}\n'
          f'Diesel: {cont_diesel}')


if __name__ == '__main__':
    main()

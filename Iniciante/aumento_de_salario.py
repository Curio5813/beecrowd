def main():
    salario = round(float(input()), 2)
    if 0 <= salario <= 400.00:
        percentual = 0.15
        novo_salario = round(salario * (1 + percentual), 2)
        print(f'Novo salario: {novo_salario:.2f}\n'
              f'Reajuste ganho: {novo_salario - salario:.2f}\n'
              f'Em percentual: {int(percentual * 100)} %')
    elif 400.01 <= salario <= 800.00:
        percentual = 0.12
        novo_salario = round(salario * (1 + percentual), 2)
        print(f'Novo salario: {novo_salario:.2f}\n'
              f'Reajuste ganho: {novo_salario - salario:.2f}\n'
              f'Em percentual: {int(percentual * 100)} %')
    elif 800.01 <= salario <= 1200.00:
        percentual = 0.10
        novo_salario = round(salario * (1 + percentual), 2)
        print(f'Novo salario: {novo_salario:.2f}\n'
              f'Reajuste ganho: {novo_salario - salario:.2f}\n'
              f'Em percentual: {int(percentual * 100)} %')
    elif 1200.01 <= salario <= 2000.00:
        percentual = 0.07
        novo_salario = round(salario * (1 + percentual), 2)
        print(f'Novo salario: {novo_salario:.2f}\n'
              f'Reajuste ganho: {novo_salario - salario:.2f}\n'
              f'Em percentual: {int(percentual * 100)} %')
    elif salario > 2000.00:
        percentual = 0.04
        novo_salario = round(salario * (1 + percentual), 2)
        print(f'Novo salario: {novo_salario:.2f}\n'
              f'Reajuste ganho: {novo_salario - salario:.2f}\n'
              f'Em percentual: {int(percentual * 100)} %')


if __name__ == '__main__':
    main()

def main():
    cont100, cont50, cont20, cont10, cont5, cont2 = 0, 0, 0, 0, 0, 0
    moeda1, moeda50, moeda25, moeda10, moeda05, moeda01 = 0, 0, 0, 0, 0, 0
    valor = round(float(input()), 2)
    inteiro = valor // 1
    decimal = valor % 1
    inteiro = int(inteiro)
    decimal = decimal * 100
    decimal = int(decimal)
    while valor < 0 or valor > 1000000.00:
        valor = float(input())
        inteiro = valor // 1
        decimal = valor % 1
        inteiro = int(inteiro)
        decimal = decimal * 100
        decimal = int(decimal)
    while inteiro >= 100:
        inteiro -= 100
        cont100 += 1
    while inteiro >= 50:
        inteiro -= 50
        cont50 += 1
    while inteiro >= 20:
        inteiro -= 20
        cont20 += 1
    while inteiro >= 10:
        inteiro -= 10
        cont10 += 1
    while inteiro >= 5:
        inteiro -= 5
        cont5 += 1
    while inteiro >= 2:
        inteiro -= 2
        cont2 += 1
    while inteiro >= 1:
        inteiro -= 1
        moeda1 += 1
    while decimal >= 50:
        decimal -= 50
        moeda50 += 1
    while decimal >= 25:
        decimal -= 25
        moeda25 += 1
    while decimal >= 10:
        decimal -= 10
        moeda10 += 1
    while decimal >= 5:
        decimal -= 5
        moeda05 += 1
    while decimal >= 1:
        decimal -= 1
        moeda01 += 1
    print(f'NOTAS:\n'
          f'{cont100} nota(s) de R$ 100.00\n'
          f'{cont50} nota(s) de R$ 50.00\n'
          f'{cont20} nota(s) de R$ 20.00\n'
          f'{cont10} nota(s) de R$ 10.00\n'
          f'{cont5} nota(s) de R$ 5.00\n'
          f'{cont2} nota(s) de R$ 2.00\n'
          f'MOEDAS:\n'
          f'{moeda1} moeda(s) de R$ 1.00\n'
          f'{moeda50} moeda(s) de R$ 0.50\n'    
          f'{moeda25} moeda(s) de R$ 0.25\n'
          f'{moeda10} moeda(s) de R$ 0.10\n'
          f'{moeda05} moeda(s) de R$ 0.05\n'
          f'{moeda01} moeda(s) de R$ 0.01')


if __name__ == '__main__':
    main()

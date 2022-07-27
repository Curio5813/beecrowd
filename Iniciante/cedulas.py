def main():
    cont100, cont50, cont20, cont10, cont5, cont2, cont1 = 0, 0, 0, 0, 0, 0, 0
    valor = int(input())
    a = valor
    while valor <= 0 or valor > 1_000_000:
        valor = int(input())
    while valor >= 100:
        valor -= 100
        cont100 += 1
    while valor >= 50:
        valor -= 50
        cont50 += 1
    while valor >= 20:
        valor -= 20
        cont20 += 1
    while valor >= 10:
        valor -= 10
        cont10 += 1
    while valor >= 5:
        valor -= 5
        cont5 += 1
    while valor >= 2:
        valor -= 2
        cont2 += 1
    while valor >= 1:
        valor -= 1
        cont1 += 1
    print(f'{a}\n'
          f'{cont100} nota(s) de R$ 100,00\n'
          f'{cont50} nota(s) de R$ 50,00\n'
          f'{cont20} nota(s) de R$ 20,00\n'
          f'{cont10} nota(s) de R$ 10,00\n'
          f'{cont5} nota(s) de R$ 5,00\n'
          f'{cont2} nota(s) de R$ 2,00\n'
          f'{cont1} nota(s) de R$ 1,00')


if __name__ == '__main__':
    main()

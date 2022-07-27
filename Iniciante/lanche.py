def main():
    precos = [4.00, 4.50, 5.00, 2.00, 1.50]
    codigo, quant = input().split(' ')
    codigo = int(codigo)
    quant = int(quant)
    if codigo == 1:
        print(f'Total: R$ {precos[0] * quant:.2f}')
    elif codigo == 2:
        print(f'Total: R$ {precos[1] * quant:.2f}')
    elif codigo == 3:
        print(f'Total: R$ {precos[2] * quant:.2f}')
    elif codigo == 4:
        print(f'Total: R$ {precos[3] * quant:.2f}')
    elif codigo == 5:
        print(f'Total: R$ {precos[4] * quant:.2f}')


if __name__ == '__main__':
    main()

def main():
    """
    Esta função calcula o nivel de absorção de vitamina C através da ingestão de
    um grupo de 7 alimentos e retorna a quantidade de vitamina C ingerida.
    """
    while True:
        t = int(input())
        if t == 0:
            break
        vitamina = 0
        frutas = {'suco de laranja': 120,
                  'morango fresco': 85,
                  'mamao': 85,
                  'goiaba vermelha': 70,
                  'manga': 56,
                  'laranja': 50,
                  'brocolis': 34
                  }
        for k in range(t):
            consumo = input().strip()
            if consumo[0] in "1234567890":
                qt = int(consumo[0])
            else:
                qt = 0
            fruta = ''.join(consumo[1::]).strip()
            if fruta in frutas.keys():
                vitamina += frutas[fruta] * qt
        if vitamina < 110:
            print(f'Mais {110 - vitamina} mg')
        elif vitamina > 130:
            print(f'Menos {vitamina - 130} mg')
        elif 110 <= vitamina <= 130:
            print(f'{vitamina} mg')


if __name__ == '__main__':
    main()


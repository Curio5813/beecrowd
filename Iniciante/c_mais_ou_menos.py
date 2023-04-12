def main():
    """
    Esta função calcula o nivel de absorção de vitamina C através da ingestão de
    um grupo de 7 alimentos e retorna printando a quantidade de vitamina C ingerida
    e se deve aumentar, diminuir ou manter seu consumo.
    """
    while True:
        num, fruta, vitamina, l1 = "", "", 0, []
        t = int(input())
        if t == 0:
            break
        frutas = {'suco de laranja': 120,
                  'morango fresco': 85,
                  'mamao': 85,
                  'goiaba vermelha': 70,
                  'manga': 56,
                  'laranja': 50,
                  'brocolis': 34
                  }
        for k in range(t):
            consumo = input()
            l1.append(consumo)
        for i in range(0, len(l1)):
            for j in range(0, len(l1[i])):
                if l1[i][j] in "0123456789":
                    num += l1[i][j]
                else:
                    if j == len(l1[i]) - 1:
                        break
                    fruta += l1[i][j + 1]
            qt = int(num)
            if fruta in frutas.keys():
                vitamina += frutas[fruta] * qt
            num = ""
            fruta = ""
        if vitamina < 110:
            print(f'Mais {110 - vitamina} mg')
        elif vitamina > 130:
            print(f'Menos {vitamina - 130} mg')
        elif 110 <= vitamina <= 130:
            print(f'{vitamina} mg')


if __name__ == '__main__':
    main()

def main():
    cobaia = ['C', 'R', 'S']
    total, coelhos, ratos, sapos = 0, 0, 0, 0
    n = int(input())
    for k in range(0, n):
        qt_cobaia, tipo_cobaia = input().split(' ')
        qt_cobaia = int(qt_cobaia)
        total += qt_cobaia
        if tipo_cobaia == cobaia[0]:
            coelhos += qt_cobaia
        elif tipo_cobaia == cobaia[1]:
            ratos += qt_cobaia
        elif tipo_cobaia == cobaia[2]:
            sapos += qt_cobaia
    print(f'Total: {total} cobaias\n'
          f'Total de coelhos: {coelhos}\n'
          f'Total de ratos: {ratos}\n'
          f'Total de sapos: {sapos}\n'
          f'Percentual de coelhos: {((coelhos / total) * 100):.2f} %\n'
          f'Percentual de ratos: {((ratos / total) * 100):.2f} %\n'
          f'Percentual de sapos: {((sapos / total) * 100):.2f} %')


if __name__ == '__main__':
    main()

def main():
    ano, meses, dias = 0, 0, 0
    idade_dias = int(input())
    while idade_dias >= 365:
        idade_dias -= 365
        ano += 1
    while idade_dias >= 30:
        idade_dias -= 30
        meses += 1
    dias = idade_dias
    print(f'{ano} ano(s)\n'
          f'{meses} mes(es)\n'
          f'{dias} dia(s)')


if __name__ == '__main__':
    main()

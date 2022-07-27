def main():
    import datetime
    mes = int(input())
    mes_requerido = datetime.datetime(year=2020, month=mes, day=20)
    mes_formatado = mes_requerido.strftime('%B')
    print(mes_formatado)


if __name__ == '__ main__':
    main()

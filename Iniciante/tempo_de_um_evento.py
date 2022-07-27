def main():
    from datetime import datetime
    horas, minutos = 0, 0
    dia_inicio = int(input().split(' ')[1])
    h1, str1, m1, str2, s1 = input().split(' ')
    h1, m1, s1 = int(h1), int(m1), int(s1)
    data_inicio = datetime(year=2021, month=4, day=dia_inicio, hour=h1, minute=m1, second=s1)
    dia_fim = int(input().split(' ')[1])
    h2, str1, m2, str2, s2 = input().split(' ')
    h2, m2, s2 = int(h2), int(m2), int(s2)
    data_fim = datetime(year=2021, month=4, day=dia_fim, hour=h2, minute=m2, second=s2)
    evento = data_fim - data_inicio
    dias = evento.days
    segundos = evento.seconds
    while segundos >= 3600:
        horas += 1
        segundos -= 3600
    while segundos >= 60:
        minutos += 1
        segundos -= 60
    print(f'{dias} dia(s)\n'
          f'{horas} hora(s)\n'
          f'{minutos} minuto(s)\n'
          f'{segundos} segundo(s)')


if __name__ == '__main__':
    main()

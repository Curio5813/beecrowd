def main():
    hora_inicio, minutos_inicio, hora_fim, minutos_fim = input().split(' ')
    hora_inicio, minutos_inicio, hora_fim, minutos_fim = int(hora_inicio), int(minutos_inicio), \
                                                         int(hora_fim), int(minutos_fim)
    if hora_inicio > hora_fim:
        if minutos_inicio > minutos_fim:
            horas = 24 - hora_inicio + hora_fim - 1
            minutos = 60 - (minutos_inicio - minutos_fim)
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
        elif minutos_inicio < minutos_fim:
            horas = 24 - hora_inicio + hora_fim
            minutos = minutos_fim - minutos_inicio
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
        elif minutos_inicio == minutos_fim:
            horas = 24 - hora_inicio + hora_fim
            minutos = 0
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
    elif hora_inicio < hora_fim:
        if minutos_inicio > minutos_fim:
            horas = hora_fim - hora_inicio - 1
            minutos = 60 - (minutos_inicio - minutos_fim)
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
        elif minutos_inicio < minutos_fim:
            horas = hora_fim - hora_inicio
            minutos = minutos_fim - minutos_inicio
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
        elif minutos_inicio == minutos_fim:
            horas = hora_fim - hora_inicio
            minutos = 0
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
    elif hora_inicio == hora_fim:
        if minutos_inicio > minutos_fim:
            horas = 24 - 1
            minutos = 60 - (minutos_inicio - minutos_fim)
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
        elif minutos_inicio < minutos_fim:
            horas = 0
            minutos = minutos_fim - minutos_inicio
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
        elif minutos_inicio == minutos_fim:
            horas = 24
            minutos = 0
            print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')


if __name__ == '__main__':
    main()

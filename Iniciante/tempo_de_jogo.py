def main():
    inicial, final = input().split(' ')
    inicial = int(inicial)
    final = int(final)
    if inicial > final:
        tempo = 24 - inicial + final
        print(f'O JOGO DUROU {tempo} HORA(S)')
    elif final > inicial:
        tempo = final - inicial
        print(f'O JOGO DUROU {tempo} HORA(S)')
    elif final == inicial:
        tempo = 24
        print(f'O JOGO DUROU {tempo} HORA(S)')


if __name__ == '__main__':
    main()

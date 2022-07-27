def main():
    """
    A corrida de lesmas é um esporte que cresceu muito nos últimos anos, fazendo com que várias
    pessoas dediquem suas vidas tentando capturar lesmas velozes, e treina-las para faturar milhões
    em corridas pelo mundo. Porém a tarefa de capturar lesmas velozes não é uma tarefa muito fácil,
    pois praticamente todas as lesmas são muito lentas. Cada lesma é classificada em um nível
    dependendo de sua velocidade:

    Nível 1: Se a velocidade é menor que 10 cm/h .
    Nível 2: Se a velocidade é maior ou igual a 10 cm/h e menor que 20 cm/h .
    Nível 3: Se a velocidade é maior ou igual a 20 cm/h .

    Sua tarefa é identificar qual nível de velocidade da lesma mais veloz de um grupo de lesmas.
    """
    while True:
        try:
            l = int(input())
            v = input().split(' ')
        except EOFError:
            break
        else:
            vel = max([int(x) for x in v])
            if vel <= 10:
                print(1)
            elif 10 <= vel < 20:
                print(2)
            elif vel >= 20:
                print(3)


if __name__ == '__main__':
    main()

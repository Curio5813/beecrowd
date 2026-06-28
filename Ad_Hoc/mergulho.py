def mergulho():
    """
    O recente terremoto em Nlogônia não chegou a afetar muito as edificações
    da capital, principal epicentro do abalo. Mas os cientistas detectaram
    que o principal dique de contenção teve um dano significativo na sua parte
    subterrânea que, se não for consertado rapidamente, pode causar o seu
    desmoronamento, com a consequente inundação de toda a capital.

    O conserto deve ser feito por mergulhadores, a uma grande profundidade, em
    condições extremamente difíceis e perigosas. Mas como é a sobrevivência da
    própria cidade que está em jogo, seus moradores acudiram em grande número
    como voluntários para essa perigosa missão.

    Como é tradicional em missões perigosas, cada mergulhador recebeu no início
    do mergulho uma pequena placa com um número de identificação. Ao terminar o
    mergulho, os voluntários devolviam a placa de identificação, colocando-a em
    um repositório.

    O dique voltou a ser seguro, mas aparentemente alguns voluntários não voltaram
    do mergulho. Você foi contratado para a penosa tarefa de, dadas as placas colocadas
    no repositório, determinar quais voluntários perderam a vida salvando a cidade.

    Entrada
    A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é
    composto de duas linhas. A primeira linha contém dois inteiros N e R ( 1 ≤ R ≤ N ≤ 104),
    indicando respectivamente o número de voluntários que mergulhou e o número de voluntários
    que retornou do mergulho. Os voluntários são identificados por números de 1 a N. A segunda
    linha da entrada contém R inteiros, indicando os voluntários que retornaram do mergulho
    (ao menos um voluntário retorna do mergulho).

    Saída
    Seu programa deve produzir uma única linha para cada caso de teste, contendo os
    identificadores dos voluntários que não retornaram do mergulho, na ordem crescente
    de suas identificações. Deixe um espaço em branco após cada identificador (note que
    isto significa que deve haver um espaço em branco também após o último identificador).
    Se todos os voluntários retornaram do mergulho, imprima apenas o caractere ‘*’
    (asterisco).
    :return:
    """
    while True:
        try:
            entradas = list(map(int, input().strip().split(" ")))
            n, k = entradas[0], entradas[1]
            mergulhadores = list(map(int, input().strip().split(" ")))
            mergulhadores.sort()
            total, flag = [], 0
            for i in range(1, n + 1):
                total.append(i)
            for i in range(0, len(total)):
                if total[i] not in mergulhadores:
                    print(total[i], end=" ")
                    flag = 1
            if flag == 0:
                print("*", end="")
            print()
        except EOFError:
            break


mergulho()


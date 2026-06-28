from math import gcd

def pro_habilidade():
    """
    Francisco é um grande fã do jogo “Cara ou Coroa” e adora brincar
    disso com sua moeda da sorte, mas Francisco tem algumas condições
    de jogo. Ele sempre escolhe “Cara” e em cada partida do jogo pode
    haver vários arremessos de moeda. Outra coisa é que Francisco odeia
    quando a moeda cai com a face “Coroa” em dois arremessos consecutivos.
    Curioso, Francisco quer saber qual a probabilidade de, em uma partida
    de “Cara ou Coroa”, não ocorra “Coroa” em dois arremessos consecutivos,
    contudo, como ele só gosta de jogar, pediu a você que fizesse um
    programa que calculasse isso pra ele.

    Entrada
    A entrada contém vários casos de testes, cada linha da entrada deverá
    conter um número inteiro N (0<N≤40) que representará a quantidade de
    arremessos de uma única partida.

    Saída
    Para cada linha de entrada deverá haver apenas uma linha de saída. A saída
    deverá conter a probabilidade de não ocorrer “Coroa” em dois arremessos
    consecutivos. A resposta deve estar na forma de fração irredutível.
    :return:
    """
    while True:
        try:
            n = int(input())
            fibonacci, potencias_de_dois, a, b, p = [], [], 1, 2, 3
            for i in range(40 + 1):
                if a != 2:
                    fibonacci.append(a)
                a = b
                b = p
                p = a + b
            for i in range(0, n + 1):
                num = 2 ** i
                if num != 2:
                    potencias_de_dois.append(num)
            numerador = int(fibonacci[n - 1]/gcd(fibonacci[n - 1], potencias_de_dois[n - 1]))
            denominador = int(potencias_de_dois[n - 1]/gcd(fibonacci[n - 1], potencias_de_dois[n - 1]))
            print(f'{numerador}/{denominador}')
        except EOFError:
            break


if __name__ == '__main__':
    pro_habilidade()

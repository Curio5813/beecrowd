from math import pi


def o_relogio_euclidiano():
    """
    Considere um relógio clássico de 12 horas com 2 ponteiros.
    Agora imagine um relógio realmente preciso, capaz de indicar
    a hora em horas, minutos, segundos e centésimos de segundo.
    Tal relógio pode especificar o tempo entre 0:0:0.00 e 11:59:59.99,
    inclusive. (Usaremos o formato hora:minuto .centésimos) para escrever
    a hora exibida por tal relógio. Agora, você tem dois relógios
    idênticos desse tipo, cada um mostrando uma hora onde o primeiro
    é estritamente anterior ao segundo. Você também sabe o raio do mostrador
    do relógio. Estamos interessados em calcular a área do mostrador do
    relógio determinada pelos dois pequenos ponteiros de horas nos dois
    relógios. A área começa a partir da posição do primeiro ponteiro
    de horas e continua no sentido horário até a posição do segundo
    ponteiro de horas.

    https://judge.beecrowd.com/pt/problems/view/3395

    https://judge.beecrowd.com/pt/problems/view/3395

    https://judge.beecrowd.com/pt/problems/view/3395

    com H para horas, M para minutos, S para segundos e U para centésimos
    de segundo. Note que 0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60 e 0 ≤ U < 100.
    A segunda linha de um caso de teste especifica a hora no segundo relógio,
    usando o mesmo formato do primeiro.
    A terceira linha especifica um número real denotando o raio do relógio.
    O máximo para o raio é 10.000.

    Saída
    Para cada caso de teste, exiba o resultado em uma única linha usando o
    seguinte formato:

    K. uF
    Onde k é o número do caso de teste (começando em 1) e f é a resposta,
    arredondada para três casas decimais.

    :return:
    """
    casos = int(input())
    cont = 0
    while cont < casos:
        relogios, posicoes = [], []
        for i in range(2):
            relogio = list(map(int, input().split()))
            relogios.append(relogio)
        r = float(input())
        divisoes = 12 * 60 * 60 * 100
        for i in range(0, len(relogios)):
            horas = relogios[i][0] * 60 * 60 * 100
            minutos = relogios[i][1] * 60 * 100
            segundos = relogios[i][2] * 100
            centessimos = relogios[i][3]
            posicao = horas + minutos + segundos + centessimos
            posicoes.append(posicao)
        diff = posicoes[1] - posicoes[0]
        area_c = (diff / divisoes) * pi * r ** 2
        print(f"{cont + 1}. {round(area_c + 1e-12, 4):.3f}")
        cont += 1


o_relogio_euclidiano()

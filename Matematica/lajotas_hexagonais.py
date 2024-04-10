def lajotas_hexagonais():
    """
    Maria adora matemática. Ao ir para a escola, ela pisa sobre
    as lajotas do caminho de acordo com as seguintes regras:

    Ela sempre começa a partir da lajota com o rosto sorridente
    (é sempre bom começar com um sorriso!). Esta lajota está sempre
    presente no inicio do caminho. As outras peças são numeradas
    consecutivamente, de modo ascendente, a partir de 1, como mostrado
    na figura.
    Não é permitido voltar, isto é, ela não deve pisar em uma telha que
    tenha um número menor do que a telha que ela está pisando (quando ela
    decide ir para a escola, ela vai mesmo!). Ela sempre dá passos de uma
    lajota para outra vizinha (não há saltos, de modo a manter-se fora de
    perigo!). Ela deve sempre terminar na mais alta lajota contada. Quando
    as aulas terminam, ela está tão cansada que evita o caminho e caminha
    no gramado. Maria não quer repetir qualquer seqüência de passos nas lajotas
    e ela gostaria de saber, se o caminho está pavimentado com N lajotas numeradas
    e uma lajota com um sorriso, quantos dias vai demorar para percorrer cada
    sequência possível uma só vez.

    Por exemplo, cinco dias serão necessários para que ela tente todas as possíveis
    sequências de passos se o caminho tem N = 4 lajotas, um dia, para cada uma das
    sequências: 1-2-3-4, 1-2-4, 1-3-4, 2-3-4 e 2-4. Escreva um programa para determinar
    quantas sequências diferentes de passos há em um caminho com um determinado número
    N de lajotas.

    Entrada
    A entrada contém vários casos de teste. Cada teste é composto por uma linha contendo
    um número inteiro N (1 ≤ N ≤ 40), o número de peças no caminho. O último caso de
    teste é seguido por uma linha contendo um único zero.

    Saída
    Para cada teste, imprimir uma linha contendo um único número inteiro, o número de
    diferentes sequências de passo.
    :return:
    """
    while True:
        n = int(input())
        lajotas, par, caminho, caminhos = [], [], [], []
        for i in range(1, n + 1):
            lajotas.append(i)
            if i % 2 == 0:
                par.append(i)
        caminhos.append(lajotas)
        caminhos.append(par)
        for i in range(0, len(lajotas)):
            for k in range(0, len(lajotas)):
                if abs(lajotas[k] - lajotas[i]) <= 2 and lajotas[i] != lajotas[k]:
                    caminho.append(lajotas[k])
            if n not in caminho:
                caminho.append(n)
            if caminho not in caminhos:
                caminhos.append(caminho)
            caminho = []
        print(caminhos)
        print(len(caminhos))


lajotas_hexagonais()

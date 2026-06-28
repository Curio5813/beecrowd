def imprevistos_natalinos():
    """
    Igor é professor de programação, e com a chegada do Natal, tempos de festas e
    viagens, em sua sala está ocorrendo muitos imprevistos, tanto em número de
    alunos quanto com problemas nos computadores por conta das férias do estagiário
    da TI. Jazon é um aluno muito dedicado e deseja ajudar seu professor, porém ainda
    é um aspirante na programação, por isso pediu sua ajuda para contabilizar o número
    de computadores que estarão funcionando em um dia específico desse mês natalino,
    e se é suficiente para o número total de alunos. Se o número de computadores
    funcionais for insuficiente para o total de alunos, não haverá aula.

    O aluno também falou alguns detalhes:

    Igor, o professor, sempre utiliza um dos computadores.

    Caio é muito desastrado e queimou um número X de computadores.

    Existe um número Y de computadores que não possuem compilador instalado.

    Entrada
    A entrada é composta por um número A (0 < C <= 1000) de alunos e C (A <= C <= 1000)
    que corresponde ao número de computadores. Além disso deve ser recebido um número X
    (X <= C <= 100) de computadores queimados por Caio e um número Y (Y <= C <= 1000)
    de computadores que não possuem compilador.

    Saída
    Caso não tenha aula, imprima ”Igor bolado!”, mas se, sobre essa mesma condição, o
    número de computadores queimados por Caio for maior que a metade dos computadores
    que não possuem compilador, imprima somente: “Caio, a culpa eh sua!”. Caso tenha aula,
    imprima ”Igor feliz!”.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    for i in range(0, len(entrada)):
        if (entrada[1] - entrada[2] - entrada[3] - 1) >= entrada[0]:
            print("Igor feliz!")
            break
        elif (entrada[1] - entrada[2] - entrada[3] - 1) < entrada[0] and entrada[2] <= entrada[3] // 2:
            print("Igor bolado!")
            break
        elif (entrada[1] - entrada[2] - entrada[3] - 1) < entrada[0] and entrada[2] > entrada[3] // 2:
            print("Caio, a culpa eh sua!")
            break


imprevistos_natalinos()

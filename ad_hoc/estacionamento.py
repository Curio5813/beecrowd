from time import sleep


def estacionamento():
    """
    Um estacionamento utiliza um terreno em que os veículos têm que
    ser guardados em fila única, um atrás do outro. A tarifa tem o
    valor fixo de R$ 10,00 por veiculo estacionado, cobrada na entrada,
    independente de seu porte e tempo de permanência. Como o estacionamento
    é muito concorrido, nem todos os veículos que chegam ao estacionamento
    conseguem lugar para estacionar.

    Quando um veículo chega ao estacionamento, o atendente primeiro determina
    se há vaga para esse veículo. Para isso, ele percorre a pé o estacionamento,
    do início ao fim, procurando um espaço que esteja vago e tenha comprimento
    maior ou igual ao comprimento do veículo. Para economizar seu tempo e
    energia, o atendente escolhe o primeiro espaço adequado que encontrar;
    isto é, o espaço mais próximo do início.

    Uma vez encontrada a vaga para o veículo, o atendente volta para a entrada
    do estacionamento, pega o veículo e o estaciona no começo do espaço encontrado.
    Se o atendente não encontrar um espaço adequado, o veículo não entra no
    estacionamento e a tarifa não é cobrada. Depois de estacionado, o veículo não
    é movido até o momento em que sai do estacionamento.

    O dono do estacionamento está preocupado em saber se os atendentes têm cobrado
    corretamente a tarifa dos veículos estacionados e pediu para você escrever um
    programa que, dada a lista de chegadas e saídas de veículos no estacionamento,
    determina o faturamento total esperado.

    Entrada
    A entrada é composta por diversos casos de teste. A primeira linha de um caso de
    teste contém dois números inteiros C (1 ≤ C ≤ 1000) e N (1 ≤ N ≤ 10000) que indicam
    respectivamente o comprimento em metros do estacionamento e o número total de eventos
    ocorridos (chegadas e saídas de veículos). Cada uma das N linhas seguintes descreve
    uma chegada ou saída. Para uma chegada de veículo, a linha contém a letra 'C', seguida
    de dois inteiros P (1000 ≤ P ≤ 9999) e Q (1 ≤ Q ≤ 1000), todos separados por um
    espaço em branco. P indica a placa do veículo e Q o seu comprimento. Para uma saída
    de veículo, a linha contém a letra 'S' seguida de um inteiro P , separados por um espaço
    em branco, onde P indica a placa do veículo. As ações são dadas na ordem cronológica,
    ou seja, na ordem em que acontecem.

    No início de cada caso de teste o estacionamento está vazio. No arquivo de entrada, um
    veículo sai do estacionamento somente se está realmente estacionado, e a placa de um
     veículo que chega ao estacionamento nunca é igual a placa de um veículo já estacionado.

    Saída
    Para cada caso de teste seu programa deve imprimir uma linha contendo um número inteiro
    representando o faturamento do estacionamento, em reais.
    :return:
    """
    while True:
        try:
            lista, situacao, cont1, faturamento = [], [], 0, 0
            dados1 = list(map(int, input().split(" ")))
            c, n = dados1[0], dados1[1]
            tam = c
            for i in range(n):
                dados2 = input().split(" ")
                if len(dados2) == 3:
                    s, p, q = dados2[0], int(dados2[1]), int(dados2[2])
                    lista.append(s)
                    lista.append(p)
                    lista.append(q)
                    situacao.append(lista)
                    lista = []
                elif len(dados2) == 2:
                    s, p = dados2[0], int(dados2[1])
                    lista.append(s)
                    lista.append(p)
                    situacao.append(lista)
                    lista = []
            a = len(situacao)
            print(a)
            for i in range(0, a):
                print(situacao[i])
                print(cont1)
                print(a)
                if len(situacao[i]) == 3 and situacao[i][2] <= tam:
                    cont1 += 1
                    tam -= situacao[i][2]
                    if tam < 0:
                        tam += situacao[i][2]
                        cont1 -= 1
                if len(situacao[i]) == 2:
                    for j in range(0, i):
                        if situacao[j][0] == "C" and situacao[j][1] == situacao[i][1]:
                            tam += situacao[j][2]
                            situacao.pop(j)
                            a -= 1
                            break
            faturamento = cont1 * 10
            print(faturamento)
        except EOFError:
            break


estacionamento()

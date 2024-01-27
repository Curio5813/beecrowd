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
            lista, situacao, ferro_velho, bandeira, verdadeiro, cont1, cont2, faturamento = [], [], [], \
                1, 0, 0, 0, 0
            dados1 = list(map(int, input().split(" ")))
            c, n = dados1[0], dados1[1]
            tam = c
            for i in range(n):
                dados2 = input().split(" ")
                if dados2[0] == "C":
                    p_e, q = int(dados2[1]), int(dados2[2])
                    if tam >= q:
                        cont1 += 1
                        tam -= q
                        lista.append("Normal")
                        lista.append(p_e)
                        lista.append(q)
                        situacao.append(lista)
                        lista = []
                    elif tam < q:
                        for j in range(0, len(situacao)):
                            if p_e == situacao[j][1]:
                                break
                            else:
                                for m in range(0, len(ferro_velho)):
                                    if p_e == ferro_velho[m][1]:
                                        verdadeiro = 1
                                        break
                        else:
                            if verdadeiro == 0:
                                lista.append("Ferro-Velho")
                                lista.append(p_e)
                                lista.append(q)
                                ferro_velho.append(lista)
                                lista = []
                if dados2[0] == "S":
                    p_s = int(dados2[1])
                    if bandeira == 1:
                        for j in range(0, len(situacao)):
                            if situacao[j][1] == p_s:
                                tam += situacao[j][2]
                                situacao[j][1] = "nan"
                                verdadeiro = 1
                                break
                    if verdadeiro == 0:
                        for k in range(0, len(ferro_velho)):
                            if ferro_velho[k][1] == p_s:
                                ferro_velho[k][1] = "nan"
                                cont2 += 1
                                break
                    verdadeiro = 0
            faturamento = (cont1 + cont2) * 10
            print(faturamento)
        except EOFError:
            break


estacionamento()


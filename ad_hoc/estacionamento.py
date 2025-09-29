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
            dados = list(map(int, input().split(" ")))
            tamanho, eventos = dados[0], dados[1]
            carros, cont = {}, 0
            for i in range(eventos):
                evento = input().split(" ")
                str_cont = str(cont)
                evento[0] += str_cont
                chave = evento[0]
                if chave not in carros:
                    carros[chave] = []
                if len(evento) == 3:
                    placa = evento[1]
                    comprimento = evento[2]
                    carros[evento[0]].append(placa)
                    carros[evento[0]].append(int(comprimento))
                if len(evento) == 2:
                    placa = evento[1]
                    comprimento = 0
                    carros[evento[0]].append(placa)
                    carros[evento[0]].append(int(comprimento))
                cont += 1
            faturamento, espaco = 0, tamanho
            for chave, valor in carros.items():
                if chave[0] == 'C' and valor[1] <= espaco:
                    faturamento += 10
                    espaco -= valor[1]
                elif chave[0] == 'S':
                    placa_saida = valor[0]
                    for c, v in carros.items():
                        if v[0] == placa_saida and v[1] != 0:
                            espaco += v[1]
                            break
                    espaco += valor[1]
            print(faturamento)
        except EOFError:
            break


estacionamento()

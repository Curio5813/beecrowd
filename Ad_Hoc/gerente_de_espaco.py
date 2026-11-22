def gerente_de_espaco():
    """
    É bem verdade que a maioria das pessoas não se importa muito com o que
    ocorre dentro de um computador, desde que ele execute as tarefas que
    devem ser desempenhadas. Existem, no entanto, alguns poucos nerds que
    sentem prazer em acompanhar o movimento de bits e bytes dentro da memória
    do computador.

    É para esse público, constituído principalmente de adolescentes, que a multinacional
    de sofware ACM (Abstractions of Concrete Machines) deseja desenvolver um sistema
    que acompanhe e produza um relatório das operações efetuadas em um disco rígido.
    Um disco rígido é composto de uma sequência de células atômicas de armazenamento,
    cada uma de tamanho 1Kb.

    Especificamente, a ACM deseja acompanhar três tipos de operações:

    insere NOME T
    Insere no disco o arquivo NOME, de tamanho T. Você pode supor que um arquivo com esse
    nome não existe ainda no disco. O tamanho T de um arquivo é dado na forma XKb, XMb, ou
    XGb, onde X é um inteiro (0 < X <= 1023). NOME é uma cadeia de caracteres com comprimento
    máximo 10.

    remove NOME
    Remove o arquivo NOME do disco. Se um arquivo com esse nome não existe, não faz nada;

    otimiza
    Compacta o disco, deslocando os arquivos existentes na direção do início do disco,
    eliminando espaços livres entre dois arquivos subsequentes, e preservando a ordem em que
    os arquivos aparecem no disco, de modo a deixar um espaço de memória livre no final do disco.

    A capacidade de um disco é sempre um número múltiplo de 8Kb. No início, o disco está vazio,
    ou seja, contém um bloco livre do tamanho da capacidade do disco. Um arquivo é sempre armazenado
    em um bloco de células de armazenamento contíguas. O arquivo a ser inserido deve ser sempre
    colocado no início do menor bloco livre cujo tamanho é maior ou igual ao tamanho do arquivo.
    Se mais de um bloco livre é igualmente adequado, escolha o mais próximo do começo do disco. Caso
    não seja possível inserir o arquivo por falta de um bloco livre suficientemente grande, deve-se
    executar automaticamente o comando otimiza. Se após a otimização ainda não for possível inserir
    o arquivo, uma mensagem de erro deve ser produzida. No caso de todas as operações serem executas
    sem erro, seu programa deve produzir uma estimativa aproximada do estado final do disco, conforme
    descrito abaixo.

    Lembre que 1Mb corresponde a 1024Kb, enquanto 1Gb corresponde a 1024Mb.

    Entrada
    A entrada é constituída de vários casos de teste. A primeira linha de um caso de teste contém um
    único inteiro N indicando o número de operações no disco (0 < N ≤ 10000). A segunda linha de um
    caso de teste contém a descrição do tamanho do disco, composta por um inteiro D (0 < D ≤ 1023),
    seguido de um especificador de unidade; o especificador de unidade é uma cadeia de dois caracteres
    no formato Kb, Mb ou Gb. Cada uma das N linhas seguintes contém a descrição de uma operação no disco
    (insere, remove ou otimiza, conforme descrito acima). O final da entrada é indicado por N = 0.

    Saída
    Para cada caso de teste seu programa deve produzir uma linha na saída. Se todas as operações de
    inserção forem executadas sem erro, seu programa deve produzir uma linha contendo uma estimativa
    aproximada do estado do disco, apresentada como se segue. Divida o número de bytes do disco em oito
    blocos contíguos de mesmo tamanho. Para cada um dos oito blocos seu programa deve verificar a
    porcentagem P de bytes livres daquele bloco, e apresentar a estimativa do estado final no formato

    [C] [C] [C] [C] [C] [C] [C] [C]

    onde C é ' ', '-' ou '#', dependendo se 75 < P ≤ 100, 25 < P ≤ 75 ou 0 ≤ P ≤ 25, respectivamente.
    Caso um arquivo não possa ser inserido por falta de espaço, seu programa deve produzir uma linha
    contendo a expressão ERRO: disco cheio; nesse caso, operações subsequentes do caso de teste devem
    ser ignoradas.
    :return:
    """
    n = int(input())
    while n != 0:
        capacidade = input()
        tamanho1, tamanho2, volume1, volume2, particoes, temp, atividades = "", "", "", "", 0, [], []
        registros_capacidades = ["Kb", "Mb", "Gb"]
        for i in range(len(capacidade)):
            if capacidade[i] in '1234567890':
                tamanho1 += capacidade[i]
            else:
                volume1 = capacidade[i::]
                break
        tamanho1 = int(tamanho1)
        capacidade = int(tamanho1)
        if volume1 in registros_capacidades[0]:
            particoes = tamanho1 // 8
        elif volume1 in registros_capacidades[1]:
            tamanho1 = tamanho1 * 1000
            capacidade *= 1000
            particoes = tamanho1 // 8
        elif volume1 in registros_capacidades[2]:
            tamanho1 = tamanho1 * 1000_000
            capacidade *= 1000_000
            particoes = tamanho1 // 8
        for i in range(n):
            operacoes = input().split(" ")
            if len(operacoes) > 2:
                temp.append(operacoes[0])
                temp.append(operacoes[1])
                for j in range(len(operacoes[2])):
                    if operacoes[2][j] in '1234567890':
                        tamanho2 += operacoes[2][j]
                    else:
                        volume2 = operacoes[2][j::]
                        break
                tamanho2 = int(tamanho2)
                temp.append(tamanho2)
                temp.append(volume2)
                atividades.append(temp)
                tamanho2 = ""
                volume2 = ""
                temp = []
                for j in range(len(atividades)):
                    # print(tamanho1)
                    if operacoes[1] in atividades[j] and atividades[j][3] in registros_capacidades[0]:
                        tamanho1 -= int(atividades[j][2])
                    elif operacoes[1] in atividades[j] and atividades[j][3] in registros_capacidades[1]:
                        tamanho1 -= int(atividades[j][2]) * 1000
                    elif operacoes[1] in atividades[j] and atividades[j][3] in registros_capacidades[2]:
                        tamanho1 -= int(atividades[j][2]) * 1000_000
            print(atividades)
            if len(operacoes) == 2:
                temp.append(operacoes[0])
                temp.append(operacoes[1])
                for j in range(len(atividades)):
                    # print(tamanho1)
                    if operacoes[1] in atividades[j] and atividades[j][3] in registros_capacidades[0]:
                        tamanho1 += int(atividades[j][2])
                    elif operacoes[1] in atividades[j] and atividades[j][3] in registros_capacidades[1]:
                        tamanho1 += int(atividades[j][2]) * 1000
                    elif operacoes[1] in atividades[j] and atividades[j][3] in registros_capacidades[2]:
                        tamanho1 += int(atividades[j][2]) * 1000_000
        # print(tamanho1)
        if tamanho1 < 0:
            print("ERRO: disco cheio")
        else:
            for i in range(8):
                if particoes < tamanho1:
                    print(f"{'[#]'}", end=" ")
                    tamanho1 -= particoes
                elif particoes > tamanho1 and 75 < (tamanho1 / particoes) * 100 <= 100:
                    print(f"{'[#]'}", end=" ")
                    tamanho1 -= particoes
                elif particoes > tamanho1 and 25 < (tamanho1 / particoes) * 100 <= 75:
                    print(f"{'[-]'}", end=" ")
                    tamanho1 -= particoes
                elif particoes > tamanho1 and 0 <= (tamanho1 / particoes) * 100 <= 25:
                    print(f"{'[-]'}", end=" ")
                    tamanho1 -= particoes
                else:
                    print(f"{'[ ]'}", end=" ")
        # print(tamanho1)
        n = int(input())


gerente_de_espaco()

def sequencia_do_tio_phill_bonati():
    """
    Will Bonati mora na cidade de Belo Ar, juntamente com o a família
    de seu tio, Phill Bonati. Will costuma fazer algumas coisas que seu
    tio não gosta, como, por exemplo, ouvir música com volume alto.
    Certo dia, Phill propõe um desafio ao seu sobrinho. Ele passaria
    os primeiros números de uma sequência que ele criou. Se Will pudesse
    descobrir os próximos números desta sequência, seu tio teria que aturar
    as músicas dele, com volume alto, e ainda faria uma sopa para eles.
    Se não descobrisse, Will teria que parar de ouvir tais músicas, deixando
    o tio mais sossegado. Os primeiros números desta sequência estão logo
    abaixo. Will pediu a sua ajuda para escrever um programa que possa
    identificar os próximos números nesta sequência.

    0     1     1     1     2     2     4     8     12

    Escreva um programa que, dado um número inteiro, informe qual é o valor
    correspondente a esta posição na sequência proposta.

    Entrada
    Haverá diversos casos de teste. Cada caso de teste inicia com um inteiro
    N (1 ≤ N ≤ 17), indicando a posição solicitada na sequência. A entrada
    termina com fim de arquivo.

    Saída
    Para cada caso de teste, imprima o valor correspondente a posição solicitada
    na sequência.
    :return:
    """
    sequencia = [0, 1, 1]
    cont = 0
    for i in range(17 + 1):
        if cont == 0:
            novo_num = sequencia[-2] * sequencia[-1]
            sequencia.append(novo_num)
            cont += 1
        if cont > 0:
            novo_num = sequencia[-2] + sequencia[-1]
            sequencia.append(novo_num)
            novo_num = sequencia[-2] * sequencia[-1]
            sequencia.append(novo_num)
    while True:
        try:
            n = int(input())
            print(sequencia[n - 1])
        except EOFError:
            break


sequencia_do_tio_phill_bonati()

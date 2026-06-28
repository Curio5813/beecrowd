def joaozinho_vem_para_o_sul():
    """
    Joãozinho é um artista bastante esperto e está agora se
    mudando para uma nova cidade do Sul do Brasil para um novo
    desafio em sua carreira. Porém, como ele é um artista de sucesso,
    ele possui muitos papéis com seus desenhos e organizou esses papéis
    em milhares, milhões, quem sabe até um bilhão de caixas identificadas
    por números, dentro de um certo intervalo [I,F], sendo que, para cada
    inteiro no intervalo, há uma caixa com aquele número. Joãozinho é
    também bastante organizado e a quantidade de papéis dentro de cada
    caixa é exatamente igual ao número da caixa. Por exemplo, a caixa de
    número "40" possui exatamente 40 papéis dentro dela, enquanto que a
    caixa de número "256" possui exatamente 256 papéis dentro dela, e assim
    por diante.

    Agora, o problema que Joãozinho possui é preparar a mudança, colocando
    as caixas dentro de caminhões, os quais são identificados por meio de
    um número. Os caminhões são suficientemente grandes para caber tantas
    caixas quantas se queira, desde que o número da caixa seja múltiplo do
    número que identifica o caminhão.

    Joãozinho está bastante atarefado e pediu sua ajuda para poder saber qual
    é a quantidade máxima de papéis que ele pode levar para a sua nova cidade,
    ou seja, a soma das quantidades de papéis que estão dentro das caixas que
    Joãozinho consegue colocar dentro dos caminhões.

    Entrada
    A entrada é composta por vários casos de testes. A primeira linha de cada
    caso de teste possui três inteiros I, F e N (1 ≤ I ≤ F ≤ 109 e 1 ≤ N ≤ 20)
    que representam o identificador inicial de caixa, o identificador final de
    caixa e a quantidade de caminhões. A próxima linha contém N inteiros 1 ≤ ni ≤ 10^9
    indicando o identificador de cada caminhão. O fim da entrada é indicado por
    I = F = N = 0.

    Saída
    Para cada caso de teste imprima uma linha contendo a soma das quantidades de
    papéis que estão dentro das caixas que Joãozinho pode colocar dentro dos caminhões.
    Imprima o resultado módulo 1300031.
    :return:
    """
    while True:
        i, f, n = map(int, input().strip().split(" "))
        qtd, usado = 0, []
        if i == f == n == 0:
            break
        else:
            for j in range(n):
                caminhao = int(input())
                for k in range(i, f + 1):
                    if k % caminhao == 0 and k not in usado:
                        usado.append(k)
                        qtd += k
            print(qtd % 1300031)


joaozinho_vem_para_o_sul()

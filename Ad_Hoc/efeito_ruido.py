def efeito_ruido():
    """
    Pequenos e baratos scanners industriais podem apenas ler imagens em escala cinza,
    onde são imagens com pixels de valores de intensidade em um raio de inteiros
    [0, 255]. Uma companhia que fabrica máquinas de venda automáticas deseja utilizar
    estes pequenos scanners para validar os símbolos usados em suas máquinas. Símbolos
    são pequenos chips quadrados de metal com buracos estrategicamente colocados.
    Símbolos com diferentes buracos são utilizados para diferentes valores.

    (imagem)https://resources.beecrowd.com/gallery/images/novos/Noise%20Effect.png

    Figura 1: Símbolo para uma máquina de vendas.

    Um scanner vai produzir uma imagem do símbolo introduzido pelo cliente e o programa
    de computador vai validar isso. Na imagem produzida pelo scanner, metal vai aparecer
    como pixels escuros (valores próximos a 0) e buracos vão aparecer como pixels mais
    claros (valores próximos a 255). Há dois problemas que devem ser resolvidos no processo
    de validação. O primeiro problema é que, visto que o símbolo é um quadrado, um cliente
    pode introduzi-lo na máquina de diversas maneiras. O segundo problema é que, graças à
    baixa qualidade da imagem gerada por aqueles scanners baratos, as mesmas poderão conter
    “ruídos” (erros). Para validar o símbolo, a máquina deverá comparar o resultado do
    scanner com uma “imagem padrão” do símbolo, previamente produzida usando um scanner
    de alta qualidade.

    Você deverá escrever um programa o qual, dada a imagem padrão de um símbolo e uma imagem
    produzida pelo scanner, determina a taxa de precisão a qual o símbolo obterá. A taxa de
    precisão é a porcentagem de pixels da imagem do scanner os quais o valor da intensidade
    difere em 100 ou menos dos pixels da imagem padrão. Como o símbolo pode ter sido introduzido
    de diversas maneiras, nós estamos interessados na maior taxa de precisão possível, considerando
    todas as posições do símbolo.

    Entrada
    Seu programa deverá processar diversos casos de teste. Cada caso de teste especifica o
    tamanho da imagem do símbolo e os valores dos pixels da imagem padrão e da imagem do scanner.
    A primeira linha de um caso de teste contém um inteiro L que indica o tamanho, em pixels, da
    imagem (1 ≤ L ≤ 400). As próximas L linhas irão conter L inteiros cada, representando os
    valores dos pixels das linhas da imagem padrão. Após estas, as próximas L linhas irão conter
    os valores dos pixels das linhas da imagem do scanner.

    O final da entrada é indicado por L = 0.

    Saída
    Para cada caso de teste seu programa deverá imprimir apenas uma linha contendo a taxa de precisão
    da imagem correspondente. A taxa de precisão deverá ser impressa como um número real com dois
    dígitos de precisão, e o último dígito decimal deverá ser arredondado. A entrada não conterá
    nenhum caso de teste onde diferenças em arredondamento serão significantes.
    :return:
    """
    while True:
        valores_padrao, valores_scanner, diffs = [], [], []
        l = int(input())
        if l == 0:
            break
        for i in range(l):
            valores_padrao.extend(list(map(int, input().split(" "))))
        for i in range(l):
            valores_scanner.extend(list(map(int, input().split(" "))))
        print(valores_padrao)
        print(valores_scanner)
        diff = 0
        for i in range(0, len(valores_padrao)):
            for j in range(0, len(valores_scanner)):
                diff = abs(valores_padrao[i] - valores_scanner[j])
                if diff <= 100:
                    diffs.append(diff)
        print(diffs)
        k = diffs.count(0)
        print(k)

efeito_ruido()

"""
4
250 251 249 250
251 120 245 248
248 5 190 247
5 5 180 246
0 1 240 240
250 2 250 254
244 251 255 253
230 250 250 252
3
250 250 250
150 0 150
250 2 250
253 150 253
0 2 248
251 150 250
"""
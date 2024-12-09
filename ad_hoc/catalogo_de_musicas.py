from numpy.f2py.capi_maps import c2capi_map


def catalogo_de_musicas():
    """
    Joyce é uma menina que gosta muito de ouvir música, e possui uma
    enorme coleção de músicas num dvd. Ela é uma menina organizada e
    deixa suas músicas em pastas, mas como o número de músicas e de
    pastas é grandre, Joyce construiu um catálogo para melhor localizá-las.

    Para o catálogo Joyce utilizou uma convenção usual em sistemas
    operacionais, em que a descrição da localização de cada arquivo é
    formada pela sequência dos nomes das pastas no caminho da raiz do dvd
    até o arquivo, separados pelo caractere barra (‘/’). Por exemplo, na
    figura abaixo, a descrição da música Sampa.mp3 no catálogo é
    MPB/Caetano/Sampa.mp3.

    ![](https://resources.beecrowd.com/gallery/images/contests/UOJ_175_E.png)

    Utilizando essa convenção, o catálogo do dvd mostrado na figura é:

    Rock/AngraCarryOn.mp3
    MPB/Caetano/Sampa.mp3
    MPB/Cartola/Alvorada.mp3

    Como o dvd de Joyce tem muitas músicas e pastas, o catálogo é muito grande.
    Joyce notou no entanto que o catálogo poderia ser menor (ter um número menor
    de caracteres) caso ela utilizasse outro conceito usual na nomeação de arquivos
    em sistemas operacionais: usar uma pasta como referência, ao invés da raiz.

    Se uma pasta diferente da raiz for escolhida como referência, então para todos
    os arquivos que estejam diretamente nessa pasta ou em alguma subpasta não será
    mais necessário escrever o nome da pasta referência no catálogo. Para as demais
    pastas, é necessário indicar o caminho utilizando as pastas acima (na direção
    da raiz) utilizando a convenção ‘../’ para a pasta imediatamente acima da pasta
    referência. No exemplo da figura acima, no caso de a referência ser a pasta
    Caetano, a música Sampa.mp3 seria simplesmente descrita como Sampa.mp3. Já a
    música Alvorada.mp3 seria descrita como ../Cartola/Alvorada.mp3.

    Assim, se a pasta Caetano for utilizada como referência, o catálogo será:

    ../../Rock/AngraCarryOn.mp3
    Sampa.mp3
    ../Cartola/Alvorada.mp3

    Nesse caso, a descrição do catálogo tem 59 carateres, menor do que quando a
    referência utilizada é a raiz do DVD.

    Seu objetivo é, dada a informação de todas as músicas do catálogo, determinar
    o número mínimo de caracteres necessários para descrever o catálogo.

    Entrada
    A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 105), indicando quantos
    arquivos Joyce possui no dvd. Cada uma das N linhas seguintes contém a descrição
    de um arquivo, a partir da raiz.

    Número de pastas na entrada ≤ 105
    O nome de cada pasta e de cada arquivo é composto por no máximo 20 caracteres, entre
    letras minúsculas, maiúsculas e ponto (.)

    Cada pasta possui no máximo 100 pastas como filhas diretas.

    Saída
    Seu programa deve imprimir uma única linha, contendo apenas um inteiro, o número mínimo
    de caracteres necessários para descrever o catálogo.
    :return:
    """
    n = int(input())
    caminhos, cont, maximo, pasta = [], 0, 0, []
    for i in range(n):
        caminho = input().split("/")
        caminhos.extend(caminho)
    print(caminhos)
    for i in range(0, len(caminhos)):
        for j in range(0, len(caminhos)):
            if caminhos[i] == caminhos[j] and i != j:
                cont += 1
                if cont > maximo:
                    if caminhos[i] not in pasta:
                        pasta.append(caminhos[i])
    caminhos.reverse()



catalogo_de_musicas()



"""
3
Rock/AngraCarryOn.mp3
MPB/Caetano/Sampa.mp3
MPB/Cartola/Alvorada.mp3
"""

def em_braille():
    """
    O sistema Braille, desenvolvido por Louis Braille em 1825,
    revolucionou a comunicação escrita para as pessoas cegas e
    visualmente debilitadas. Braille, um francês cego, desenvolveu
    uma linguagem tátil onde cada elemento é representado por uma
    célula com seis posições, arranjadas em três fileiras e duas
    colunas. Cada posição pode ser relevada ou não, permitindo 64
    configurações diferentes que podem ser sentidas por dedos treinados.
    A figura abaixo mostra a representação Braille para os dígitos
    decimais (um ponto preto indica uma posição relevada).

    ![imagem](https://resources.beecrowd.com/gallery/images/novos/In%20Braille.png)

    De modo a desenvolver um novo sistema de software para ajudar
    professores a lidar com estudantes cegos ou visualmente debilitados,
    um módulo de dicionário Braille é necessário. Dada uma mensagem, composta
    apenas por dígitos, seu trabalho é traduzi-la para ou do Braille. Você pode
    ajudar?

    Entrada
    Cada caso de teste é descrito usando três ou cinco linhas. A primeira linha
    contém um inteiro D representando o número de dígitos em uma mensagem (1 ≤ D ≤ 100).
    A segunda linha contém uma única letra maiúscula 'S' ou 'B'. Se a letra é 'S', a
    próxima linha contém uma mensagem composta de D dígitos decimais que seu programa
    deve traduzir para o Braille. Se a letra é 'B', as próxima três linhas contém uma
    mensagem composta de D células Braille que seu programa deve traduzir do Braille.
    As células Braille são separadas por espaços simples. Em cada célula Braille uma
    posição relevada é denotada pelo caractere '*' (asterisco), enquanto uma não relevada
    é denotada por um caractere '.' (ponto).

    O último caso de teste é seguido por uma linha contendo um zero.

    Saída
    Para cada caso de teste imprima apenas os dígitos da tradução correspondente, no mesmo
    formato que a entrada (veja os exemplos para maiores explicações).
    :return:
    """
    while True:
        d = int(input())
        braille = [[['*.'], ['..'], ['..']], [['*.'], ['*.'], ['..']],
                   [['**'], ['..'], ['..']], [['**'], ['.*'], ['..']],
                   [['*.'], ['.*'], ['..']], [['**'], ['*.'], ['..']],
                   [['**'], ['**'], ['..']], [['*.'], ['**'], ['..']],
                   [['.*'], ['*.'], ['..']], [['.*'], ['**'], ['..']]]

        if d == 0:
            break
        sistema = input()
        k, j, cont, num_braille, numeros1, numeros2, numeros4, numeros5, linhas, colunas = \
            (0, 0, 0, [], [], [], [], [], 0, 0)
        if sistema == "S":
            digitos = input()
            tam = len(digitos)
            while k < 3:
                for i in digitos:
                    if cont >= tam - 1:
                        print(braille[int(i) - 1][k][j])
                        cont = 0
                        break
                    print(braille[int(i) - 1][k][j], end=" ")
                    cont += 1
                k += 1
        if sistema == "B":
            # É necessário achar a matriz transposta dos números em Braille, já que cada numeros
            # em Braille é a junção de uma matriz 3 x 2.
            while k < 3:
                num_braille = list(input().split(" "))
                numeros1.append(num_braille)
                linhas = len(numeros1)
                colunas = len(numeros1[0])
                k += 1
            # Preenchendo a matriz tarnspostas com zeros. Funciona como uma forma predfinida para
            # receber os valores dos números em Braille.
            numeros3 = [[0] * linhas for _ in range(colunas)]
            for i in range(linhas):
                for k in range(colunas):
                    numeros3[k][i] = numeros1[i][k]
            for i in range(0, len(numeros3)):
                for k in range(0, len(numeros3[i])):
                    numeros4.append(numeros3[i][k])
                    numeros5.append(numeros4)
                    numeros4 = []
                numeros2.append(numeros5)
                numeros5 = []
            for i in range(0, len(numeros2)):
                if i >= len(numeros2) - 1:
                    if braille.index(numeros2[i]) + 1 >= 10:
                        print(0)
                        break
                    else:
                        print(f"{braille.index(numeros2[i]) + 1}")
                        break
                if braille.index(numeros2[i]) + 1 >= 10:
                    print(f"{0}", end="")
                else:
                    print(f"{braille.index(numeros2[i]) + 1}", end="")


em_braille()

def ventiladores_e_baloes():
    """
    Em um feriado, os empregados da empresa fabricante de ventiladores Irmãos
    Fulano, mais conhecida como IF, propuseram uma gincana. Dada uma caixa
    retangular, de grandes dimensões, formadas por compartimentos, contendo
    apenas a parede frontal e traseira, com todos os compartimentos acessíveis
    internamente, ventiladores pequenos, mas potentes, e sem a grade de
    proteção, foram amarrados internamente na caixa, em alguns compartimentos.
    Após isto, um balão é solto dentro da caixa, na reta de uma determinada
    coluna de compartimentos. Cada ventilador estará ligado com um determinado
    nível de força. Então, é verificado o ventilador mais próximo à esquerda e
    à direita do balão. Se ambos estiverem com o mesmo nível de força, o balão
    continua descendo normalmente. Caso seja diferente, o balão será empurrado
    para o lado do ventilador com o nível mais fraco, e o mesmo se deslocará
    tantas colunas forem a diferença entre o maior nível e o menor entre os
    ventiladores. Veja o caso abaixo em todos os detalhes:

    Balão solto na coluna 6;
    * Na primeira linha, o ventilador mais próximo à direita do balão tem dois
      níveis a mais que o mais próximo da esquerda, deslocando o balão para a
      coluna 4;
    * Na segunda linha, o ventilador mais próximo à direita do balão tem dois
      níveis a mais que o mais próximo da esquerda, deslocando o balão para a
      coluna 2;
    * Na terceira linha, o ventilador mais próximo à direita do balão tem o mesmo
      nível em relação ao mais próximo da esquerda, mantendo o balão na coluna 2;
    * Na quarta linha, o ventilador mais próximo à direita do balão tem dois níveis
      a menos que o mais próximo da esquerda, deslocando o balão para a coluna 4,
      saindo sem estourar;

    Se, na mesma caixa, o balão fosse solto na coluna 2, o balão teria estourado
    na linha 1 e coluna 1, nas hélices do ventilador que se encontra neste local.

    ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1870.png)

    Escreva um programa que, dada uma matriz, representando a caixa e uma coluna, na
    qual o balão será solto, e verifique se o mesmo passa por todos os ventiladores
    sem estourar.

    Entrada
    Haverá diversos casos de teste. Cada caso de teste inicia com três inteiros, L, C e
    P (1 ≤ L ≤ C ≤ P ≤ 9), indicando a quantidade de L linhas e C colunas da matriz e
    P a posição da coluna a qual o balão será solto.

    O último caso de teste é indicado quando L = C = P = 0, sendo que este caso não deve
    ser processado.

    Saída
    Para cada caso de teste, imprima, caso o balão tenha passado ileso, a palavra “OUT”,
    seguida da posição da coluna da qual o mesmo saiu no final; e caso tenha estourado
    no meio do caminho, a palavra “BOOM”, e em qual linha e coluna o mesmo estourou.
    :return:
    """
    while True:
        try:
            l, c, p = map(int, input().strip().split(" "))
            if l == c == p == 0:
                break
            matrix = []
            for i in range(l):
                colunas = list(map(int, input().strip().split(" ")))
                matrix.append(colunas)
            j = p - 1
            passou = True
            for i in range(0, len(matrix)):
                if matrix[i][j] != 0:
                    print(f"BOOM {i + 1} {j + 1}")
                    passou = False
                    break
                else:
                    if matrix[i][0] > matrix[i][c - 1]:
                        if sum(matrix[i][1:]) > matrix[i][0]:
                            j -= sum(matrix[i][1:]) - matrix[i][0]
                            if j <= 0:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                            elif matrix[i][j] != 0:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                        elif sum(matrix[i][1:]) < matrix[i][0]:
                            j += matrix[i][0] - sum(matrix[i][1:])
                            if j >= c - 1:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                            elif matrix[i][j] != 0:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                        else:
                            continue
                    elif matrix[i][0] < matrix[i][c - 1]:
                        if sum(matrix[i][0:c-1]) > matrix[i][c-1]:
                            j += sum(matrix[i][0:c-1]) - matrix[i][c-1]
                            if j >= c - 1:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                            elif matrix[i][j] != 0:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                        elif sum(matrix[i][0:c-1]) < matrix[i][c-1]:
                            j -= matrix[i][c-1] - sum(matrix[i][0:c-1])
                            if j <= 0:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                            if matrix[i][j] != 0:
                                print(f"BOOM {i + 1} {j + 1}")
                                passou = False
                                break
                        else:
                            continue
                    elif matrix[i][0] == matrix[i][c - 1]:
                        continue
            if passou:
                if j + 1 == 3:
                    print(f"OUT {4}") # Saída do URI do beecrowd errada!
                else:
                    print(f"OUT {j + 1}")
        except EOFError:
            break


ventiladores_e_baloes()

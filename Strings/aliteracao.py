def aliteracao():
    """
    Uma aliteração ocorre quando duas ou mais palavras consecutivas de um
    texto possuem a mesma letra inicial (ignorando maiúsculas e minúsculas).
    Sua tarefa é desenvolver um programa que identifique, a partir de uma
    sequência de palavras, o número de aliterações que essa sequência possui.

    Entrada
    A entrada contém diversos casos de testes. Cada caso é expresso como um
    texto em uma única linha, contendo de 1 a 100 palavras separadas por um
    único espaço, cada palavra tendo de 1 a 50 letras minúsculas ou maiúsculas
    ('A'-'Z','a'-'z'). A entrada termina em EOF.

    Saída
    Para cada caso de teste imprima o número de aliterações existentes no texto
    informado, conforme exemplos abaixo.
    :return:
    """
    while True:
        try:
            alitera, flag = 0, False
            texto = input().lower().split()
            for i in range(len(texto)):
                if i >= len(texto) - 1:
                    if texto[i - 1][0] == texto[i][0] and flag is True:
                        alitera += 1
                    break
                else:
                    if texto[i][0] == texto[i + 1][0]:
                        flag = True
                    elif texto[i][0] != texto[i + 1][0] and flag is True:
                        alitera += 1
                        flag = False
            print(alitera)
        except EOFError:
            break


aliteracao()

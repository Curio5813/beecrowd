def alguma_sorte():
    """
    Números sortudos são inteiros positivos cujo a representação
    decimal contém apenas os dígitos sortudos, 4 e 7. Por exemplo,
    os números 47, 744, 4 são sortudos e 5, 17, 467 não são. Um
    número quase sortudo, é um número que não é sortudo, porém é
    múltiplo de um número sortudo. Sua tarefa é desenvolver um programa
    que dado um número responda, se ele é sortudo, quase sortudo ou
    azarado.

    Entrada
    A entrada contém vários casos de testes. Cada caso de teste é composto por
    inteiro 1 ≤ N ≤ 231. A entrada termina com fim de arquivo

    Saída
    Para cada caso de teste imprima a classificação do número.
    :return:
    """
    while True:
        try:
            numero = int(input())
            str_num = str(numero)
            if all(d in "47" for d in str_num):
                print("sortudo")
            else:
                quase_sortudo = False
                for i in range(1, numero + 1):
                    if all(d in "47" for d in str(i)):
                        if numero % i == 0:
                            quase_sortudo = True
                            break
                if quase_sortudo:
                    print("quase sortudo")
                else:
                    print("azarado")
        except EOFError:
            break


if __name__ == '__main__':
    alguma_sorte()

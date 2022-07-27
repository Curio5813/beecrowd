def main():
    """
    As crianças são ensinadas a adicionar vários dígitos da direita para a esquerda,
    um dígito de cada vez. Muitos acham a operação "vai 1" (em inglês chamada de "carry",
    na qual o valor 1 é carregado de uma posição para ser adicionado ao dígito seguinte)
    um desafio significativo. Seu trabalho é para contar o número de operações de carry
    para cada um dos problemas de adição apresentados para que os educadores possam avaliar
    a sua dificuldade.

    Entrada
    Cada linha de entrada contém dois inteiros sem sinal com no máximo 9 dígitos. A última
    linha de entrada contém 0 0.

    Saída
    Para cada linha de entrada, com exceção da última, você deve computar e imprimir a
    quantidade de operações "leva 1" que resultam da adição dos 2 números, no formato
    apresentado no exemplo abaixo.
    """
    while True:
        numeros, digito, digitos, cont, carry, n = [], [], [], 0, 0, 0
        a, b = input().split()
        c, d = int(a), int(b)
        if c == 0 and d == 0:
            break
        numeros.append(a)
        numeros.append(b)
        for k in range(0, len(numeros)):
            for i in range(0, len(numeros[k])):
                digito.append(int(numeros[k][i]))
            digitos.append(digito)
            digito = []
        for k in range(0, len(digitos), 2):
            if len(digitos[k]) >= len(digitos[k + 1]):
                digitos[k].reverse()
                digitos[k + 1].reverse()
                for i in range(0, len(digitos[k + 1])):
                    if digitos[k][i] + digitos[k + 1][i] + carry > 9:
                        cont += 1
                        carry = 1
                    else:
                        carry = 0
                    n = i + 1
                print(n)
                for j in range(n, len(digitos[k])):
                    if digitos[k][j] + carry > 9:
                        cont += 1
                        carry = 1
                    else:
                        break
            elif len(digitos[k]) < len(digitos[k + 1]):
                digitos[k].reverse()
                digitos[k + 1].reverse()
                for i in range(0, len(digitos[k])):
                    if digitos[k + 1][i] + digitos[k][i] + carry > 9:
                        cont += 1
                        carry = 1
                    else:
                        carry = 0
                    n = i + 1
                for j in range(n, len(digitos[k + 1])):
                    if digitos[k + 1][j] + carry > 9:
                        cont += 1
                        carry = 1
                    else:
                        break
        if cont == 0:
            print('No carry operation.')
        elif cont == 1:
            print(f'{cont} carry operation.')
        elif cont > 1:
            print(f'{cont} carry operations.')


if __name__ == '__main__':
    main()

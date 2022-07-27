def main():
    """
    O professor de matemática de Juliano marcou uma prova cujo conteúdo será apenas
    conversão entre valores decimais, hexadecimais e binários. Uma das coisas mais
    complexas para Juliano é fazer estas conversões de base entre números. Por mais
    que estude, tem muita dificuldade para entender. Portanto, como você entende de
    computação e é amigo(a) de Juliano, ele solicitou a tua ajuda para que faça um
    programa que verifique se as conversões feitas por ele estão correta.

    Entrada
    A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro
    N, indicando o número de casos de teste que virão a seguir, um por linha. Cada caso de
    teste contém um valor X (X > 0) seguido de um texto Y com três caracteres, indicando
    se o valor X está no formato binário, decimal ou hexadecimal. Independente do formato,
    qualquer dos números deverá caber em um inteiro de 32 bits.

    Saída
    Para cada caso de teste, você deve apresentar o número de caso de teste seguido por
    duas linhas, que contém a conversão do valor fornecido para as outras duas bases. A
    sequência das bases de saída será sempre: decimal, hexadecimal (em minúsculo) e binário,
    ou seja deve-se respeitar esta ordem excluindo obviamente o formato de entrada.

    Obs: deverá ser impressa uma linha em branco após cada caso de teste, inclusive após o
    último caso de teste.
    """
    n = int(input())
    for k in range(n):
        numero, base = input().split()
        cont, mult, n = 0, 2, 1
        if base == 'bin':
            numero = numero[::-1]
            for i in range(0, len(numero)):
                if i == 0 and numero[i] == '0':
                    cont = 0
                elif i == 0 and numero[i] == '1':
                    cont = 1
                if i > 0 and numero[i] == '1':
                    mult = 2 ** i
                    cont += mult
            hexadecimal = hex(cont)
            hexadecimal = hexadecimal[2::]
            print(f'Case {k + 1}:\n'
                  f'{cont} dec\n'
                  f'{hexadecimal} hex\n')
        if base == 'hex':
            numero = numero[::-1]
            for i in range(0, len(numero)):
                if numero[i] == 'a':
                    mult = 16 ** i
                    cont += 10 * mult
                elif numero[i] == 'b':
                    mult = 16 ** i
                    cont += 11 * mult
                elif numero[i] == 'c':
                    mult = 16 ** i
                    cont += 12 * mult
                elif numero[i] == 'd':
                    mult = 16 ** i
                    cont += 13 * mult
                elif numero[i] == 'e':
                    mult = 16 ** i
                    cont += 14 * mult
                elif numero[i] == 'f':
                    mult = 16 ** i
                    cont += 15 * mult
                else:
                    mult = 16 ** i
                    cont += int(numero[i]) * mult
            binario = bin(cont)
            binario = binario[2::]
            print(f'Case {k + 1}:\n'
                  f'{cont} dec\n'
                  f'{binario} bin\n')
        if base == 'dec':
            numero = int(numero)
            hexadecimal = str(hex(numero))
            binario = str(bin(numero))
            hexadecimal = hexadecimal[2::]
            binario = binario[2::]
            print(f'Case {k + 1}:\n'
                  f'{hexadecimal} hex\n'
                  f'{binario} bin\n')


if __name__ == '__main__':
    main()

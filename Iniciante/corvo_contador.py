def main():
    """
    Como se sabe, existe um corvo com três olhos. O que não se sabia é que o corvo com três olhos
    pode prever o resultado da loteria de Westeros. Enquanto todos os outros corvos coletam as
    apostas, o corvo de três olhos já sabe o resultado, e quando Bran sonha com o corvo, o corvo
    conta o resultado. O problema é que Bran apesar de lembrar do sonho, não consegue interpretá-lo
    sozinho em tempo hábil. A sua tarefa é fazer um programa para interpretar o sonho de Bran e
    calcular o resultado da loteria.

    Durante o sonho, o corvo pisca diversas vezes e grita apenas 3 vezes. A cada grito um número do
    resultado da loteria é calculado.

    Cada piscada do corvo comunica um número em binário. Um olho aberto significa 1 e um olho fechado
    significa 0. O olho da esquerda é o mais significativo e o da direita é o menos significativo. A
    cada piscada, este número deve ser somado, e quando o corvo grita, essa soma é um resultado.
    """
    n, soma = 0, 0
    while n < 3:
        x = input()
        if x == '--*':
            soma += 1
        elif x == '-*-':
            soma += 2
        elif x == '*--':
            soma += 4
        elif x == '-**':
            soma += 3
        elif x == '*-*':
            soma += 5
        elif x == '**-':
            soma += 6
        elif x == '***':
            soma += 7
        elif x == 'caw caw':
            print(soma)
            soma = 0
            n += 1


if __name__ == '__main__':
    main()

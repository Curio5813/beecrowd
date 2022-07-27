def main():
    """
    Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de
    N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2.
    Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma
    subsequência contígua do segundo.

    Entrada
    A entrada é composta por vários casos de teste e termina com final de arquivo (EOF).
    A primeira linha de cada entrada é composta por um valor natural N1(1 < N1 < 1010),
    a segunda linha é composta por um valor N2( N1 < N2 < 1032).

    Saída
    Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição
    onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde
    é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe
    subsequencia". Mostre o resultado conforme o exemplo de saída.
    """
    n = 0
    while True:
        try:
            n1 = input()
            n2 = input()
        except EOFError:
            break
        else:
            qt = n2.count(n1)
            pos = n2.rfind(n1) + 1
            n += 1
            if qt >= 1:
                print(f'Caso #{n}:\n'
                      f'Qtd.Subsequencias: {qt}\n'
                      f'Pos: {pos}\n')
            else:
                print(f'Caso #{n}:\n'
                      f'Nao existe subsequencia\n')


if __name__ == '__main__':
    main()

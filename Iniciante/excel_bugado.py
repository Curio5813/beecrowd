def excel_bugado():
    """
    Esta função calcula e printa o número da coluna de uma planilha
    do excel, que vai de A -> 1, AA -> 27, até XFD. A entrada consiste
    em vários casos de teste. Cada caso de teste possuí uma linha com
    uma string S (1 ≤ |S| ≤  10) que contém a sequência de letras que
    identificam a coluna. É garantido que S possuí apenas letras maiúsculas
    ('A' - 'Z'). A entrada termina com EOF. Para cada caso de teste
    imprima um inteiro contendo o valor do índice numérico daquela coluna.
    Caso o código da coluna informado não esteja dentro dos limites do
    Excel, imprima “Essa coluna nao existe Tobias!” (sem aspas).
    :return:
    """
    while True:
        try:
            colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z"]
            s = input()
            if len(s) > 3:
                print("Essa coluna nao existe Tobias!")
            elif len(s) == 1:
                idx = colunas.index(s) + 1
                print(idx)
            elif len(s) == 2:
                idx = (colunas.index(s[0]) + 1) * 26 + (colunas.index(s[1]) + 1)
                print(idx)
            elif len(s) == 3:
                idx = (colunas.index(s[0]) + 1) * 26 * 26 + (colunas.index(s[1]) + 1) * 26 + (colunas.index(s[2]) + 1)
                if idx > 16384:
                    print("Essa coluna nao existe Tobias!")
                elif idx <= 16384:
                    print(idx)
        except EOFError:
            break


excel_bugado()

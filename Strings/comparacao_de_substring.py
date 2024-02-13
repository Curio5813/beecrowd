def comparacao_de_substring():
    """
    Encontre a maior substring comum entre as duas strings informadas.
    A substring pode ser qualquer parte da string, inclusive ela toda.
    Se não houver subseqüência comum, a saída deve ser “0”. A comparação
    é case sensitive ('x' != 'X').

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste é composto
    por duas linhas, cada uma contendo uma string. Ambas strings de entrada
    contém entre 1 e 50 caracteres ('A'-'Z','a'-'z' ou espaço ' '), inclusive,
    ou no mínimo uma letra ('A'-'Z','a'-'z').

    Saída
    O tamanho da maior subsequência comum entre as duas Strings.
    :return:
    """
    while True:
        try:
            tam, maior = 0, 0
            string1 = input()
            string2 = input()
            for i in range(0, len(string1)):
                for k in range(0, len(string2)):
                    if string1[i] == string2[k]:
                        a = i
                        b = k
                        while string1[a] == string2[b]:
                            if a >= len(string1) - 1 or b >= len(string2) - 1:
                                if len(string1) > 1 and len(string2) > 1 and string1[a] == string2[b]:
                                    tam += 1
                                    break
                                else:
                                    tam += 1
                                    break
                            tam += 1
                            a += 1
                            b += 1
                    if tam > maior:
                        maior = tam
                        tam = 0
                        break
                    else:
                        tam = 0
            print(maior)
        except EOFError:
            break


comparacao_de_substring()

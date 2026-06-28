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
            string1 = input()
            string2 = input()
            cont1, cont2, distaciancias = 0, 0, []
            for i in range(0, len(string1)):
                for j in range(cont1, len(string2)):
                    if string1[i] == string2[j]:
                        cont1 += 1
                        cont2 += 1
                        distaciancias.append(cont2)
                        print(string1[i], string2[j], distaciancias)
                        break
                    else:
                        cont1 += 1
                        cont2 = 0
                else:
                    cont1 = 0
            #print(string1)
            #print(string2)
            # print(distaciancias)
            if distaciancias:
                print(max(distaciancias))
            else:
                print(0)
        except EOFError:
            break


comparacao_de_substring()

"""
abcdef
cdofhij
TWO
FOUR
abracadabra
open
Hey This java is hot
Java is a new paradigm
Find the longest common substring
The substring can be any part of the String
If there is no common substring, return 0
The search is case sensitive
"""

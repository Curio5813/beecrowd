def main():
    """
    A cifra mais antiga conhecida é a Cifra de César. César escrevia suas cartas trocando
    cada letra pela próxima do alfabeto, para evitar que, quando a carta fosse interceptada,
    conseguissem ler. Com o tempo, a criptografia adquiriu melhor qualidade, mas a criptografia
    por substituição ainda é uma brincadeira de criança interessante, por exemplo:

                                            ZENIT
                                            POLAR

    Neste tipo de brincadeira, ao escrever uma carta a letra Z é trocada pela letra P e vice
    versa, bem como: E e O e assim sucessivamente. A frase cifrada desta forma: "Osro roxre
    osri caftide" pode ser decifrada como: "Este texto esta cifrado". Como a brincadeira ficou
    séria, a você foi solicitado um programa que decifre as mensagens cifradas a partir de
    uma chave fornecida.

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste começa com uma linha indicando
    dois números inteiros C e N, 0 < C < 21 e 0 < N < 100. C é o tamanho da cifra. Nas duas
    linhas seguintes está a cifra de tamanho C indicando quais caracteres da primeira linha
    será substituído por caracteres da segunda linha, um caracter aparece uma única vez,
    na primeira ou na segunda linha.

    A cifra pode conter letras de ‘A’ a ‘Z’, números de ‘0’ a ‘9’ além do espaço em branco
    e alguns símbolos de pontuação: '.' ',' ';' ':' '(' ')' '!' e '?'. Nas próximas N linhas
    estão frases e sentenças criptografadas pela cifra fornecida, que você deve decifrar.
    Cada linha contém no mínimo 1 e no máximo 1000 caracteres. São permitidos quaisquer
    caracteres ASCII (não extendido) imprimíveis, neste caso não estão presentes nenhum
    caracter acentuado, nem mesmo 'ç'.

    Saída
    Para cada caso de teste da entrada seu programa deve gerar para cada linha de frase e
    sentença de entrada, uma linha com a saída decifrada, respeitando a capitalização da
    letra (letras maiúsculas são decifradas como maiúsculas e minúsculas como minúsculas
    quando for possível aplicar a diferenciação, se não for possível serão decifrados como
    letras minúsculas). Após cada caso de teste deve ser impressa uma linha em branco,
    inclusive após o último.
    """
    while True:
        try:
            c, n = input().split()
            c, n = int(c), int(n)
            subs_x = input()
            subs_y = input()
            x = subs_x
            x = x.lower()
            y = subs_y
            y = y.lower()
            descifra = []
        except EOFError:
            break
        else:
            for k in range(n):
                p = ''
                cif = input()
                for i in range(0, len(cif)):
                    if cif[i] in '0123456789 .,;:()!?' and cif[i] in subs_y:
                        p += x[subs_y.index(cif[i])]
                    elif cif[i] in '0123456789 .,;:()!?' and cif[i] in subs_x:
                        p += y[subs_x.index(cif[i])]
                    elif cif[i] in subs_x:
                        p += subs_y[subs_x.index(cif[i])]
                    elif cif[i] in subs_y:
                        p += subs_x[subs_y.index(cif[i])]
                    elif cif[i] in x:
                        p += y[x.index(cif[i])]
                    elif cif[i] in y:
                        p += x[y.index(cif[i])]
                    else:
                        p += cif[i]
                descifra.append(p)
            for k in range(0, len(descifra)):
                print(descifra[k])
        print('')


if __name__ == '__main__':
    main()

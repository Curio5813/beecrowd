def ebcdic():
    """
    O EBCDIC (Extended Binary Coded Decimal Interchange Code) é um esquema
    de codificação de caracteres de 8 bits desenvolvido pela IBM nos anos 60.
    O EBCDIC tem origem nos esquemas de codificação dos cartões perfurados, e
    era utilizado nos mainframes da empresa. Apesar de utilizar um intervalo
    maior de codificação, o esquema é menos amigável ao programador do que o
    esquema ASCII de 7 bits, uma vez que as letras do alfabeto não ficam em
    posições contíguas.

    A tabela a seguir apresenta a codificação EBCDIC. Células em branco representam
    valores que não estão associados a um caractere em particular, e dois ou mais
    caracteres maiúsculos indicam caracteres não imprimíveis. O caractere BLANK é o
    espaço em branco.

    ![](https://resources.beecrowd.com/gallery/images/problems/UOJ_1832.png)

    Escreva um programa que receba um texto em codificação EBCDIC e o traduza para a
    codificação ASCII.

    Entrada
    A entrada consiste em vários casos de teste. Cada caso de teste é representado por uma
    única linha, que contém os valores de cada caractere EBCDIC, em números octais de três
    dígitos, separados por um espaço em branco.

    Pode-se considerar os códigos que aparecem nas mensagens correspondem apenas à caracteres
    alfanuméricos e espaços em branco.

    Saida
    Para cada linha da entrada a saída deve ser a mensagem decodificada para o padrão ASCII,
    seguida de uma quebra de linha.
    :return:
    """
    while True:
        try:
            entrada = list(input().strip().split(" "))
            decimal = []
            tabela = {
                240: '0', 241: '1', 242: '2', 243: '3', 244: '4',
                245: '5', 246: '6', 247: '7', 248: '8', 249: '9',
                193: 'A', 194: 'B', 195: 'C', 196: 'D', 197: 'E',
                198: 'F', 199: 'G', 200: 'H', 201: 'I',
                209: 'J', 210: 'K', 211: 'L', 212: 'M', 213: 'N',
                214: 'O', 215: 'P', 216: 'Q', 217: 'R',
                226: 'S', 227: 'T', 228: 'U', 229: 'V', 230: 'W',
                231: 'X', 232: 'Y', 233: 'Z',
                129: 'a', 130: 'b', 131: 'c', 132: 'd', 133: 'e',
                134: 'f', 135: 'g', 136: 'h', 137: 'i',
                145: 'j', 146: 'k', 147: 'l', 148: 'm', 149: 'n',
                150: 'o', 151: 'p', 152: 'q', 153: 'r',
                162: 's', 163: 't', 164: 'u', 165: 'v', 166: 'w',
                167: 'x', 168: 'y', 169: 'z', 64: ' '
            }
            for i in range(0, len(entrada)):
                decimal.append(int(entrada[i], 8))
            for i in range(0, len(decimal)):
                if i >= len(decimal) - 1:
                    print(tabela[decimal[i]])
                    break
                print(tabela[decimal[i]], end="")
        except EOFError:
            break


ebcdic()

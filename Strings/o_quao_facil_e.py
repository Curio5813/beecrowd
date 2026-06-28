from copy import deepcopy


def o_quao_facil_e():
    """
    TopCoder decidiu automatizar o processo de atribuição de níveis de
    dificuldade para os problemas. Os desenvolvedores do TopCoder concluíram
    que a dificuldade do problema esta relacionado apenas ao comprimento
    médio das palavras do enunciado do problema. Se o comprimento médio das
    palavras do enunciado é menor ou igual a 3, o problema recebe dificuldade
    de 250 pontos. Se o comprimento médio das palavras do enunciado for 4 ou 5,
    o problema recebe dificuldade de 500 pontos. Se o comprimento médio das palavras
    do enunciado for maior ou igual a 6, o problema recebe dificuldade de 1000 pontos.


    Definições:

    Símbolo: um conjunto de carateres ligados em ambos os lados por espaços, ou
    pelo início da descrição do problema, ou ainda pelo fim da descrição do problema.

    Palavra: um símbolo que contenha apenas letras a-z ou A-Z, e pode terminar com um
    único ponto.

    Comprimento da palavra: número de letras de uma palavra (um ponto não é uma letra).


    Exemplos de símbolos que são palavras (aspas duplas apenas para exemplificar): "AB", "ab".

    Exemplo de símbolos que não são palavras: "ab..", "a.b", ".ab", "a.b.", "a2b.", ".".


    O comprimento médio das palavras é dado pela soma dos tamanhos das palavras do enunciado
    dividido pelo numero de palavras, a divisão é feita por números inteiros. Se o número
    de palavras for zero, então o comprimento médio das palavras é zero.


    Sua tarefa é dado o enunciado do problema, computar a sua classificação de dificuldade
    do problema, que poderá ser 250, 500, ou 1000.

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste é composto por uma linha que
    contém o enunciado de um problema, é uma string que contém entre 1 e 50 caracteres
    ('A'-'Z', 'a'-'z', '0'-'9', ' ', '.'), inclusive. O final da entrada é determinado por EOF.

    Saída
    Compute o comprimento médio das palavras do enunciado do problema, e mostre a classificação
    do problema, para mais detalhes olhe o exemplo abaixo.
    :return:
    """
    while True:
        try:
            palavras = input().split()
            temp = []
            temp = deepcopy(palavras)
            i = 0
            for palavra in palavras:
                if palavra[0] == '.':
                    temp.remove(palavra)
                elif palavras[-2:] == '..':
                    temp.remove(palavra)
                elif palavras[0:] == '.':
                    temp = temp.replace(palavra, '')
                elif any(c in '0123456789.' for c in palavra[1:-1]):
                    temp.remove(palavra)
                while i < len(palavra) and palavra[i].isdigit():
                    i += 1
                i = 0
            # print(temp)
            palavras = deepcopy(temp)
            tamanhos = []
            if not palavras:
                print(250)
            else:
                for i in range(len(palavras)):
                    tamanho = len(palavras[i])
                    tamanhos.append(tamanho)
                # print(tamanhos)
                media = sum(tamanhos) // len(tamanhos)
                # print(media)
                if media == 0:
                    print(0)
                elif 0 < media <= 3:
                    print(250)
                elif 3 < media <= 5:
                    print(500)
                elif 5 < media:
                    print(1000)
        except EOFError:
            break


o_quao_facil_e()

"""
This is a problem statement
523hi.
Implement a class H5 which contains some method.
 no9 . wor7ds he8re. hj..
"""
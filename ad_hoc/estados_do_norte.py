def estados_do_norte():
    """
    Com extensão territorial igual 8,51 milhões km², o Brasil é o quinto maior
    país do planeta Terra. A sua região é, por sua vez, dividida em 5 regiões:
    Centro-Oeste, Nordeste, Norte, Sul e Sudeste.

    A região Norte tem extensão territorial igual a 3,85 milhões km², e abrange
    7 estados: Roraima, Acre, Amapá, Amazonas, Pará, Rondônia e Tocantins.

    Você está ajudando um amigo em um trabalho para a escola, e precisa escrever um
    algoritmo que: dado o nome de um estado brasileiro, diga se o mesmo pertence à
    região Norte do Brasil ou não.

    Entrada
    A entrada será composta por uma única linha contendo o nome de um estado brasileiro.
    Todas as letras estarão em minúsculo e sem acentuação.

    Saída
    Imprima a frase "Regiao Norte", caso o estado informado seja da região Norte, ou "Outra
    regiao" caso contrário.
    :return:
    """
    estados = ['roraima', 'acre', 'amapa', 'amazonas', 'para', 'rondonia', 'tocantins']
    estado = input().strip()
    flag = False
    for i in range(len(estados)):
        if estado in estados[i]:
            print("Regiao Norte")
            flag = True
            break
    if not flag:
        print("Outra regiao")


if __name__ == '__main__':
    estados_do_norte()

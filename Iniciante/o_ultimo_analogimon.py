def main():
    """
    Analógimôn Go! é um jogo bastante popular. Em sua jornada, o jogador percorre diversas
    cidades capturando pequenos monstrinhos virtuais, chamados analógimôns. Você acabou de
    chegar em uma cidade que contém o último analógimôn que falta para sua coleção!

    A cidade pode ser descrita como um grid de N linhas e M colunas. Você está em uma dada
    posição da cidade, enquanto o último analógimôn está em outra posição da mesma cidade.
    A cada segundo, você pode se mover (exatamente) uma posição ao norte, ao sul, a leste ou
    a oeste. Considerando que o analógimôn não se move, sua tarefa é determinar o menor tempo
    necessário para ir até a posição do monstrinho.

    A figura abaixo descreve o exemplo da entrada, e apresenta um caminho percorrido em 5
    segundos. Outros caminhos percorridos no mesmo tempo são possíveis, mas não há outro
    caminho que pode ser percorrido em um tempo menor.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de cada caso contém dois inteiros
    N e M (2 ≤ N, M ≤ 100), o número de linhas e de colunas na cidade, respectivamente. As
    próximas N linhas contém M inteiros cada, descrevendo a cidade. O inteiro 0 indica uma
    posição em branco; o inteiro 1 indica a sua posição na cidade; o inteiro 2 indica a
    posição do analógimôn na cidade. É garantido que haverá exatamente um inteiro 1 e
    exatamente um inteiro 2 na descrição da cidade, e que os demais inteiros serão iguais a 0.

    A entrada termina com fim-de-arquivo (EOF).

    Saída
    Para cada caso de teste, imprima uma linha contendo o menor tempo necessário para ir até o
    monstrinho, em segundos.
    """
    while True:
        c, city, d1, d2 = [], [], [], []
        try:
            n, m = input().split()
            n, m = int(n), int(m)
        except EOFError:
            break
        else:
            for k in range(n):
                a = [int(x) for x in input().split()]
                city.append(a)
            for k in range(0, len(city)):
                for i in range(0, len(city[k])):
                    if city[k][i] == 1:
                        d1.append(k)
                        d1.append(i)
                    if city[k][i] == 2:
                        d2.append(k)
                        d2.append(i)
            d_l = abs(d1[0] - d2[0])
            d_c = abs(d1[1] - d2[1])
            dist = d_l + d_c
            print(dist)


if __name__ == '__main__':
    main()

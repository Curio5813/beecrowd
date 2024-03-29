def main():
    """
    Após comprar vários sítios adjacentes na região do oeste catarinense, a família
    Estrela construiu uma única estrada que passa por todos os sítios em sequência.
    O primeiro sítio da sequência foi batizado de Estrela 1, o segundo de Estrela 2,
    e assim por diante. Porém, o irmão que vive em Estrela 1 acabou enlouquecendo e
    resolveu fazer uma Jornada nas Estrelas para roubar carneiros das propriedades de
    seus irmãos. Mas ele está definitivamente pirado. Quando passa pelo sítio Estrela i,
    ele rouba apenas um carneiro daquele sítio (se o sítio tem algum) e segue ou para
    Estrela i + 1 ou para Estrela i - 1, dependendo se o número de carneiros em Estrela
    i era, respectivamente, ímpar ou par. Se não existe a Estrela para a qual ele deseja
    seguir, ele interrompe sua jornada. O irmão louco começa sua Jornada em Estrela 1,
    roubando um carneiro do seu próprio sítio.

    Entrada
    A primeira linha da entrada consiste de um único inteiro N (1 ≤ N ≤ 106), o qual
    representa o número de Estrelas. A segunda linha da entrada consiste de N inteiros,
    de modo que o i-ésimo inteiro, Xi (1 ≤ Xi ≤ 106), representa o número inicial de
    carneiros em Estrela i.

    Saída
    Imprima uma linha contendo dois inteiros, de modo que o primeiro represente o número
    de Estrelas atacadas pelo irmão louco e o segundo represente o número total de
    carneiros não roubados.
    """
    i, estrelas = 1, {()}
    e = int(input())
    carneiros = [int(x) for x in input().split()]
    while 0 < i <= e:
        if carneiros[i - 1] % 2 != 0:
            if carneiros[i - 1] > 0:
                carneiros[i - 1] -= 1
                if i <= 0 or i > e:
                    break
                estrelas.add(i)
                i += 1
                if i <= 0 or i > e:
                    break
            elif carneiros[i - 1] == 0:
                i -= 1
                if i <= 0 or i > e:
                    break
                estrelas.add(i)
        elif carneiros[i - 1] % 2 == 0:
            if carneiros[i - 1] > 0:
                carneiros[i - 1] -= 1
                if i <= 0 or i > e:
                    break
                estrelas.add(i)
                i -= 1
                if i <= 0 or i > e:
                    break
            elif carneiros[i - 1] == 0:
                i -= 1
                if i <= 0 or i > e:
                    break
                estrelas.add(i)
    print(f'{len(estrelas) - 1} {sum(carneiros)}')


if __name__ == '__main__':
    main()

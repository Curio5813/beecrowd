def lucro():
    """
    George é dono de um circo e traz seu circo de cidade em cidade.
    Ele sabe o quanto de receita ele pode obter em qualquer dia de
    uma série de dias em uma cidade. Ele também sabe o custo constante
    diário para manter o seu circo. George quer trazer seu circo à cidade
    para a série de dias que resulta em maior lucro.

    Por exemplo, se em uma determinada cidade o custo for de $ 20 por dia
    em um exemplo com 6 dias, sendo que as receitas previstas por dia são
    {$ 18, $ 35, $ 6, $ 80, $ 15, $ 21}, George pode obter o máximo de lucro
    trazendo o seu circo para esta cidade do dia 2 ao dia 4. Desta forma
    ele pode lucrar (35 + 80 + 6) - (3 * 20) = $ 61.

    Nota: A série de dias que George traz seu circo para a cidade pode ser
    entre 0 e o número máximo de dias, inclusive. Obviamente, se George traz
    seu circo para a cidade por 0 dias, ele obtém $ 0 de lucro.

    Entrada
    A entrada contém muitos casos de teste. A primeira linha de cada caso de
    teste contém um inteiro N (1 ≤ N ≤ 50) que representa o número de dias
    que George pode trazer o seu circo para a cidade. A segunda linha do
    caso de teste contém um número inteiro custoPorDia (0 ≤ custoPorDia < 1000)
    que representa o custo em manter o circo na cidade. Segue N linhas (uma
    por cada dia), contendo cada um um inteiro receita (0 ≤ receita < 1000)
    representa a receita que o circo obtem em cada dia. O final da entrada é
    indicado por EOF (fim de arquivo).

    Saída
    Para cada caso de teste imprima o máximo de dinheiro que George pode ganhar
    trazendo o seu circo para a cidade de acordo com o exemplo abaixo.
    :return:
    """
    while True:
        try:
            dias = int(input())
            custo = int(input())
            receitas = []
            lucros, temp, maiores_lucros = 0, [], []
            for i in range(dias):
                receitas.append(int(input()))
            for i in range(0, len(receitas)):
                for j in range(i, len(receitas)):
                    lucros += (receitas[j] - custo)
                    temp.append(lucros)
                maiores_lucros.append(max(temp))
                temp = []
                lucros = 0
            if max(maiores_lucros) > 0:
                print(max(maiores_lucros))
            else:
                print(0)
        except EOFError:
            break


if __name__ == '__main__':
    lucro()

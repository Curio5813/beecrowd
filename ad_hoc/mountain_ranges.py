def mountain_ranges():
    """
    Famosa pelas suas cadeias de montanhas, a Nlogónia atrai milhões
    de turistas todos os anos. O governo dispõe de um orçamento dedicado
    à manutenção contínua dos percursos de pedestres espalhados por todo o
    país e a maioria deles está repleta de miradouros panorâmicos, acessíveis
    através de passadiços e escadas de madeira.

    Atualmente em viagem pela Nlogônia e com esperança de voltar para casa com
    muitas fotos de tirar o fôlego, Lola e seu marido querem visitar o maior
    número possível de mirantes. Eles planejam percorrer uma trilha diferente
    a cada dia e explorar seus mirantes. No entanto, para não ficarem exaustos
    no final do dia, se a passagem de um miradouro para outro necessitar de subir
    mais de X metros, basta encerrar o dia e regressar ao hotel para descansar
    um pouco. Felizmente, todas as trilhas para caminhadas na Nlogônia estão
    equipadas com teleféricos modernos, para que o casal possa começar a caminhar
    em qualquer ponto de vista que desejar. Uma vez iniciada a caminhada o casal
    só se desloca em direção ao pico da montanha.

    Para não perder um dia, Lola só quer caminhar por trilhas onde possa chegar a
    um número razoável de mirantes. Dadas as altitudes dos mirantes panorâmicos
    de um percurso pedestre, deve-se determinar o número máximo de mirantes que
    o casal pode visitar.

    Entrada
    A primeira linha contém dois inteiros N (1 ≤ N ≤ 1000) e X (0 ≤ X ≤ 8848),
    indicando respectivamente o número de mirantes panorâmicos na trilha e o
    número máximo de metros que Lola e seu marido estão dispostos a percorrer e
    subir de um ponto de vista para o outro. A segunda linha contém N inteiros
    A1, A2,. . . , AN (1 ≤ Ai ≤ 8848 para i = 1, 2, . . . , N ), onde Ai é a
    altitude (em metros) do i-ésimo ponto de vista. Os pontos de vista são dados
    na ordem em que aparecem na trilha e suas altitudes não são decrescentes,
    ou seja, Ai ≤ Ai+1 para i = 1, 2, . . . , N − 1.

    Saída
    Produza uma única linha com um número inteiro indicando o número máximo de
    mirantes panorâmicos que podem ser visitados sem subir mais de X metros de
    um mirante a outro, e considerando que a jornada pode ser iniciada em qualquer
    mirante.
    :return:
    """
    n, x = map(int, input().split(" "))
    mirantes = list(map(int, input().split(" ")))
    cont, maior = 1, 0
    for i in range(0, len(mirantes)):
        if i >= len(mirantes) - 1:
            break
        if mirantes[i + 1] - mirantes[i] <= x:
            cont += 1
            if cont > maior:
                maior = cont
        else:
            cont = 1
    if maior == 0:
        print(1)
    else:
        print(maior)


mountain_ranges()

def presentes_de_natal():
    """
    Esta função calcula e printa o valor total do valor dos
    pares de presentes mais caros e o valor do pares de presentes
    mais baratos, buscando minimizar a diferença de valor
    entre eles. A entrada consiste em vários casos de teste.
    A primeira linha de um caso de teste possui um inteiro
    n (1 ≤ n ≤ 104), a quantidade de netos. A segunda linha
    possui 2n inteiros xi (1 ≤ xi ≤ 108, em que 1 ≤ i ≤ 2n)
    em ordem decrescente e separados por exatamente um espaço
    em branco. Cada inteiro xi representa o valor do i-ésimo
    presente comprado por Dona Ricota. A primeira linha do último
    caso de teste contém n = 0 e não deve ser processada. A saída
    para cada caso de teste deve imprimir uma linha com o preço
    total do par de presentes mais caro e o preço total do par
    de presentes mais barato separados por um espaço em branco.
    :return:
    """
    while True:
        n = int(input())
        if n == 0:
            break
        presentes, maior, menor, idx = [], 0, 100_000_001, 1
        presentes = list(map(int, input().split(" ")))
        for i in range(0, len(presentes)):
            aux = presentes[i] + presentes[len(presentes) - idx]
            idx += 1
            if aux < menor:
                menor = aux
            if aux > maior:
                maior = aux
        print(f"{maior} {menor}")


presentes_de_natal()

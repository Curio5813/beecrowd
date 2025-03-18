def obras_da_china():
    """
    Devido à abertura econômica ocorrida na China nos últimos anos,
    boa parte do país foi transformada em canteiro de obras. Algumas
    construções em curso são tão monumentais que, juntamente com a já
    famosa Muralha da China, poderão ser vistas da lua a olho nu.

    Uma empreiteira radicada em Shangai é responsável pela execução de
    várias obras no país. Após algum tempo, os engenheiros da empreiteira
    perceberam que, a cada nova obra, tinham de resolver um problema semelhante
    ao que já tinham resolvido no início das obras anteriores. Cansados
    de realizar sempre os mesmos tipos de cálculos, pediram a sua ajuda
    na construção de um programa que resolvesse o problema deles, descrito a
    seguir.

    Considere uma obra que tem duração de n semanas. Na i-ésima semana da obra,
    para i ≤ 1 ≤ n, são necessários fi funcionários para executá-la. Os custos
    com recrutamento e instrução de um funcionário são de x yuan. Gasta-se y yuan
    para demitir um funcionário. Um funcionário necessário custa z yuan por semana
    e cada funcionário excedente, isto é, cada funcionário contratado que não é
    necessário em uma semana da obra, custa w yuan por semana para a empreiteira.
    (yuan é a moeda chinesa.) Funcionários podem ser contratados e demitidos a
    cada semana. Inicialmente, a obra não possui nenhum funcionário. Ao final da
    mesma, todos os funcionários devem ser demitidos. O problema consiste em determinar
    o menor valor possível que a empreiteira deve gastar com funcionários ao longo
    da obra, satisfazendo sempre as restrições semanais. Ou seja, não pode haver
    menos de fi funcionários trabalhando na obra na i-ésima semana.

    Entrada
    Seu programa deve estar preparado para trabalhar com diversas obras, doravante
    denominadas instâncias. Cada instância tem a estrutura que segue.

    Na primeira linha é fornecido um inteiro n (0 ≤ n ≤ 200) que representa o número de
    semanas de duração da obra.

    Na próxima linha são dados, separados por espaços em branco, n valores inteiros não
    negativos e menores ou iguais a 50, em que o i-ésimo valor (1 ≤ i ≤ n) representa o
    número fi de funcionários necessários na i-ésima semana.

    Na linha seguinte, também separados por espaços em branco, são fornecidos quatro inteiros
    x, y, z e w (0 ≤ x, y, z, w ≤ 1000), em que x é o custo de recrutamento e instrução de
    um funcionário novo, y é o custo de demitir um funcionário empregado, z é o custo
    semanal de um funcionário necessário e w é o custo para manter um funcionário excedente,
    por uma semana, na obra.

    Um valor n = 0 indica o final das instâncias e não deve ser processado.

    Saída
    Para cada instância solucionada, você deverá imprimir um identificador “Instancia h” em
    que h é um número inteiro, sequencial e crescente a partir de 1. Na linha seguinte, você
    deve imprimir o menor valor possível que a empreiteira deve gastar com funcionários ao
    longo dessa obra.

    Uma linha em branco deve separar a saída de cada instância.
    :return:
    """
    n, cont = 1, 0
    while n != 0:
        n = int(input())
        if n == 0:
            break
        func = list(map(int, (input().split(" "))))
        custo = list(map(int, input().split(" ")))
        total1, total2, demissao, admissao = 0, 0, 0, 0
        for i in range(0, len(func)):
            if i == 0:
                total1 += func[i] * custo[0] + func[i] * custo[1] + func[i] * custo[2]
            if i > 0:
                if func[i - 1] > func[i]:
                    manter = func[i - 1] - func[i]
                    total1 += (func[i] + manter) * custo[2] + manter * custo[3]
                if func[i - 1] < func[i]:
                    admissao = func[i] - func[i - 1]
                    total1 += admissao * custo[0] + func[i] * custo[2]
        for i in range(0, len(func)):
            if i == 0:
                total2 += func[i] * custo[0] + func[i] * custo[1] + func[i] * custo[2]
            if i > 0:
                if func[i - 1] > func[i]:
                    demissao = func[i - 1] - func[i]
                    total2 += demissao * custo[1] + func[i] * custo[2]
                if func[i - 1] < func[i]:
                    admissao = func[i] - func[i - 1]
                    total2 += admissao * custo[0] + func[i] * custo[2]
        cont += 1
        print(f"Instancia {cont}")
        if total1 < total2:
            print(total1)
        elif total2 <= total1:
            print(total2)


obras_da_china()

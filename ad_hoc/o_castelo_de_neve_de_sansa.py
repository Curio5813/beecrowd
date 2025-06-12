def o_castelo_de_neve_de_sansa():
    """
    Robin: "O que você está fazendo?"
    Sansa: "Estou construindo minha casa, Winterfell."

    Sansa está construindo um castelo de neve no jardim do Ninho da Águia.
    O castelo de neve é feito para parecer com o verdadeiro castelo de
    Winterfell.

    O castelo de neve pode ser descrito como uma sequência de N torres de
    neve, numeradas de 1 a N da esquerda para a direita. A altura da torre i
    (1 ≤ i ≤ N) é igual a hi centímetros.

    Sansa diz que o castelo é bonito se ele consiste em uma sequência de K "picos"
    alternados com K-1 "vales", como o castelo de Winterfell. Em outras palavras,
    o castelo é bonito se existe uma sequência de K torres T1 < T2 < ... < TK tal que:

    As alturas das torres no intervalo [1, T1] estão em ordem crescente;
    Existe um "vale" no intervalo [Ti, Ti+1], para todo 1 ≤ i < K;
    As alturas das torres no intervalo [TK, N] estão em ordem decrescente.
    Existe um "vale" em um intervalo [A, B] se B ≥ A+2 e existe alguma torre J, A ≤ J ≤ B,
    tal que as alturas das torres no intervalo [A,J] estão em ordem decrescente, e as
     alturas das torres no intervalo [J,B] estão em ordem crescente.

    Ajude Sansa a determinar se seu castelo é bonito ou não!

    Entrada
    A primeira linha contém dois inteiros N e K (1 ≤ N ≤ 1000, 1 ≤ K ≤ N). A segunda linha
    contém N inteiros h1, h2, ..., hN (1 ≤ hi ≤ 100), as alturas das torres, em centímetros.
    A primeira e a última torre sempre terão 1 centímetro de altura. Duas torres consecutivas
    nunca terão a mesma altura.

    Saída
    Imprima uma linha contendo a palavra beautiful se o castelo dado é bonito, ou a palavra ugly
    caso contrário.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, k = entrada[0], entrada[1]
    castelo = list(map(int, input().strip().split(" ")))
    const, flag = k, 0
    for i in range(0, len(castelo)):
        if i >= len(castelo) - 2:
            if castelo[i] < castelo[i + 1] and i != (k - 1):
                flag = 1
                break
            if castelo[i] > castelo[i + 1] and i == (k - 1):
                flag = 1
                break
            else:
                flag = 0
                break
        if castelo[i] < castelo[i + 1] and i < (k - 1):
            print("Ok0", k - 1)
            flag = 1
        if i == (k - 1) and castelo[i] > castelo[i + 1]:
            print("Ok1", k - 1)
            flag = 1
            k += const
            print(k)
    if flag == 1:
        print("beautiful")
    elif flag == 0:
        print("ugly")


o_castelo_de_neve_de_sansa()


"""
9 3
1 2 3 2 4 3 1 2 1
5 3
1 2 1 2 1
"""

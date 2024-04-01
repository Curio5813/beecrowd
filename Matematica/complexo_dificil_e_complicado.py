def complexo_dificil_e_complicado():
    """
    Números complexos não são apenas complexos, mas também complicados.
    Então é melhor tentar resolver outro problema...

    Nós temos um números complexo, a+b*i, onde i é a raiz quadrada de -1.
    Nós queremos torná-lo simples (isto é, real), elevando-o a uma potência
    natural. Por exemplo, o número complexo 2+2*i, pode ser simplificado
    elevando-o a 4:

    (2+2*i)4 = -64

    Você tem que computar o menor número natural, N, (zero não está incluso)
    tal que (a+b*i)N é um número real. Além disso, pedimos que o valor absoluto
    de (a+b*i)N não seja maior que 2^30.

    Entrada
    A primeira linha da entrada contém um inteiro M, indicando o número de casos
    de teste.

    Para cada caso de teste, há uma linha com dois inteiros A e B. A é a parte real
    do número complexo, e B a parte imaginária.

    Você pode assumir que -10000 ≤ A ≤ 10000, e -10000 ≤ B ≤ 10000.

    Saída
    Para cada caso de teste, a saída deve consistir de um único número natural N em
    uma linha, indicando a potência tal que (A+B*i)N é real e seu valor absoluto não
    é maior que 2^30. Se não houver solução imprima "TOO COMPLICATED".
    :return:
    """
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split(" "))
        z = complex(a + b*1j)
        for k in range(1, 31):
            num = z ** k
            if num.imag == 0j:
                print(k)
                break
        else:
            print("TOO COMPLICATED")


complexo_dificil_e_complicado()

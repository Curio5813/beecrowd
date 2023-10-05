def o_retorno_do_rei():
    """
    Esta função calcula a quantidade de runas que
    devem ser utilizadas para derrotar Gollum. Essa
    quantidade deve ser igual ao valor necessária para
    derrotar Gollum. A entrada a primeira linha é composta 
    por dois inteiros N(1 <= N) e G(G <= 100), indicando, 
    respectivamente, a quantidade de runas existentes, e 
    a quantidade de amizade necessária para derrotar Gollum. 
    As próximas N linhas são compostas por um caractere 
    Ri('A' <= Ri <= 'Z') e um inteiro Vi(-100 <= Vi <= 100), 
    indicando, respectivamente, a runa e o valor de amizade 
    que ela agrega. A próxima linha é iniciada por um inteiro X, 
    indicando a quantidade de runas recitadas por Frodo e Sam. 
    A última linha da entrada é composta por X caracteres, 
    indicando as runas recitadas por Frodo e Sam. A saída a primeira 
    linha da saída deve conter a quantidade de valor de amizade. 
    A segunda linha deve conter uma das seguintes mensagens:
    “My precioooous”, se Gollum vencer; “You shall pass!”, se Frodo 
    e Sam vencerem.
    :return:
    """
    n, g = map(int, input().split(" "))
    runa, valores, soma = [], [], 0
    for i in range(n):
        r, v = input().split(" ")
        v = int(v)
        runa.append(r)
        valores.append(v)
    x = int(input())
    runas = input().split(" ")
    for i in runas:
        if i not in runa:
            runa.append(i)
            valores.append(0)
    for i in range(0, len(runas)):
        soma += valores[runa.index(runas[i])]
    if soma >= g:
        print(soma)
        print("You shall pass!")
    else:
        print(soma)
        print("My precioooous")


o_retorno_do_rei()

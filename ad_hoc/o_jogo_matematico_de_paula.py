def o_jogo_matematico_de_paula():
    """
    Paula simplesmente adora matemática. Seu maior passatempo
    é ficar inventando jogos ou atividades que a envolvam para
    brincar com seus amiguinhos. Obviamente, nem todos eles não
    são tão apaixonados assim por matemática e têm muita dificuldade
    para resolver as brincadeiras propostas por ela. Agora Paula
    inventou um pequeno passatempo que envolve 3 caracteres: um
    dígito numérico, uma letra e outro dígito numérico.

    Se a letra for maiúscula, deve-se subtrair o primeiro dígito do
    segundo. Se a letra for minúscula, deve-se somar ambos os dígitos
    e se os DÍGITOS forem iguais, deve-se desconsiderar a letra e mostrar
    o produto entre os dois dígitos. Ela pediu para seu amigo Marcelo,
    que é bom em programação, para criar um programa para que encontre a
    solução para cada uma das sequências que Paula lhe apresentar.

    Entrada
    A entrada contém vários casos de teste. A primeira linha da entrada
    contém um inteiro N, indicando o número de casos de teste que virão
    a seguir. Cada caso de teste é uma sequência de três caracteres criada
    por Paula. Esta sequência contém na primeira posição um caractere de '0'
    a '9', na segunda posição uma letra maiúscula ou minúscula do alfabeto
    e na terceira posição outro caractere de '0' a '9'.

    Saída
    Para cada caso de teste, deve ser impressa uma linha com um valor inteiro
    que representa a solução da sequência proposta por Paula.
    :return:
    """
    n = int(input())
    for i in range(n):
        seq = input()
        if seq[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and seq[0] != seq[2]:
            res = int(seq[2]) - int(seq[0])
            print(res)
        elif seq[1] in "abcdefghijklmnopqrstuvwxyz" and seq[0] != seq[2]:
            res = int(seq[0]) + int(seq[2])
            print(res)
        elif seq[0] == seq[2]:
            res = int(seq[0]) * int(seq[2])
            print(res)


o_jogo_matematico_de_paula()

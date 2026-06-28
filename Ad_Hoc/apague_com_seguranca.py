def apague_com_seguranca():
    """
    Jon Marius é o especialista em computadores em sua empresa e
    agora foi encarregado de encontrar um software para apagar
    dados corretamente. É muito importante que os dados não sejam
    recuperáveis posteriormente, portanto, eles devem ser sobrescritos
    no disco rígido várias vezes. Incapaz de encontrar um programa
    gratuito para a tarefa, Jon Marius decide escrever tal programa
    sozinho. A interface do usuário é simples, pede apenas que o arquivo
    seja destruído e N, o número de vezes que ele deve ser sobrescrito.
    Esse número pode variar de 1 (exclusão rápida) a 20 (segurança máxima).
    Jon Marius processa o arquivo bit a bit e não considera escrever um
    zero onde já havia um zero como realmente sobrescrever. Portanto, para
    cada uma das N varreduras, ele sobrescreve cada zero com um e cada
    um com um zero.

    Jon Marius sabe que o teste independente é importante, então ele pediu
    que você escrevesse a rotina de verificação. Ele não ouvirá suas
    objeções ao algoritmo, então, eventualmente, você cede.

    Entrada
    A primeira linha da entrada contém um único inteiro 1 ≤ N ≤ 20. As duas
    linhas seguintes contêm, cada uma, uma string contendo apenas os caracteres
    0 e 1. A primeira dessas linhas representa os bits do arquivo antes da
    exclusão e a segunda os bits na mesma posição no disco rígido após o arquivo
    ser excluído. O comprimento dessas strings é o mesmo e tem entre 1 e 1 000
    caracteres.

    Saída
    Emita uma única linha contendo as palavras “Deletion succeeded” se cada bit for
    trocado N vezes ou “Deletion failed” se este não for o caso.
    :return:
    """
    n = int(input())
    antes = input()
    depois = input()
    flag = 0
    for i in range(0, len(antes)):
        if antes[i] == "1" and depois[i] == "1" and n % 2 == 1:
            print("Deletion failed")
            flag = 1
            break
        if antes[i] == "1" and depois[i] == "0" and n % 2 == 0:
            print("Deletion failed")
            flag = 1
            break
        if antes[i] == "0" and depois[i] == "0" and n % 2 == 1:
            print("Deletion failed")
            flag = 1
            break
        if antes[i] == "0" and depois[i] == "1" and n % 2 == 0:
            print("Deletion failed")
            flag = 1
            break
    if flag == 0:
        print("Deletion succeeded")


apague_com_seguranca()

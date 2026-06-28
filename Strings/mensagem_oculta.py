def mensagem_oculta():
    """
    Textos podem conter mensagens ocultas. Neste problema a mensagem oculta em
    um texto é composto pelas primeiras letras de cada palavra do texto, na ordem
    em que aparecem.

    É dado um texto composto apenas por letras minúsculas ou espaços. Pode haver
    mais de um espaço entre as palavras. O texto pode iniciar ou terminar em espaços,
    ou mesmo conter somente espaços.

    Entrada
    A entrada contém vários casos de testes. A primeira linha de entrada contém um inteiro
    N que indica a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste
    de uma única linha contendo de um a 50 caracteres, formado por letras minúsculas
    (‘a’-‘z’) ou espaços (‘ ’). Atenção para possíveis espaços no início ou no final do texto!

    Nota: No exemplo de entrada os espaços foram substituídos por pequenos pontos (‘·’) para
    facilitar o entendimento dos exemplos.

    Saída
    Para cada caso de teste imprima a mensagem oculta no texto de entrada.
    :return:
    """
    n = int(input())
    oculta = ""
    for i in range(n):
        mensagem = input().split(' ')
        for j in range(0, len(mensagem)):
            for k in range(0, len(mensagem[j])):
                if mensagem[j][k] in 'abcdefghijklmnopqrstuvwxyz':
                    oculta += mensagem[j][0]
                    break
        print(oculta)
        oculta = ""


mensagem_oculta()

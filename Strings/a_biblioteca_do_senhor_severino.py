def a_biblioteca_do_senhor_severino():
    """
    Em uma pacata cidade do interior, o senhor Severino
    decidiu montar a própria biblioteca, já que coleciona
    vários livros desde sua juventude. Como ele não sabe
    programar, pediu ajuda ao neto para criar um programa
    que cadastre e ordene seus livros pelo código. Porém,
    seu neto ainda está no ensino fundamental, e como sabe
    muito pouco de programação, acabou criando um programa
    que somente cadastra os livros, mas não os ordena.

    Desse modo, o senhor Severino recorreu a você, pois sabe
    de suas habilidades com programação. Sua tarefa é simples:
    ordenar os cadastros dos códigos dos livros.

    Entrada
    A entrada contém vários casos de teste. Cada teste começa com
    um valor N (1 ≤ N ≤ 1000). Em seguida, N linhas terão os códigos
    dos livros, que estão sempre no formato "xxxx", isto é, não haverá
    o cadastro '1', por exemplo, mas "0001". A entrada termina com
    fim de arquivo.

    Saída
    Seu programa deverá imprimir o cadastro dos códigos ordenado. Não
    haverá linha em branco entre os casos de teste.
    :return:
    """
    while True:
        try:
            n = int(input())
            biblioteca = []
            for i in range(n):
                cadastro = input()
                biblioteca.append(cadastro)
            biblioteca.sort()
            for i in range(0, len(biblioteca)):
                print(biblioteca[i])
        except EOFError:
            break


a_biblioteca_do_senhor_severino()

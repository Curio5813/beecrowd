def dijkstra():
    """
    Esta função retorna numero inteiro que é igual
    a soma de todas ‘strings’ diferentes contidos
    numa lista. Essas ‘strings’ contém apenas os
    caracteres "(" e ")". O programa termina com
    o EOF error.
    """
    l1 = []
    while True:
        try:
            joias = input()
            if joias in l1:
                continue
            else:
                l1.append(joias)
        except EOFError:
            return print(len(l1))


dijkstra()

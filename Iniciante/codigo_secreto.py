def codigo_secreto():
    while True:
        try:
            """
            Esta função retorna a frase contida no codigo secreto
            formados por pontos e espaços.
            """
            l1 = ['.', '..', '...', '. .', '.. ..', '... ...', '. . .', '.. .. ..', '... ... ...',
                  '. . . .', '.. .. .. ..', '... ... ... ...', '. . . . .', '.. .. .. .. ..', '... ... ... ... ...',
                  '. . . . . .', '.. .. .. .. .. ..', '... ... ... ... ... ...', '. . . . . . .', '.. .. .. .. .. .. ..',
                  '... ... ... ... ... ... ...', '. . . . . . . .', '.. .. .. .. .. .. .. ..',
                  '... ... ... ... ... ... ... ...', '. . . . . . . . .', '.. .. .. .. .. .. .. .. ..',
                  '... ... ... ... ... ... ... ... ...']
            l2, l3 = [], []
            for j in "abcdefghijklmnopqrstuvwxyz":
                l2.append(j)
            n = int(input())
            for m in range(n):
                dot = input()
                h = l1.index(dot)
                l3.append(l2[h])
            for o in range(0, len(l3)):
                print(l3[o])
        except EOFError:
            break


codigo_secreto()

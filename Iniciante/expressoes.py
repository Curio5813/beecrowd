def expressoes():
    """
    Esta função printa um valor "S" para sim ou "N" para não
    se as expressões com colchetes, parenteses e chaves abrem
    e fecham corretamente.
    """
    l1 = []
    t = int(input())
    for k in range(t):
        expressao = input()
        for i in expressao:
            ch = i
            if ch == '{' or ch == '[' or ch == '(':
                # Preenchendo a pilha
                l1.append(ch)
            elif ch == '}' or ch == ']' or ch == ')':
                if len(l1) != 0:
                    # Desempilhando a pilha
                    chx = l1.pop()
                    if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
                        # Forçar erro
                        l1.append(chx)
                        break
                elif len(l1) == 0:
                    if ch == '}' or ch == ']' or ')':
                        # Forçar erro
                        l1.append(ch)
                        break
        if len(l1) != 0:
            print("N")
        elif len(l1) == 0:
            print("S")
        l1 = []


expressoes()

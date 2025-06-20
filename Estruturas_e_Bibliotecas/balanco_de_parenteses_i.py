def balanco_de_parenteses_i():
    """
    Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses
    está correta ou não, sem levar em conta o restante da expressão. Por exemplo:

    a+(b*c)-2-a        está correto
    (a+b*(2-c)-2+a)*2  está correto

    enquanto

    (a*b-(2+c)         está incorreto
    2*(3-a))           está incorreto
    )3+b*(2-c)(        está incorreto

    Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e
    não pode haver parênteses que fecha sem um previo parenteses que abre e a quantidade total
    de parenteses que abre e fecha deve ser igual.

    Entrada
    Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

    Saída
    O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada,
    cada uma delas contendo as palavras correct ou incorrect de acordo com as regras acima
    fornecidas.
    :return:
    """
    while True:
        try:
            pilha = []
            expressao = input()
            flag = 1
            for j in expressao:
                if j == ")" and len(pilha) == 0:
                    print("incorrect")
                    flag = 0
                    break
                if j == "(":
                    pilha.append(j)
                elif j == ")" and pilha[-1] == "(":
                    pilha.pop()
            if len(pilha) > 0:
                print("incorrect")
            if flag == 1 and len(pilha) == 0:
                print("correct")
        except EOFError:
            break


balanco_de_parenteses_i()

"""
a+(b*c)-2-a 
(a+b*(2-c)-2+a)*2 
(a*b-(2+c) 
2*(3-a))  
)3+b*(2-c)( 
"""

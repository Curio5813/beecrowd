def fibonacci_quantas_chamadas():
    """
    Quase todo estudante de Ciência da Computação recebe em algum momento no início
    de seu curso de graduação algum problema envolvendo a sequência de Fibonacci.
    Tal sequência tem como os dois primeiros valores 0 (zero) e 1 (um) e cada próximo
    valor será sempre a soma dos dois valores imediatamente anteriores. Por definição,
    podemos apresentar a seguinte fórmula para encontrar qualquer número da sequência de
    Fibonacci:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2);

    Uma das formas de encontrar o número de Fibonacci é através de chamadas recursivas.
    Isto é ilustrado a seguir, apresentando a árvore de derivação ao calcularmos o valor
    fib(4), ou seja o 5º valor desta sequência:

    [imagem]!(https://resources.beecrowd.com/gallery/images/problems/UOJ_1029.png)

    Desta forma,
    fib(4) = 1+0+1+1+0 = 3
    Foram feitas 8 calls, ou seja, 8 chamadas recursivas.
    Entrada
    A primeira linha da entrada contém um único inteiro N, indicando o número de casos
    de teste. Cada caso de teste contém um inteiro X (1 ≤ X ≤ 39) .

    Saída
    Para cada caso de teste de entrada deverá ser apresentada uma linha de saída, no seguinte
    formato: fib(n) = num_calls calls = result, aonde num_calls é o número de chamadas
    recursivas, tendo sempre um espaço antes e depois do sinal de igualdade.
    :return:
    """
    n = int(input())
    for i in range(n):
        a, b, p = 0, 1, 1
        chamadas = 0
        termos = 0
        x = int(input())
        if x == 1:
            print(f"fib({x}) = {chamadas} calls = {1}")
        else:
            while termos < x:
                a = b
                b = p
                p = a + b
                chamadas = p
                termos += 1
            print(f"fib({x}) = {chamadas + (b - a) - 2} calls = {a}")


fibonacci_quantas_chamadas()

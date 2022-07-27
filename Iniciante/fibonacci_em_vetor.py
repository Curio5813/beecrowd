def main():
    """
    Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor
    lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é
    a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber
    em um inteiro de 64 bits sem sinal.
    """
    vetor = []
    a, b = 0, 1
    for k in range(0, 61):
        vetor.append(a)
        a, b, = b, a + b
    t = int(input())
    for k in range(0, t):
        n = int(input())
        print(f'Fib({n}) = {vetor[n]}')


if __name__ == '__main__':
    main()

def main():
    from math import log
    """
    Schoenfeld e Rosser publicaram em 1962 um artigo descrevendo um valor mínimo
    e máximo para a quantidade de números primos até n, para n ≥ 17. Esta quantidade
    é representada pela função (n) e a fórmula é mostrada abaixo.

                n / ln(n) < pi(n) < 1.25506 (n/ ln(n))

    Sua tarefa é, dado um natural n, calcular o mínimo e máximo do intervalo para
    o número aproximado de primos até n.

    Entrada
    A entrada é um número natural n (17 ≤ n ≤ 109).

    Saída
    A saída são dois valores P e M com 1 casa decimal cada, tal que P < (n) < M,
    de acordo com a fórmula dada acima. Os valores devem ser separados por um espaço
    em branco.
    """
    n = int(input())
    p = n / log(n)
    m = 1.25506 * (n / log(n))
    print(f'{p:.1f} {m:.1f}')


if __name__ == '__main__':
    main()

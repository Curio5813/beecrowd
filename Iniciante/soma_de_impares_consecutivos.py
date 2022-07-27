def main(x=int(input()), y=int(input())):
    """
    A função retorna a soma dos números ímpares estipulado pelos dois intervalos
    fornecidos pelo usuário, sendo esses intervalos exclusive da soma.
    """
    if y <= x:
        impares = [k for k in range(y, x) if k > y and k % 2 != 0]
        return f'{sum(impares)}'
    elif x <= y:
        impares = [k for k in range(x, y) if k > x and k % 2 != 0]
        return f'{sum(impares)}'


if __name__ == '__main__':
    print(main())


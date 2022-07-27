def main():
    """
    Dados três valores, verifique se os três podem formar um triângulo. Em caso
    afirmativo, verifique se ele é escaleno, isóceles ou equilátero e se trata-se
    de um triângulo retângulo ou não.

    Entrada
    A entrada consiste em três números inteiros A,B e C (0 < A,B,C < 105).

    Saída
    A saída deve conter a string "Invalido" se os valores lidos não formarem um
    triângulo. Se os valores formarem um triângulo a saída deve ser "Valido-Equilatero",
    "Valido-Escaleno" ou "Valido-Isoceles" de acordo com a característica do triângulo
    seguido de "Retangulo: S" se o triângulo for retângulo ou "Retangulo: N" se não for,
    conforme os exemplos.
    """
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            print('Valido-Equilatero\n'
                  'Retangulo: N')
        elif a != b and a != c and b != c:
            if a > b and a > c and a ** 2 == b ** 2 + c ** 2:
                print('Valido-Escaleno\n'
                      'Retangulo: S')
            elif b > a and b > c and b ** 2 == a ** 2 + c ** 2:
                print('Valido-Escaleno\n'
                      'Retangulo: S')
            elif c > a and c > b and c ** 2 == a ** 2 + b ** 2:
                print('Valido-Escaleno\n'
                      'Retangulo: S')
            else:
                print('Valido-Escaleno\n'
                      'Retangulo: N')
        else:
            if a > b and a > c and a ** 2 == b ** 2 + c ** 2:
                print('Valido-Isoceles\n'
                      'Retangulo: S')
            elif b > a and b > c and b ** 2 == a ** 2 + c ** 2:
                print('Valido-Isoceles\n'
                      'Retangulo: S')
            elif c > a and c > b and c ** 2 == a ** 2 + b ** 2:
                print('Valido-Isoceles\n'
                      'Retangulo: S')
            else:
                print('Valido-Isoceles\n'
                      'Retangulo: N')
    else:
        print('Invalido')


if __name__ == '__main__':
    main()

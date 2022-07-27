def main():
    cont1, cont2, cont3, cont4 = 0, 0, 0, 0
    for k in range(0, 5):
        num = int(input())
        if num % 2 == 0:
            cont1 += 1
        if num % 2 == 1:
            cont2 += 1
        if num > 0:
            cont3 += 1
        if num < 0:
            cont4 += 1
    print(f'{cont1} valor(es) par(es)\n'
          f'{cont2} valor(es) impar(es)\n'
          f'{cont3} valor(es) positivo(s)\n'
          f'{cont4} valor(es) negativo(s)')


if __name__ == '__main__':
    main()

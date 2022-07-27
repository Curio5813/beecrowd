def main():
    from statistics import mean
    positivos = []
    for k in range(1, 7):
        num = round(float(input()), 1)
        if num > 0:
            positivos.append(num)
    print(f'{len(positivos)} valores positivos\n'
          f'{mean(positivos):.1f}')


if __name__ == '__main__':
    main()

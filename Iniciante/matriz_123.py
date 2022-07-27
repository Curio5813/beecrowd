def main():
    """
    Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.
    """
    while True:
        matriz = []
        try:
            n = int(input())
        except EOFError:
            break
        else:
            for k in range(n):
                if k == 0:
                    matriz.append(1)
                elif k == n - 1:
                    matriz.append(2)
                else:
                    matriz.append(3)
            for k in range(0, len(matriz)):
                if len(matriz) % 2 == 0:
                    if k == 0:
                        print(f'{matriz}'.replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))
                    elif k > 0:
                        matriz[k - 1], matriz[k] = matriz[k], matriz[k - 1]
                        matriz[-k], matriz[-k - 1] = matriz[-k - 1], matriz[-k]
                        print(f'{matriz}'.replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))
                    if k == int((len(matriz) / 2) - 1):
                        matriz.reverse()
                if len(matriz) % 2 == 1:
                    if k >= len(matriz) - 1:
                        break
                    if k == 0:
                        print(f'{matriz}'.replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))
                    elif 0 < k < int(len(matriz) / 2):
                        matriz[k - 1], matriz[k] = matriz[k], matriz[k - 1]
                        matriz[-k], matriz[-k - 1] = matriz[-k - 1], matriz[-k]
                        print(f'{matriz}'.replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))
                    if k == int(len(matriz) / 2):
                        matriz[k - 1] = 3
                        matriz[k + 1] = 3
                        matriz[k] = 2
                        print(f'{matriz}'.replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))
                    if k == int(len(matriz) / 2):
                        matriz[k - 1] = 2
                        matriz[k + 1] = 1
                        matriz[k] = 3
                        print(f'{matriz}'.replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))
                    elif k > int(len(matriz) / 2):
                        matriz[k], matriz[k + 1] = matriz[k + 1], matriz[k]
                        matriz[-k - 1], matriz[-k - 2] = matriz[-k - 2], matriz[-k - 1]
                        print(f'{matriz}'.replace(' ', '').replace('[', '').replace(']', '').replace(',', ''))


if __name__ == '__main__':
    main()

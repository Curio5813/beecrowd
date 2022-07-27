def main():
    """
    Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo
    elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.
    """
    vetor = []
    x = int(input())
    vetor.append(x)
    while len(vetor) < 20:
        x = int(input())
        vetor.append(x)
    for k in range(0, 10):
        vetor[k], vetor[19 - k] = vetor[19 - k], vetor[k]
    for k in range(0, len(vetor)):
        print(f'N[{k}] = {vetor[k]}')


if __name__ == '__main__':
    main()

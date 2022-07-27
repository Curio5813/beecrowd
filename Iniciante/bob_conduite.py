def main():
    """
    Você tem em mãos dois cabos circulares de energia. O primeiro cabo tem raio R1 e o segundo raio R2.
    Você precisa comprar um conduite circular (veja a imagem abaixo que ilustra um conduite) de maneira
    a passar os dois cabos por dentro dele:

    Qual o menor raio do conduite que você deve comprar? Em outras palavras, dado dois círculos,
    qual o raio do menor círculo que possa englobar ambos os dois?
    """
    t = int(input())
    for k in range(t):
        r1, r2 = input().split()
        r1, r2 = int(r1), int(r2)
        r = r1 + r2
        print(r)


if __name__ == '__main__':
    main()

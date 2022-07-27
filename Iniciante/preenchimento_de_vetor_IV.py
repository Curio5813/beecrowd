def main():
    """
    Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem
    pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez
    que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os
    próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em
    cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser
    preenchido tantas vezes quantas for necessário.
    """
    par, impar, cont = [], [], 0
    while cont < 15:
        x = int(input())
        if x % 2 == 0:
            par.append(x)
            if len(par) == 5:
                for k in range(0, len(par)):
                    print(f'par[{k}] = {par[k]}')
                par = []
        elif x % 2 == 1:
            impar.append(x)
            if len(impar) == 5:
                for k in range(0, len(impar)):
                    print(f'impar[{k}] = {impar[k]}')
                impar = []
        cont += 1
    if len(impar) > 0:
        for k in range(0, len(impar)):
            print(f'impar[{k}] = {impar[k]}')
    if len(par) > 0:
        for k in range(0, len(par)):
            print(f'par[{k}] = {par[k]}')


if __name__ == '__main__':
    main()

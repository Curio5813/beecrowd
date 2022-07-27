def main():
    """
    A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito
    tradicional quando se trata de numerar as páginas de seus livros. Ela sempre
    usa a numeração romana para isso. E seus livros nunca ultrapassam as 999 páginas
    pois, quando necessário, dividem o livro em volumes.

    Você deve escrever um programa que, dado um número arábico, mostra seu equivalente
    na numeração romana.

    Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa
    1000.

    Entrada
    A entrada é um número inteiro positivo N (0 < N < 1000).

    Saída
    A saída é o número N escrito na numeração romana em uma única linha. Use sempre
    letras maiúsculas.
    """
    lista, pagina = [], []
    romanos = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    n = int(input())
    numero = str(n)
    for k in numero:
        lista.append(int(k))
    if len(lista) == 3:
        for k in range(0, len(lista)):
            if k == 0 and lista[k] <= 3:
                pagina.append(romanos[4] * lista[k])
            elif k == 0 and lista[k] == 4:
                pagina.append(romanos[4] + romanos[5])
            elif k == 0 and 5 <= lista[k] < 9:
                pagina.append(romanos[5] + romanos[4] * (lista[k] - 5))
            elif k == 0 and lista[k] == 9:
                pagina.append(romanos[4] + romanos[6])
            elif k == 1 and lista[k] <= 3:
                pagina.append(romanos[2] * lista[k])
            elif k == 1 and lista[k] == 4:
                pagina.append(romanos[2] + romanos[3])
            elif k == 1 and 5 <= lista[k] < 9:
                pagina.append(romanos[3] + romanos[2] * (lista[k] - 5))
            elif k == 1 and lista[k] == 9:
                pagina.append(romanos[2] + romanos[4])
            elif k == 2 and lista[k] <= 3:
                pagina.append(romanos[0] * lista[k])
            elif k == 2 and lista[k] == 4:
                pagina.append(romanos[0] + romanos[1])
            elif k == 2 and 5 <= lista[k] < 9:
                pagina.append(romanos[1] + romanos[0] * (lista[k] - 5))
            elif k == 2 and lista[k] == 9:
                pagina.append(romanos[0] + romanos[2])
        print(f'{pagina[0]}{pagina[1]}{pagina[2]}')
    elif len(lista) == 2:
        for k in range(0, len(lista)):
            if k == 0 and lista[k] <= 3:
                pagina.append(romanos[2] * lista[k])
            elif k == 0 and lista[k] == 4:
                pagina.append(romanos[2] + romanos[3])
            elif k == 0 and 5 <= lista[k] < 9:
                pagina.append(romanos[3] + romanos[2] * (lista[k] - 5))
            elif k == 0 and lista[k] == 9:
                pagina.append(romanos[2] + romanos[4])
            elif k == 1 and lista[k] <= 3:
                pagina.append(romanos[0] * lista[k])
            elif k == 1 and lista[k] == 4:
                pagina.append(romanos[0] + romanos[1])
            elif k == 1 and 5 <= lista[k] < 9:
                pagina.append(romanos[1] + romanos[0] * (lista[k] - 5))
            elif k == 1 and lista[k] == 9:
                pagina.append(romanos[0] + romanos[2])
        print(f'{pagina[0]}{pagina[1]}')
    elif len(lista) == 1:
        for k in range(0, len(lista)):
            if k == 0 and lista[k] <= 3:
                pagina.append(romanos[0] * lista[k])
            elif k == 0 and lista[k] == 4:
                pagina.append(romanos[0] + romanos[1])
            elif k == 0 and 5 <= lista[k] < 9:
                pagina.append(romanos[1] + romanos[0] * (lista[k] - 5))
            elif k == 0 and lista[k] == 9:
                pagina.append(romanos[0] + romanos[2])
        print(f'{pagina[0]}')


if __name__ == '__main__':
    main()

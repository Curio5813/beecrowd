def main():
    """
    Os cientistas da NASA descobriram um novo exoplaneta que fica a 1 bilhão de
    anos luz da terra. O nome desse planeta foi batizado de Pronalândia em
    homenagem aos novos cientistas que estão sendo formados no PRONATEC. Só que o
    mais incrível ainda está por vir. Ao observar melhor o planeta eles conseguiram
    identificar que os habitantes da Pronalândia estavam querendo se comunicar por
    uma numeração. Só que a numeração que encontraram está invertida e como encontraram
    muitas delas chamaram você para conseguir automatizar esse processo. Logo, dado
    um número grande, sua tarefa é imprimir esse número invertido.

    Entrada
    O arquivo contém apenas uma linha de teste que é o número encontrado (0 < n < 9999999999).

    Obs.: Perceba que o número lido é muito alto para armazenar em uma variável do tipo int,
    logo você irá precisar utilizar o tipo long, que para a leitura e impressão em C, você
    deve utilizar o %llu.

    Saída
    Imprimir o número lido invertido. Não esqueça de imprimir a quebra de linha (\n) no
    final, caso contrário você receberá (Presentation Error).
    """
    n = int(input())
    n = str(n)
    print(n[::-1], end='\n')


if __name__ == '__main__':
    main()

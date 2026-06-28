def frequencia_de_letras():
    """
    Neste problema estamos interessados na frequência das letras em uma dada
    linha de texto.

    Especificamente, deseja-se saber qual(is) a(s) letra(s) de maior frequência
    do texto, ignorando o “case sensitive”, ou seja maiúsculas ou minúsculas
    (sendo mais claro, “letras” referem-se precisamente às 26 letras do alfabeto).

    Entrada
    A entrada contém vários casos de teste. A primeira linha contém um inteiro N
    que indica a quantidade de casos de teste. Cada caso de teste consiste de uma
    única linha de texto. A linha pode conter caracteres “não letras”, mas é
    garantido que tenha ao menos uma letra e que tenha no máximo 200 caracteres
    no total.

    Saída
    Para cada caso de teste, imprima uma linha contendo a(s) letra(s) que mais
    ocorreu(ocorreram) no texto em minúsculas (se houver empate, imprima as letras
    em ordem alfabética).
    :return:
    """
    n = int(input())
    for i in range(n):
        texto = input().lower().replace(' ', '')
        texto.strip(" ")
        contados = []
        frequencia = []
        for j in texto:
            cont = 0
            if j not in contados:
                contados.append(j)
                for k in texto:
                    if k in texto and k == j:
                        cont += 1
                frequencia.append(cont)
        maximo = max(frequencia)
        contou = []
        for j in range(len(frequencia)):
            if frequencia[j] == maximo:
                contou.append(contados[j])
        contou.sort()
        for j in range(len(contou)):
            print(f"{contou[j]}", end="")
        print("")


frequencia_de_letras()

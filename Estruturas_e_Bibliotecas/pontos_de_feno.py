def pontos_de_feno():
    """
    Cada funcionário de um serviço burocrático tem uma descrição do
    cargo - alguns parágrafos que descrevem as responsabilidades do
    trabalho. A descrição do cargo combinado com outros fatores, como
    por exemplo tempo de serviço, é utilizado para determinar qual
    é o salário deste funcionário.

    [imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_1261.jpg)

    Um sistema denominado Pontos de Feno (Hay Points) libera o departamento
    de Recursos Humanos de ter que fazer um julgamento inteligente do
    valor de cada empregado para a empresa. A descrição de um cargo ou
    função é feita através da verificação de palavras e frases que indicam
    responsabilidade. Em particular, descrições de cargo que indicam o controle
    sobre um grande orçamento ou gestão sobe um grande número de pessoas geram
    escores altos neste sistema.

    Você deve implementar um sistema de Ponto de Feno simplificado. Você terá
    como informações um dicionário Hay Point que conterá algumas palavras-chaves
    que são as descrições dos cargos e um valor em dólares americanos associado
    com cada um destes cargos. Para cada descrição de trabalho você deverá
    calcular o salário associado com o trabalho, de acordo com este sistema.

    Entrada
    A entrada contém vários casos de teste. A primeira linha da entrada contém
    dois números inteiros positivos: M (M ≤ 1000), que é o número de palavras no
    dicionário Hay Point, e um número inteiro N (N ≤ 100) que corresponde à quantidade
    de descrições de cargos ou funções. M linhas seguem, cada um contém uma palavra
    (uma seqüência de até 16 letras minúsculas) e um valor de dólar (um número
    real entre 0 e 1000000). Logo na sequência, após o dicionário, estão as
    descrições de cada uma dos cargos N.

    Cada descrição de cargo consiste em uma ou mais linhas de texto. Para sua
    conveniência, o texto contém somente letras minúsculas (de 'a' até 'z').
    Cada descrição de cargo é finalizada por uma linha contendo um ponto ".".

    Saída
    Para cada caso de teste de entrada, imprima o salário do funcionário que é
    calculado através deste sistema Pontos de Feno (que nada mais é do que a soma
    do valor de todas as palavras que aparecem na descrição do cargo). Obs.: o valor
    das palavras que não aparecem no dicionário é zero (0).
    :return:
    """
    n, m = map(int, input().split())
    dicionario, descricoes, texto, cont, valor = {}, [], "", 0, 0
    for i in range(n):
        palavra_valor = input().split()
        dicionario[palavra_valor[0]] = int(palavra_valor[1])
    while cont < m:
        descricao = input()
        texto += descricao
        if "." in texto:
            cont += 1
            descricoes.append(texto)
            texto = ""
    for i in range(0, len(descricoes)):
        for key in dicionario:
            if descricoes[i].count(key) >= 1:
                valor += dicionario[key] * descricoes[i].count(key)
        print(valor)
        valor = 0


if __name__ == '__main__':
    pontos_de_feno()

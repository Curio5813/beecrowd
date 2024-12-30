def digitando_no_telefone_celular():
    """
    Uma equipe de pesquisadores está desenvolvendo uma nova
    tecnologia para economizar tempo ao digitar mensagens de
    texto em dispositivos móveis. Eles estão trabalhando em
    um novo modelo que tem um teclado completo, assim os usuários
    podem digitar qualquer letra pressionando a tecla correspondente.
    Desta forma, um usuário precisa pressionar P teclas para digitar
    uma palavra de comprimento P.

    No entanto, isto não é suficientemente rápido. A equipe vai montar
    um dicionário de palavras comuns que um usuário pode digitar. O objetivo
    é reduzir o número médio de teclas pressionadas necessárias para
    digitar palavras que constam no dicionário. Durante a digitação de
    uma palavra, sempre que houver apenas uma possibilidade para a seguinte
    letra, o sistema de telefone celular irá introduzí-la automaticamente,
    sem a necessidade de digitação. Para ser mais preciso, o comportamento
    do sistema de telefone celular irá ser determinado pelas seguintes regras:

    1. O sistema nunca irá adivinhar a primeira letra de uma palavra, ou seja,
    para a primeira letra sempre terá que ser pressionada a tecla correspondente.

    2. Se uma sucessão não-vazia de letras c1c2...cn for introduzida, e houver uma
    letra c tal que cada palavra no dicionário que começa com c1c2...cn também começa
    com c1c2 ... cnc, em seguida, o sistema coloca a entrada c automaticamente,
    sem a necessidade de uma combinação de teclas. Caso contrário, o sistema
    aguarda o usuário.

    Por exemplo, se o dicionário é composto das palavras "hello", "hell", "heaven"
    e "goodbye", e o usuário pressiona "h", o sistema colocará a letra "e" automaticamente,
    porque cada palavra que começa com "h" também começa com "he". No entanto, uma vez
    que existem palavras que começam com "hel" e com "hea", o sistema precisa agora
    esperar a próxima digitação do usuário. Se o usuário pressionar então o "l",
    obtendo-se a palavra parcial "hel", o sistema de entrada incluirá um segundo "l"
    automaticamente. Quando se tem o "hell" como entrada, o sistema não pode supor nada,
    porque é possível que a palavra terminou, ou também é possível que o usuário pode
    querer pressionar "o" para obter "hello". Desta forma, para digitar a palavra "hello"
    o usuário precisa de três teclas, "hell" exige duas e "heaven" também requer duas,
    porque quando a entrada é "hea" o sistema pode colocar automaticamente o restante da
    palavra aplicando repetidamente a segunda regra. Da mesma forma, a palavra "goodbye"
    precisa de apenas uma tecla, porque depois de pressionar a inicial "g", a sistema irá
    preencher automaticamente a palavra inteira. Neste exemplo, o número médio de teclas
    necessário digitar uma palavra no dicionário é, então, (3 + 2 + 2 + 1) / 4 = 2.00.

    Dado um determinado dicionário, sua tarefa então é calcular o número médio de teclas
    necessárias para escrever uma palavra no dicionário com o novo sistema para celular
    desenvolvido pelos pesquisadores.

    Entrada
    Cada caso de teste é descrito por várias linhas. A primeira linha contém um número
    inteiro N representando o número de palavras no dicionário (1 ≤ N ≤ 105 ). Cada uma
    das próximas N linhas contém uma string não-vazia de no máximo 80 letras minúsculas
    do alfabeto inglês, representando uma palavra no dicionário. Dentro de cada caso de
    teste todas as palavras são diferentes, e a soma dos comprimentos de todas as palavras
    é, no máximo, 106.

    Saída
    Para cada caso de teste de entrada imprima um número com duas casas decimais (arredondado
    caso necessário) que representa o número médio de pressionamentos de tecla necessários
    para digitar uma palavra no dicionário.
    :return:
    """
    while True:
        try:
            j, k, cont, dicionario, teclas = 0, 0, 0, [], []
            n = int(input())
            for i in range(n):
                palavra = input()
                dicionario.append(palavra)
            for i in range(1, len(dicionario)):
                while dicionario[k][j] == dicionario[i][j]:
                    if j >= len(dicionario[i]) - 1 or k >= len(dicionario) - 1:
                        teclas.append(cont)
                        cont = 0
                        j = 0
                        break
                    cont += 1
                    j += 1
                k += 1
            print(teclas)
        except EOFError:
            break


digitando_no_telefone_celular()



"""
4
hello
hell
heaven
goodbye
3
hi
he
h
7
structure
structures
ride
riders
stress
solstice
ridiculous
"""
def o_caso_douglas():
    """
    No bairro do Bronx, existe um prolífico ladrão de carros, conhecido pela
    polícia por roubar apenas carros da marca Pontial. O detetive Jaques trabalha
    no caso há 10 anos perseguindo os passos do bandido do Pontial. Após todo esse
    tempo, o detetive foi capaz de reconhecer um padrão nos registros da delegacia:
    o número dos casos registrados relacionados ao bandido do Pontial são sempre
    divisíveis por 7, são ímpares e, se somado a dois, é um número primo. Como o
    detetive Jaques não se sente confortável com matemática, ele pediu a sua ajuda
    para saber se o Douglas irá atacar novamente conhecendo o número do último caso
    registrado na delegacia.

    (O erro encontrado pode ser solucionado adicionando +1, ao número entrada)
    Entrada
    A primeira linha de cada caso de teste contém um inteiro n
    (1 ≤ n ≤ 10^4)
    que determina a quantidade de consultas que o detetive Jaques quer fazer. As
    próximas n linhas indicam o número do último caso registrado.

    Saída
    Para cada consulta, imprima "Yes" se o próximo caso será um ataque de Douglas
    e "No" caso contrário.
    :return:
    """
    n = int(input())
    for i in range(n):
        numero = int(input())
        # print(numero)
        if numero % 7 != 0:
            print("No")
        elif numero % 7 == 0:
            numero += 2
            # print(numero)
            for j in range(2, numero + 1):
                if numero % j == 0 and j != numero:
                    print("No")
                    break
                if numero % j == 0 and j == numero:
                    print("Yes")


o_caso_douglas()

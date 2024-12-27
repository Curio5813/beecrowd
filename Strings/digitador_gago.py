def digitador_gago():
    """
    Francisco Iote é uma gago diferente. Ele não somente fala
    repetindo sílabas como estranhamente quando digita um texto
    ele repete algumas sílabas, tornando a leitura muito chata.
    Ele repete apenas sílabas que tenham exatamente 2 letras e
    nunca repete uma sílaba que não seja a primeira sílaba da
    palavra. Ele também repete apenas uma vez, ou seja a palavra
    bola, por exemplo, pode aparecer como bola ou bobola, nunca
    bobobola.

    Você foi chamado como perito para traduzir alguns textos excritos
    por Francisco eliminando as redundâncias de texto por ele geradas.

    Entrada
    A entrada é composta por apenas uma linha com até 1000 palavras,
    cada uma delas com no máximo 15 caracteres. Esta linha de texto
    deve ser corrigida eliminando-se as redundâncias, conforme exemplo
    abaixo.

    Saída
    Seu programa deve gerar uma versão do texto fornecido por Francisco
    que não contenha as repetições descritas acima.
    :return:
    """
    texto = input()
    i, revisao = 0, ""
    while i <= len(texto) - 1:
        if texto[i:i+2] == texto[i+2:i+4]:
            revisao += texto[i+2:i+4]
            i += 4
        else:
            revisao += texto[i]
            i += 1
    print(revisao)


digitador_gago()

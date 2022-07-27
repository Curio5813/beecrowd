def main():
    lista = []
    ddd = int(input())
    dicionario = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro', 32: 'Juiz de Fora',
                  19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}
    for key, values in dicionario.items():
        if ddd == key:
            lista.append(values)
    if len(lista) > 0:
        print(lista[0])
    else:
        print('DDD nao cadastrado')


if __name__ == '__main__':
    main()

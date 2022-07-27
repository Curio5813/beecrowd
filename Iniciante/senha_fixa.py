def main():
    """
    Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura
    de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada
    corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere
    que a senha correta é o valor 2002.
    """
    while True:
        senha = 2002
        login = int(input())
        if login != senha:
            print('Senha Invalida')
        elif login == senha:
            print('Acesso Permitido')
            break


if __name__ == '__main__':
    main()

def numeros_ma_sorte_pequenos():
    """
    Um número 3 é de má sorte se contém um 1 seguido
    por um 3 entre seus dígitos. Por exemplo, o número 341329
    é de má sorte, enquanto o número 26771 não é.
    :return:
    """
    n = input()
    for i in range(0, len(n)):
        if i == len(n) - 1:
            print(f"{n} NO es de Mala Suerte")
            break
        if n[i] == "1" and n[i + 1] == "3":
            print(f"{n} es de Mala Suerte")
            break


numeros_ma_sorte_pequenos()

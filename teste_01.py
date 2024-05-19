booleano = 0
for i in range(1, 100):
    for k in range(1, 100):
        if i != k and i ** k == k ** i:
            print(i, k)
            booleano = 1
            break
    if booleano == 1:
        break

aux = [1, 2, 3, 4, 5, 6]
k = 5
for i in range(10):
    if len(aux) == 3:
        break
    while k <= len(aux):
        aux.pop(k - 1)
        k += 5
    k = k - len(aux) - 1

print(aux)




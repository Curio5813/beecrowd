"""
Observações sobre alguns problemas.
"""


dados, estrutura, estruturas = [1, 2, 3], [], []
x1 = [1, 1, 1, 1, 1, 1, 1]  # 1
x2 = [2, 1, 1, 1, 1, 1]  # 6
x3 = [2, 2, 1, 1, 1]  # 5
x4 = [2, 2, 2, 1]  # 4
x5 = [3, 1, 1, 1, 1] # 5
x6 = [3, 3, 1]  # 3
x7 = [3, 1, 1, 2]  # 4
x8 = [3, 2, 2] # 3


n = int(input())

for i in range(n):
    estrutura.append(dados[0])
estruturas.append(estrutura)
temp = estrutura.copy()
a, b = 0, 1
cont = 0
for i in range(n):
    if not temp:
        temp = estrutura.copy()
        a = 0
        b += 1
        temp.insert(a, dados[b])
    else:
        temp.insert(a, dados[b])
        temp.pop()
    while sum(temp) != n:
        if not temp:
            break
        temp.pop()
    if sum(temp) == n:
        # print(a, temp, end=" ")
        if a == 0:
            estruturas.append(temp)
            temp = estruturas[-1].copy()
            a += 1
        else:
            if dados[b] == 3:
                estruturas.append(temp)
                temp = estruturas[a + 1].copy()
                a += 1
                b = 1
                print(dados[b])
            else:
                estruturas.append(temp)
                temp = estruturas[a + 1].copy()
                a += 1
        # print(temp, estruturas, i)
print(estruturas)
soma = 1
for i in range(1, len(estruturas)):
    soma += len(estruturas[i])
print(soma)



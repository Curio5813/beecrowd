cont = 0
for i in range(3, 360):
    if 360 % i == 0:
        print(i, end=" ")
        cont += 1
print("\n")
print(cont)

a = 102478
b = 83

temp = 102478
while b < temp:
    if b * 10 > temp:
        break
    temp //= 10
    print(temp)
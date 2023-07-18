from time import time

start = time()
flag, num = 1, 20
while flag != 0:
    for i in range(1, 20 + 1):
        if num % i == 0:
            flag = 0
        elif num % i != 0:
            flag = 1
            num += 1
            break

print(num)
end = time()
print(end - start)

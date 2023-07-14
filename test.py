from time import time


start = time()
cont, num = 1, 20

for i in range(1, 1001):
    for k in range(1, 1001):
        if k >= i:
            break
        for j in range(1, 1001):
            if j >= k:
                break
            if i ** 2 == k ** 2 + j ** 2 and i + k + j == 1000:
                print(f"{i} {k} {j}")


end = time()
print(end - start)

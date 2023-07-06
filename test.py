from time import time

begin = time()

for i in range(1, 10_000_000):
    i += 1
    print(i)

end = time()
print(end - begin)


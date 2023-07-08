from time import time

begin = time()

for i in range(1, 100_000_000):
    i += 1
    print(i)

end = time()
print(end - begin)


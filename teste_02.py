from time import time

start = time()
soma = 0

for i in range(1, 1_000_000_000 + 1):
    soma += i

print(soma)
end = time()
print(f"{(end - start):.2f}")

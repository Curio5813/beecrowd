from itertools import combinations, permutations
from math import factorial
from random import randint

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2, l3, l4, l5 = [], [], [], []
arranjos = list(permutations(l1, 3))
num = ""
for i in range(0, len(arranjos)):
    for k in range(0, len(arranjos[i])):
        num += str(arranjos[i][k])
    l2.append(num)
    num = ""
print(l2)
for i in range(0, len(l2)):
    for k in range(0, len(l2[i])):
        l3.append(int(l2[i][k]))
    l4.append(l3)
    l3 = []
for i in range(0, len(l4)):
    for k in range(0, len(l4[i])):
        if sum(l4[i]) == 6 and 4 in l4[i]:
            l5.append(l4[i])
            break
        elif sum(l4[i]) == 6 and 5 in l4[i]:
            l5.append(l4[i])
            break
print(l5)

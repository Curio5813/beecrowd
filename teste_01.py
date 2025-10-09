from statistics import mean
from math import ceil, floor

livros, medias, medias_cima, medias_baixo = [], [], [], []
for i in range(5):
    livros.append(list(map(int, input().split())))
for i in range(len(livros)):
    medias.append(mean(livros[i]))
soma = 0
for i in range(len(livros)):
    soma += max(livros[i])
for i in range(len(medias)):
    medias_cima.append(ceil(medias[i]))
    medias_baixo.append(floor(medias[i]))
diff_medias = (sum(medias_cima) - sum(medias_baixo))
print(medias_cima)
print(medias_baixo)
print(soma)




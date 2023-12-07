from scipy import integrate


def funcao_integral(x):
    return x ** 2


resultado = integrate.quad(funcao_integral, 0, 5)
print(resultado)

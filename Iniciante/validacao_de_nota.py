def main():
    from statistics import mean
    """
    Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
    média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer
    ao intervalo [0,10]). Cada nota deve ser validada separadamente.

    Entrada
    A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando
    forem lidas duas notas válidas.

    Saída
    Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
    Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do
    cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.
    """
    while True:
        notas = []
        try:
            nota1 = input()
            nota1 = float(nota1)
            while nota1 < 0 or nota1 > 10:
                print('nota invalida')
                nota1 = input()
                nota1 = float(nota1)
        except EOFError:
            return None
        else:
            notas.append(nota1)
        try:
            nota2 = input()
            nota2 = float(nota2)
            while nota2 < 0 or nota2 > 10:
                print('nota invalida')
                nota2 = input()
                nota2 = float(nota2)
        except EOFError:
            return None
        else:
            notas.append(nota2)
        print(f'media = {mean(notas):.2f}')


if __name__ == '__main__':
    main()

def main():
    numero = int(input())
    hora_trabalho = int(input())
    valor_hora = round(float(input()), 2)
    print(f'NUMBER = {numero}\n'
          f'SALARY = U$ {(hora_trabalho * valor_hora):.2f}')


if __name__ == '__main__':
    main()

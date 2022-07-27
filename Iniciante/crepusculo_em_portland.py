def main():
    """
    No crepúsculo, a cidade de Portland fica cheia de vampiros e lobisomens. Entretanto,
    nenhum deles quer ser visto enquanto passeiam pelo centro.

    Vão ser instaladas câmeras de vigilância em cada esquina do centro de Portland. A cada
    mês, um mapa atualizado com as câmeras já em funcionamento é disponibilizado no site
    da prefeitura.

    Uma quadra é considerada segura se existem câmeras em, pelo menos, duas de suas quatro
    esquinas. No centro de Portland todas as quadras são quadrados de mesmo tamanho.

    Sua tarefa é, dado o mapa das câmeras em funcionamento nas esquinas, indicar o status de
    todas as quadras do centro.

    Entrada
    A primeira linha da entrada tem um inteiro positivo N (1 ≤ N ≤ 100). Nas próximas N+1
    linhas, existem N+1 números, que indicam, para cada esquina, a presença ou ausência de
    uma câmera de vigilância em funcionamento. O número 1 indica que existe uma câmera
    funcionando na esquina, enquanto o número zero indica que não há câmera funcionando.

    Saída
    A saída é dada em N linhas. Cada linha tem N caracteres, indicando se a quadra correspondente
    é segura ou insegura. Se uma quadra é segura, mostre o caractere S; se não é segura, mostre
    o caractere U.
    """
    rows, answer, answers, solution, solutions = [], [], [], '', []
    n = int(input())
    for k in range(n + 1):
        row = [int(x) for x in input().split()]
        rows.append(row)
    for k in range(0, len(rows) - 1):
        for i in range(0, len(rows[k])):
            if k >= len(rows) - 1 or i >= len(rows[k]) - 1:
                break
            if rows[k][i] == 1 and rows[k][i + 1] == 1:
                answer.append('S')
            elif rows[k][i] == 1 and rows[k + 1][i] == 1:
                answer.append('S')
            elif rows[k][i] == 1 and rows[k + 1][i + 1] == 1:
                answer.append('S')
            elif rows[k][i + 1] == 1 and rows[k + 1][i] == 1:
                answer.append('S')
            elif rows[k][i + 1] == 1 and rows[k + 1][i + 1] == 1:
                answer.append('S')
            elif rows[k + 1][i] == 1 and rows[k + 1][i + 1] == 1:
                answer.append('S')
            else:
                answer.append('U')
        answers.append(answer)
        answer = []
    for k in range(0, len(answers)):
        for i in range(0, len(answers[k])):
            solution += answers[k][i]
        solutions.append(solution)
        solution = ''
    for k in range(0, len(solutions)):
        print(solutions[k])


if __name__ == '__main__':
    main()

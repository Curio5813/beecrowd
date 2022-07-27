def main():
    n1, n2, n3, n4 = input().split(' ')
    n1, n2, n3, n4, = float(n1), float(n2), float(n3), float(n4)
    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
    media = round(media, 1)
    if media >= 7.0:
        print(f'Media: {media:.1f}\n'
              f'Aluno aprovado.')
    elif media <= 4.9:
        print(f'Media: {media:.1f}\n'
              f'Aluno reprovado.')
    elif 5.0 <= media <= 6.9:
        print(f'Media: {media:.1f}\n'
              f'Aluno em exame.')
        nota_exame = float(input())
        media_final = (media + nota_exame) / 2
        media_final = round(media_final, 1)
        if media_final <= 4.9:
            print(f'Nota do exame: {nota_exame:.1f}\n'
                  f'Aluno reprovado.\n'
                  f'Media final: {media_final:.1f}')
        elif media_final >= 5.0:
            print(f'Nota do exame: {nota_exame:.1f}\n'
                  f'Aluno aprovado.\n'
                  f'Media final: {media_final:.1f}')


if __name__ == '__main__':
    main()

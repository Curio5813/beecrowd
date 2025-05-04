from collections import Counter


def os_presentes_do_noel():
    """
    Noel está pedindo sua ajuda para distribuir seus presentes de maneira ótima.

    Ele te deu uma lista contendo um número N, seguido por N inteiros gi, e te contou
    que estas anotações eram sobre N crianças que ele andou observando durante este
    ano. Cada um destes N números representa quantas boas ações cada criança fez.

    Agora ele quer distribuir presentes, mas ele quer ser justo em relação à quantas
    boas ações cada criança fez e quantos presentes elas merecem. Ele te deu três restrições:

    Toda criança deve receber no mínimo 1 presente.
    Para todo par de crianças A e B, tal que ambas fizeram a mesma quantidade de boas ações,
    ambas merecem receber a mesma quantidade de presentes.
    Para todo par de crianças A e B, tal que a criança A fez mais boas ações que a criança B,
    a criança A merece receber mais presentes que a criança B.
    Por exemplo, vamos supor que há 3 crianças, e que a primeira criança fez 1 ato bom este
    ano, a segunda fez 3 atos bons, e a terceira fez 1 ato bom. Uma forma válida de distribuir
    presentes seria dar 3 presentes para a primeira e terceira criança (pois elas fizeram a
    mesma quantidade de atos bons), e 5 presentes para a segunda criança (pois ela fez mais
    atos bons que as outras). Note que esta distribuição respeita as restrições, mas ela não
    é a única, e nem a mais econômica forma de distribuir os presentes.

    Após receber as anotações de Noel, você deve ajudá-lo a descobrir a quantidade total mínima
    de presentes a serem enviados às crianças. Você deve lembrar de respeitar as restrições
    estabelecidas, e deve tentar minimizar quantos presentes serão enviados no total.

    Entrada
    A primeira linha de entrada contém um inteiro N (1 ≤ N ≤ 104), representando a quantidade
    de crianças à quem os presentes serão distribuídos.

    A segunda linha de entrada contém N inteiros gi (1 ≤ gi ≤ 104, para todo 1 ≤ i ≤ N), representando
    que a i-ésima criança fez gi boas ações neste ano.

    Saída
    Você deve imprimir uma linha, contendo um inteiro, representando a quantidade total mínima de
    presentes que devem ser enviados às crianças.
    :return:
    """
    n = int(input())
    acoes_crianca = list(map(int, input().strip().split(" ")))
    presentes, bonus = 0, 1
    contagem = Counter(acoes_crianca)

    for i, (acoes, qtd) in enumerate(sorted(contagem.items()))    :
        if i == 0:
            if acoes == 1:
                presentes += 1
            else:
                presentes += qtd
            bonus += 1
        else:
            if acoes == 1:
                presentes += bonus
            else:
                presentes += qtd * bonus
            bonus += 1
    print(presentes)


os_presentes_do_noel()

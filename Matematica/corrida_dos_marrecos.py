from math import ceil


def corrida_dos_marrecos():
    """
    Pirabeiraba é um distrito de Joinville, onde colonizadores
    alemães se instalaram no início do século XX. Anualmente há
    a festa do aipim, tubérculo conhecido como macaxeira no nordeste
    do Brasil. Para acompanhar o aipim, nada como um prato típico
    germânico: o marreco recheado! Para os entendidos de culinária,
    há uma magia nesta combinação: marreco com aipim. Contudo, para
    matar o marreco, você deve capturá-lo quando este estiver com o
    sangue bem quente. Para isto, o marreco deve estar cansado. Dizem
    que seu sangue quente é sinônimo de fertilidade, para não dizer:
    afrodisíaco! Mas isto é uma outra história.

    Nesta brincadeira de correr atrás do marreco, surgiu a ideia de
    cansá-los com uma corrida entre eles. O espaço físico da Sociedade
    Rio da Prata é limitado, assim, construíram apenas 3 raias para se
    realizar estas corridas. As corridas são feitas em grupos de 2 e 3
    marrecos. Os primeiros colocados destes grupos são novamente divididos
    em grupos de 2 ou 3 para uma nova rodada. Isto acontece até que só
    reste o marreco campeão, que, como prêmio foge (por ora) da panela.
    Todos os marrecos sobreviventes devem correr na rodada, isto é, se
    não for possível dividir todos os marrecos em grupos de 3, alguns
    grupos de 2 devem ser formados, mas de forma a minimizar o número
    de corridas. Exemplos são vistos na Figura 1.

    ![imagem](https://resources.beecrowd.com/gallery/images/novos/
    Corrida%20dos%20Marrecos.png)

    Figura 1: Exemplos: Competição com 4, 5 e 6 marrecos.

    Os marrecos perdedores, por sua vez, serão os primeiros a irem para
    panela. Você foi convidado para comer marreco com aipim, mas, em troca,
    deve escrever um programa que calcule o número de corridas realizadas
    para se determinar o marreco campeão.

    Entrada
    A entrada do programa é composta por vários casos de teste. Cada caso de
    teste é composto por uma linha contendo um número inteiro n(que representa
    o número de marrecos), sendo que 0 ≤ n ≤ 100.000, sendo que n = 0 é
    utilizado unicamente para marcar o término das entradas, sendo que este deve
    ser desconsiderado.

    Saída
    O seu programa deve imprimir na saída padrão uma linha por caso de teste,
    contendo o número de corridas necessárias para escolher o marreco campeão.
    :return:
    """
    while True:
        n = int(input())
        cont, corridas = 1, 1
        if n == 0:
            break
        if n == 1:
            print(0)
        else:
            if n % 3 == 0:
                corridas = n // 2 + 1
            else:
                resto = n % 2
                quociente = n // 2
                corridas = quociente + resto
            print(corridas)


corrida_dos_marrecos()

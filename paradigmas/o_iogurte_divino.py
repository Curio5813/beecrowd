def o_iogurte_divino():
    """
    Aaa Muzambinho... além de seus belos cafezais, também é
    conhecido pelos seus deliciosos iogurtes. Milton, junto
    com seu amigo Neves, criaram um grupo de degustação de
    iogurtes chamado Encoders.

    No Encoders eles degustam os diversos tipos de iogurte da
    cidade. Milton e Neves perceberam que, misturando os iogurtes,
    conseguem sabores nunca antes provados! Então propuseram um
    desafio para divertimento do grupo: juntos eles escolheram
    um "valor de gostosura" para cada iogurte. Eles também sabem
    o volume de cada um.

    Milton quer encher uma garrafa para levar para sua faculdade
    com o melhor iogurte possível em termos de "gostosura" e esta
    garrafa tem um volume máximo X. O desafio então se resume a
    obter um iogurte com a "gostosura" máxima possível.

    Sabendo o volume e o "valor de gostosura" de cada iogurte do grupo,
    determine o valor de "gostosura" máximo que Milton consegue formular
    em sua garrafa e fazer a alegria de seus amiguinhos na faculdade.

    Obs: Eles nem sempre precisam colocar o volume total de um iogurte na
    garrafa, e assim o preço iogurte é proporcional ao volume colocado.

    Entrada
    A primeira linha da entrada indica o número T de casos de teste.

    A segunda linha contém dois inteiros N e X indicando, respectivamente, o
    número de iogurtes e a capacidade da garrafa.

    A seguir, seguem N linhas, cada uma contendo 2 inteiros, indicando o valor
    do iogurte e o seu volume, respectivamente.

    Limites:

    1 <= T <= 100;

    1 <= N, X <= 100.

    Saída
    Um valor real com duas casas decimais indicando o valor máximo de “gostosura”
    a ser obtido.
    :return:
    """
    while True:
        try:
            t = int(input())
            for i in range(t):
                n, x = map(int, input().split(" "))
                (iogurtes, gostosura, volume, gostosuras, volumes,
                 garrafa, valor, maiores) = [], [], [], [], [], 0, 0, []
                for j in range(n):
                    iogurte1 = list(map(int, input().split(" ")))
                    iogurtes.extend(iogurte1)
                for j in range(0, len(iogurtes)):
                    if j % 2 == 0:
                        gostosura.append(iogurtes[j])
                    if j % 2 != 0:
                        volume.append(iogurtes[j])
                gostosuras.append(gostosura)
                volumes.append(volume)
                for j in range(len(gostosura) - 1, 0, -1):
                    rotation1 = gostosura[j:] + gostosura[:j]
                    rotation2 = volume[j:] + volume[:j]
                    gostosuras.append(rotation1)
                    volumes.append(rotation2)
                full = x
                for j in range(0, len(gostosuras)):
                    for k in range(0, len(gostosuras[j])):
                        if x >= volumes[j][k]:
                            x -= volumes[j][k]
                            valor += gostosuras[j][k]
                        elif x < volumes[j][k]:
                            valor += gostosuras[j][k] * (x/volumes[j][k])
                            break
                    maiores.append(valor)
                    x = full
                    valor = 0
                print(f"{max(maiores):.2f}")
        except EOFError:
            break


o_iogurte_divino()

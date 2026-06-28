def escrita_rapida_o_duelo():
    """
    Matheus e seu irmão gêmeo Vinicius adoram disputar para ver quem
    digita mais rápido. Após muitos anos de duelo, eles chegaram à conclusão
    que o duelo nem sempre é vencido por aquele que apenas digita mais rápido,
    pois outros fatores influenciam no ganhador. Como cada um participa de
    sua própria casa, eles possuem um certo atraso para receber e enviar os dados
    do servidor. Eles também têm um tempo de reação diferente, o que pode fazer
    com que algum deles comece a digitar depois. E é claro, cada um tem a sua
    velocidade de digitação.

    Sendo fornecido o atraso referente a conexão de cada um, o seu tempo de reação,
    e a velocidade de escrita, quem será o ganhador?

    Entrada
    A entrada consiste de 3 linhas. Na primeira serão fornecido três inteiros Am,
    Rm, Em, representando respetivamente o tempo de atraso da conexão de Matheus,
    o seu tempo de reação e o tempo de escrita, ou seja, o tempo que ele gasta para
    digitar cada caractere independente de qual seja, em milissegundos. Na segunda
    linha serão fornecido três inteiros Av, Rv, Ev, com as informações de Vinicius.
    A terceira e última linha consiste de uma frase S, contendo apenas caracteres
    alfanuméricos, sinais de pontuação e espaços, usada no duelo.

    1 ≤ Am, Rm, Em, Av, Rv, Ev ≤ 1000

    1 ≤ |S| ≤ 100000

    Saída
    Você deve informar quem será o ganhador do duelo, ou “Empate”, sem as aspas, caso
    termine empatado.
    :return:
    """
    am, rm, em = map(int, input().split())
    av, rv, ev = map(int, input().split())
    frase = input()
    tempo_escrita_m = len(frase) * em + 2 * am + rm
    tempo_escrita_v = len(frase) * ev + 2 * av + rv
    if tempo_escrita_m < tempo_escrita_v:
        print("Matheus")
    if tempo_escrita_m > tempo_escrita_v:
        print("Vinicius")
    if tempo_escrita_m == tempo_escrita_v:
        print("Empate")


if __name__ == '__main__':
    escrita_rapida_o_duelo()

def oceano_profundo_faca_o_raso():
    """
    Oceano profundo
    Estou com tanto medo de mostrar meus sentimentos,
    Eu naveguei por um milhão de tetos
    Em meu quarto solitário
    Oceano profundo

    Os versos acima fazem parte de uma tradução livre da letra de
    uma música popular de Cliff Richard. Neste problema, iremos lidar
    com um tipo similar de pessoa. O nome dessa pessoa é Rampell-Stilt-Skin.
    Além disso, um outro fato importante: ele é um homem morto. Alguém o
    matou alguns dias atrás, e você é o detetive que deve resolver o
    mistério. O problema deste homem é que ele sempre tentou esconder
    suas informações e seus sentimentos "abaixo do mar" (isto é, fora de alcance).
    Ele escreveu um diário que contém algumas sentenças e um grande número
    em binário (este número pode ter até 10000 dígitos). Se o número é divisível
    pelo número primo 131071, então as sentenças são verdadeiras, e, caso contrário,
    elas são falsas.

    Dados números grandes em binário, você deve verificar se cada número é divisível
    por 131071 ou não. Seu algoritmo deve ser eficiente o bastante.

    Entrada
    O arquivo de entrada contém vários números em binário. Cada número em binário começa
    em uma linha nova, mas pode ser expandido em várias linhas. Cada número é terminado
    pelo simbolo #. Nenhuma linha contém mais de 100 dígitos.

    Saída
    Para cada número em binário, imprima "YES" se o número é divisível pelo número primo dado,
    ou "NO" caso contrário.
    :return:
    """
    primo = 131071
    while True:
        binary = ""
        try:
            binary += input()
            while "#" not in binary:
                binary += input()
            binary = binary.strip("#")
            base_dez = int(binary, 2)
            if base_dez % primo == 0:
                print("YES")
            else:
                print("NO")
        except EOFError:
            break


oceano_profundo_faca_o_raso()

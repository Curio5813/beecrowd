def pacman():
    """
    Pacman é um jogo muito conhecido, onde o personagem
    tenta comer a maior quantidade possível de bolinhas,
    tendo ao mesmo tempo que fugir de vários fantasmas.
    Dessa vez, nosso personagem quer carregar a comida
    coletada para casa, mas o encontro com um fantasma,
    ao invés de terminar o jogo, faz com que toda a comida
    coletada seja roubada.

    Neste problema os fantasmas não se movem, e o jogador
    sempre faz o Pacman percorrer o seguinte caminho:

    O Pacman começa no canto superior esquerdo do tabuleiro.
    O Pacman percorre toda a linha, da esquerda para direita,
    até chegar ao lado direito do tabuleiro.
    O jogador desce uma posição, e percorre toda a linha, desta vez
    da direita para a esquerda.
    As etapas 2 e 3 se repetem até que todo o tabuleiro tenha sido
    percorrido.
    Infelizmente, Pacman não pode ignorar os comandos do usuário para
    fugir dos fantasmas ou pegar mais comida, mas ele pode, a qualquer
    momento, se aproveitar de um bug de implementação e interromper
    o jogo, levando consigo toda a comida que estiver carregando.

    Você deve escrever um programa que determine a maior quantidade
    de comida que o Pacman pode levar, se escolher a melhor hora possível
    para sair. Note que o jogador também tem a opção de não sair antes
    do final do jogo.

    Entrada
    A primeira linha contém um inteiro N (2 ≤ N ≤ 100), o tamanho do
    tabuleiro do jogo, que é quadrado. Cada uma das N linhas seguintes
    contém N caracteres, que podem ser (aspas para melhor clareza):

    ‘.’ um espaço vazio;
    ‘o’ uma comida;
    ‘A’ um fantasma.
    Não há um fantasma e uma comida na mesma posição.

    Não há fantasma nem comida na posição inicial do Pacman (ou seja, o primeiro
    caractere da primeira linha do tabuleiro é ‘.’).

    Saída
    Seu programa deve produzir uma única linha contendo um único inteiro, a quantidade
    máxima de comida que o Pacman pode levar para casa.
    :return:
    """
    n = int(input())
    movimento, movimentos, cont, maior = "", "", 0, 0
    for i in range(n):
        movimento += input()
        if i % 2 == 0:
            movimentos += movimento
            movimento = ""
        if i % 2 == 1:
            movimentos += movimento[::-1]
            movimento = ""
    for i in range(0, len(movimentos)):
        if movimentos[i] == "o":
            cont += 1
        if cont > maior:
            maior = cont
        if movimentos[i] == "A":
            cont = 0
    print(maior)


pacman()

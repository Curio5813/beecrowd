from math import tan, radians


def flecha_no_coelho():
    """
    Olivera Queen é uma arqueira muito habilidosa. Ela consegue atingir
    qualquer alvo a longas distâncias sem muita dificuldade. Desta vez,
    ela quer realizar um treinamento com seus dois companheiros de caça
    de uma forma um tanto inusitada: o alvo será um coelho de pelúcia.
    O arqueiro escolherá a própria postura e sua distância até a árvore
    onde estará posicionado o coelho, e a partir dessas informações, o
    coelho deverá ser posicionado de forma que o arqueiro consiga o
    atingir diretamente, sem realizar nenhum movimento adicional. A imagem
    abaixo exemplifica a situação de modo genérico:

    ![imagem](https://resources.beecrowd.com/gallery/images/contests/UOJ_231_F.jpg)

    A distância entre o arqueiro e a árvore é representada por D, a altura
    dos ombros do arqueiro aos seus pés é representada por A e a altura em
    que o coelho de pelúcia deve ser posicionado para que o arqueiro o alveje
    na cabeça é H. O ângulo que a árvore e o arqueiro fazem com o chão será
    sempre de 90º, enquanto que o ângulo que o braço do arqueiro faz com o
    próprio corpo será escolhido por ele mesmo.

    Portanto, ajude Olivera Queen e seus dois promissores amigos de caça a
    realizarem seus treinamentos do modo como eles planejaram: escreva um
    programa que encontre o valor H apropriado para que o coelho de pelúcia
    seja atingido na cabeça, de acordo com as informações dadas. Considere
    que a flecha viajará sempre em linha reta, independente de sua distância
    até o alvo.

    Entrada
    A entrada contém diversos casos de teste. Cada linha contém um valor real
    A (1 ≤ A ≤ 2) indicando a altura do arqueiro, um valor real D (5 ≤ D ≤ 40)
    que indica a distância entre o arqueiro e a árvore e um valor real R (50 ≤ R ≤ 150)
    indicando o ângulo, em graus, entre o braço do arqueiro e seu corpo. É garantido
    que as entradas sejam sempre válidas e não gerem saídas inesperadas. A entrada
    termina com fim de arquivo (EOF).

    Saída
    Para cada caso de teste, imprima o valor de H com precisão de 4 casas decimais.
    :return:
    """
    while True:
        try:
            a, d, r = map(float, input().split(" "))
            hzinho = d / tan(radians(r))
            h = a - hzinho
            print(f"{h:.4f}")
        except EOFError:
            break


flecha_no_coelho()

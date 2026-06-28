def derivada_de_13_variaveis():
    """
    A derivada de uma função y = f(x) num ponto x = x0, é igual ao valor
    da tangente trigonométrica do ângulo formado pela tangente geométrica
    à curva representativa de y = f(x), no ponto x = x0, ou seja, a derivada
    é o coeficiente angular da reta tangente ao gráfico da função no ponto x0.

    A derivada de uma função y = f(x) pode ser representada também pelos símbolos:

    y', dy/dx ou f ' (x).

    A derivada de uma função f(x) no ponto x0 é dada por:

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-a.png)

    Na geometria clássica, a linha tangente ao gráfico da função f em a foi a única
    linha que passou pelo ponto (a, f(a)) que não encontrou o gráfico de f transversalmente,
    significando que a linha não passou diretamente pelo gráfico.

    O declive da secante ao gráfico de f, na imagem acima, que passa pelos pontos (x,f(x))
    e (x + h,f(x + h)) é dado pelo quociente de Newton:

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-b.png)

    Uma definição alternativa é: a função f é derivável em a se existir uma função φa de
    I em R contínua em a tal que:

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-c.png)

    Assim, por exemplo, se considerarmos a função f de R em R definida por f(x) = x² + x − 1,
    esta é diferenciável em 0. É possível observar na imagem abaixo os gráficos das restrições
    daquela função aos intervalos [−1,1] e [−1/10,1/10] e é claro que, enquanto que o primeiro
    é bastante curvo (e, portanto, f(x) − f(0) está aí longe de ser linear), o segundo é
    praticamente indistinguível de um segmento de reta (de declive 1). De fato, quanto mais se
    for ampliando o gráfico próximo de (0,f(0)), mais perto estará este de ser linear.

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-d.png)

    Quando obtemos a derivada de uma função, o resultado é também uma função de x e como tal
    também pode ser diferenciada. Calculando-se a derivada novamente, obtemos então a segunda
    derivada da função f. De forma semelhante, a derivada da segunda derivada é chamada de
    terceira derivada e assim por diante. Podemos nos referir às derivadas subsequentes de f
    por:

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2956-e.png)

    Se f é uma função com valores reais em R, então a derivada parcial de f mede a sua variação
    na direção dos eixos das coordenadas. Por exemplo, se f é uma função de x e y, então sua
    derivada parcial mede a variação em f na direção x e na direção y. Contudo, elas
    (derivadas parciais) não medem diretamente a variação de f em qualquer outra direção, tal
    como aquela ao longo da linha diagonal y=x. Estas são medidas usando-se as derivadas direcionais.

    Podemos calcular a derivada de uma função com 13 variáveis por meio de... “fake news, tá ok?
    Tem nada de derivada aqui não.”

    Este exercício é apenas para todo mundo aprender a ler algo, sem julgar pelos títulos e longos
    textos. Dada a base e altura de um triângulo, mostre qual sua área. “Ou vai falar que esqueceu
    como calcular área de triângulo também? Paulo Gueedes!”

    Entrada
    Dois valores de ponto flutuante P e T (0 < P, T ≤ 100000.00000), de até 5 casas decimais, que
    indicam, respectivamente, a base e a altura de um triângulo qualquer.

    Saída
    Valor real, com 5 casas decimais, representando a área do triângulo, junto da mensagem fake:
    “Concluimos que, dado o limite da entrada, a resposta seria: y = f(x) = “. Dois espaços após
    o ‘ : ’.
    :return:
    """
    p, t = map(float, input().strip().split(" "))
    area = (p * t) / 2
    print(f"Concluimos que, dado o limite da entrada, a resposta seria:  y = f(x) = {area:.5f}.")


derivada_de_13_variaveis()

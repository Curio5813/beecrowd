def corrida():
    """
    Para entrar em forma para o próximo verão, você e seu amigo
    decidiram correr todas as manhãs na rua da universidade.
    Geralmente vocês correm juntos, mas, na corrida de hoje, seu
    amigo começou a correr um mais cedo e, por isso, está um pouco
    mais à frente de você.

    Neste momento, seu amigo está a S metros de distância de você.
    Você está correndo a uma velocidade constante de va metros por
    segundo, e seu amigo está correndo a uma velocidade constante
    de vb metros por segundo. A figura abaixo ilustra a situação:

    ![imagem](https://resources.beecrowd.com/gallery/images/problems/UOJ_2516.png)

    Sua tarefa é determinar se você irá alcançar seu amigo, e, em caso
    positivo, em quantos segundos isto irá acontecer.

    Entrada
    A entrada contém vários casos de teste. A única linha de cada caso
    contém três inteiros S, va e vb (1 ≤ S, va, vb ≤ 103), a distância
    atual para seu amigo (em metros), sua velocidade (em metros por segundo)
    e a velocidade de seu amigo (em metros por segundo), respectivamente.

    A entrada termina com fim-de-arquivo (EOF).

    Saída
    Para cada caso de teste, se não é possível alcançar seu amigo, imprima
    uma linha contendo “impossivel” (sem aspas). Caso contrário, imprima uma
    linha contendo o tempo decorrido, em segundos, até que você alcance seu
    amigo. Arredonde e imprima a resposta com exatamente duas casas decimais.
    :return:
    """
    while True:
        try:
            s, va, vb = map(int, input().split(" "))
            if vb >= va:
                print("impossivel")
            else:
                t = s / (va - vb)
                print(f"{t:.2f}")
        except EOFError:
            break


corrida()

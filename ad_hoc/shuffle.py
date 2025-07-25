def shuffle():
    """
    Sua banda favorita acaba de lançar um novo álbum, e para tornar
    a experiência mais empolgante você decidiu escutar as músicas em
    uma ordem aleatória. Para isto você escreveu um algoritmo que iria
    montar uma playlist com K músicas desse álbum. O problema, porém,
    é que seu algoritmo não é muito eficiente na forma que as músicas
    são escolhidas, de forma que algumas músicas poderiam ser tocadas
    repetidas vezes antes que outras fossem tocadas ao menos uma vez.

    Dado o número de músicas do álbum, a duração de cada música, e a playlist
    gerada pelo seu algoritmo, diga quanto tempo se passou até que você tivesse
    escutado todas as músicas do álbum ao menos uma vez, se isso for possível.

    Entrada
    Haverá no máximo 150 casos de teste. Cada caso de teste inicia com dois
    inteiros M e K, indicando o número de músicas do álbum e o número de músicas
    na playlist do seu algoritmo (1 ≤ M ≤ 100, 1 ≤ K ≤ 1000).

    Em seguida haverá M inteiros mi, indicando que a i-ésima música do álbum
    dura mi minutos (1 ≤ mi ≤ 300, para todo 1 ≤ i ≤ M).

    Em seguida haverá K inteiros ki, indicando que a i-ésima música da playlist é
    a música de faixa número ki (1 ≤ ki ≤ M, para todo 1 ≤ i ≤ K).

    A entrada termina com final de arquivo (EOF).

    Saída
    Para cada caso de teste imprima uma linha, contendo um inteiro, indicando quanto
    tempo se passou até que você tivesse escutado todas as músicas do álbum ao menos
    uma vez. Caso isso não seja possível, imprima -1.
    :return:
    """
    while True:
        try:
            entrada = list(map(int, input().strip().split(" ")))
            m, k = entrada[0], entrada[1]
            todas_musicas, musicas_ouvidas, duracao_total, cont, flag = [], [], 0, 0, 0
            for i in range(1, m + 1):
                todas_musicas.append(i)
            duracao_musicas = list(map(int, input().strip().split(" ")))
            ordem_aleatoria = list(map(int, input().strip().split(" ")))
            for i in range(0, len(ordem_aleatoria)):
                duracao_total += duracao_musicas[ordem_aleatoria[i] - 1]
                if ordem_aleatoria[i] not in musicas_ouvidas:
                    musicas_ouvidas.append(ordem_aleatoria[i])
                    cont += 1
                    if cont == m:
                        flag = 1
                        break
            if flag == 1:
                print(duracao_total)
            if flag == 0:
                print(-1)
        except EOFError:
            break


shuffle()

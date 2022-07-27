def sentenca_dancante():
    while True:
        texto, lista, rascunho, espaco = '', [], '', []
        try:
            sentenca = input()
        except EOFError:
            return None
        else:
            for k in range(0, len(sentenca)):
                if sentenca[k] == ' ':
                    espaco.append(k)
                lista.append(sentenca[k])
            for k in range(0, len(lista)):
                texto += lista[k]
                texto = texto.replace(' ', '')
            lista = []
            for k in range(0, len(texto)):
                if k % 2 == 0:
                    rascunho += texto[k].upper()
                if k % 2 == 1:
                    rascunho += texto[k].lower()
                lista.append(rascunho)
                rascunho = ''
            texto = ''
            for k in range(0, len(espaco)):
                lista.insert(espaco[k], ' ')
            for k in range(0, len(lista)):
                texto += lista[k]
            print(texto)


sentenca_dancante()

from collections import deque


def atalhos_bloggo():
    """
    Você está ajudando a desenvolver um sistema de gerenciamento
    de weblog chamado bloggo. Embora bloggo coloque todo o conteúdo
    direto no website em HTML, nem todos autores apreciam usar tags
    HTML em seus textos. Para tornar a vida deles mais fáceis, bloggo
    oferece uma sintaxe simples chamada atalhos para obter alguns
    efeitos textuais em HTML. Sua tarefa é, dado um documento escrito
    com atalhos, traduzi-lo para o HTML apropriado.


    Um atalho é usado para colocar texto em itálico. HTML faz isto com as
    tags <i> e </i>, mas no bloggo um autor pode simplesmente colocar um
    pedaço de texto entre dois caracteres de sublinhado, '_'. Portanto,
    onde um autor escreve

      You _should_ see the baby elephant at the zoo!

    bloggo vai publicar o seguinte:

      You <i>should</i> see the baby elephant at the zoo!

    Outro atalho serve para colocar texto em negrito, o que, em HTML, é feito
    com as tags <b> e </b>. Bloggo permite aos autores fazer o mesmo com
    pares do caractere asterisco, '*'. Quando um autor escreve o texto

      Move it from *Receiving* to *Accounts Payable*.

    ele vai sair no website assim:

      Move it from <b>Receiving</b> to <b>Accounts Payable</b>.

    Entrada
    A entrada contem vários casos de teste. Cada caso de teste é composto por
    uma linha que contem uma string texto, com zero ou mais usos dos atalhos
    itálico e negrito. Cada texto tem de 1 a 50 caracteres, inclusive. Os
    únicos caracteres permitidos no texto são os caracteres alfabéticos
    (de 'a' a 'z' e de 'A' a 'Z'), o sublinhado ('_'), o asterisco ('*'),
    o caractere de espaço e os símbolos de pontuação ',', ';', '.', '!',
    '?', '-', '(' e ')'. O caractere sublinhado '_' ocorre no texto um número
    par de vezes. O asterisco '*' também aparece um número par de vezes no
    texto. Nenhuma substring do texto entre um par de sublinhados ou entre
    um par de asteriscos pode conter outros sublinhados ou asteriscos,
    respectivamente.

    Saída
    Para cada linha de entrada seu programa deve gerar uma linha de saída com o
    texto traduzido para HTML como demonstrado nos exemplos abaixo. Para tornar
    itálico um pedaço de texto no HTML, você deve iniciar este pedaço com a
    tag <i> e terminá-lo com a tag </i>. Para texto em negrito, inicie com <b>
    e termine com </b>.

    O final da entrada é determinado por EOF.
    :return:
    """
    while True:
        try:
            texto = input()
            fila, flag1, flag2 = [], False, False
            for i in texto:
                if i == '*':
                    if flag1 == False:
                        fila.append('<b>')
                        flag1 = True
                    else:
                        fila.append('</b>')
                        flag1 = False
                elif i == '_':
                    if flag2 == False:
                        fila.append('<i>')
                        flag2 = True
                    else:
                        fila.append('</i>')
                        flag2 = False
            lista = deque(texto)
            tamanho_original = len(texto)
            caracteres_processados = 0

            while caracteres_processados < tamanho_original:
                if lista[0] == '*':
                    lista[0] = fila.pop(0)
                    lista.rotate(-1)
                elif lista[0] == '_':
                    lista[0] = fila.pop(0)
                    lista.rotate(-1)
                else:
                    lista.rotate(-1)
                caracteres_processados += 1
            print("".join(lista))
        except EOFError:
            break


atalhos_bloggo()

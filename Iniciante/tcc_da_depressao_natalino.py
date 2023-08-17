def tcc_da_depressao_natalino():
    """
    Esta função recebe como entrada um valor E (0 < E < 25), representando o
    dia que foi entregue o tcc pra verificação e um valor D (0 < D < 25) que
    representa a data final pra entregar para verificação. A única possibilidade
    da entrega não ser realizada na data é por falta de orientação da Takanada.
    Caso não seja possivel, imprima "Eu odeio a professora!". Caso seja entregue
    em até 3 dias antes do prazo final, imprima "Muito bem! Apresenta antes do
    Natal!", caso contrário, sendo muito próximo da data limite imprima "Parece
    o trabalho do meu filho!", nesse ultimo caso, é adicionado mais dois dias
    para correções, e caso a data final seja menor que a véspera do natal(24),
    ela poderá apresentar, sendo impresso "TCC Apresentado!", caso contrário
    imprima "Fail! Entao eh nataaaaal!"
    :return:
    """
    e, d = map(int, input().split(" "))
    if d - e >= 3:
        print("Muito bem! Apresenta antes do Natal!")
    elif d == 22:
        print("Parece o trabalho do meu filho!")
        print("TCC Apresentado!")
    elif d == 23:
        print("Parece o trabalho do meu filho!")
        print("Fail! Entao eh nataaaaal!")
    else:
        print("Eu odeio a professora!")


tcc_da_depressao_natalino()

from math import ceil, floor
from copy import deepcopy
from traceback import print_tb


def outra_crise():
    """
    Há dois anos atrás, uma nova crise mundial teve início, deixando muitas
    pessoas com problemas econômicos. Alguns trabalhadores de uma empresa
    estão tentando pedir um aumento de salário.

    A empresa possui uma hierarquia restrita, onde cada empregado tem exatamente
    um chefe, com a exceção do dono da companhia que não tem chefe. Empregados que
    não são chefes de nenhum outro empregado são chamados trabalhadores. O resto
    dos empregados e o dono são chamados de chefes.

    Para pedir aumento, um trabalhador deve enviar uma petição ao seu chefe direto.
    Evidentemente, cada chefe é encorajado a tentar manter seus subordinados felizes
    com seu salário atual, tornando o lucro da empresa o maior possível. No entanto,
    quando ao menos T porcento de seus subordinados diretos fazem uma petição, o chefe
    será pressionado e não terá escolha a não ser enviar uma petição ele mesmo ao seu
    superior direto. Cada chefe envia no máximo uma petição para seu próprio chefe,
    independente do seu número de subordinatos que o enviaram. Um chefe somente considera
    seus subordinados diretos (os que fizeram a petição e os que não a fizeram) para
    calcular o a porcentagem da pressão.

    Note que um chefe pode ter trabalhadores e chefes como seus subordinados diretos ao
    mesmo tempo, e ele pode receber petições de ambos os tipos de empregados. Cada subordinado
    direto, independente de seu cargo, terá peso 1 ao realizar o balanço total. Quando uma
    petição chega ao dono da empresa, todos os salários são aumentados. O sindicato dos
    trabalhadores está desesperado tentando fazer isso acontecer, então eles precisam convencer
    alguns trabalhadores a enviar uma petição aos seus chefes.

    Dados a hierarquia da empresa e o parâmetro T, você deve encontrar o menor número de
    trabalhadores que deve enviar uma petição de forma a fazer com que o dono da empresa
    aumente os salários.

    Entrada
    A entrada contém vários casos de teste. Cada caso de teste é dado em exatamente duas
    linhas. A primeira linha contém dois inteiros N e T (1 ≤ N ≤ 105 e 1 ≤ T ≤ 100), separados
    por um espaço em branco. N indica o número de empregados da empresa (sem considerar o dono)
    e T é o parâmetro descrito acima. Cada um dos empregados é identificado por um inteiro entre
    1 e N, inclusive. O dono é identificado pelo número 0. A segunda linha contém uma lista de
    inteiros separados por um espaço em branco. O inteiro Bi, na posição i dessa lista (começando
    de 1), indica o identificador do chefe direto do empregado i (0 ≤ Bi ≤ i - 1).

    O último caso de teste é seguido de uma linha contendo dois zeros separados por um espaço em
    branco.

    Saída
    Para cada caso de teste, imprima uma única linha contendo um único inteiro, a menor quantidade
    de trabalhadores que deve enviar uma petição de modo a fazer com que o dono da empresa receba
    uma petição.
    :return:
    """
    entrada = list(map(int, input().strip().split(" ")))
    n, t = entrada[0], entrada[1]
    while n != 0 and t != 0:
        workers = list(map(int, input().strip().split(" ")))
        worker = 0
        for i in range(0, len(workers)):
            workers[i] += 1
        if workers.count(1) == len(workers):
            worker = len(workers)
            quorum = round(worker * (t/100))
            print(quorum)
        else:
            for i in range(0, len(workers)):
                if i + 1 not in workers:
                    print(i + 1, end=" ")
                    worker += 1
            print()
            # print(worker)
            quorum = round(worker * (t/100))
            print(quorum)
        entrada = list(map(int, input().strip().split(" ")))
        n, t = entrada[0], entrada[1]


outra_crise()


"""
3 100
0 0 0
3 50
0 0 0
14 60
0 0 1 1 2 2 2 5 7 5 7 5 7 5
7 68
0 0 1 1 2 2 3
60 37
0 1 2 3 3 3 6 2 2 9 10 9 9 13 1 1 16 17 18 17 17 21 16 16 24 25 24 24 28 0 0 31 32 33 34 33 33 37 32 32 40 41 40 40 44 31 31 47 48 49 48 48 52 47 47 55 56 55 55 59
1035 70
0 1 2 3 4 5 6 7 8 7 7 11 6 6 14 15 14 14 18 5 5 21 22 23 22 22 26 21 21 29 30 29 29 33 4 4 36 37 38 39 38 38 42 37 37 45 46 45 45 49 36 36 52 53 54 53 53 57 52 52 60 61 60 60 64 3 3 67 68 69 70 71 70 70 74 69 69 77 78 77 77 81 68 68 84 85 86 85 85 89 84 84 92 93 92 92 96 67 67 99 100 101 102 101 101 105 100 100 108 109 108 108 112 99 99 115 116 117 116 116 120 115 115 123 124 123 123 127 127 2 2 131 132 133 134 135 136 135 135 139 134 134 142 143 142 142 146 133 133 149 150 151 150 150 154 149 149 157 158 157 157 161 132 132 164 165 166 167 166 166 170 165 165 173 174 173 173 177 164 164 180 181 182 181 181 185 180 180 188 189 188 188 192 192 131 131 196 197 198 199 200 199 199 203 198 198 206 207 206 206 210 197 197 213 214 215 214 214 218 213 213 221 222 221 221 225 196 196 228 229 230 231 230 230 234 229 229 237 238 237 237 241 228 228 244 245 246 245 245 249 244 244 252 253 252 252 256 256 1 1 260 261 262 263 264 265 266 265 265 269 264 264 272 273 272 272 276 263 263 279 280 281 280 280 284 279 279 287 288 287 287 291 262 262 294 295 296 297 296 296 300 295 295 303 304 303 303 307 294 294 310 311 312 311 311 315 310 310 318 319 318 318 322 322 261 261 326 327 328 329 330 329 329 333 328 328 336 337 336 336 340 327 327 343 344 345 344 344 348 343 343 351 352 351 351 355 326 326 358 359 360 361 360 360 364 359 359 367 368 367 367 371 358 358 374 375 376 375 375 379 374 374 382 383 382 382 386 386 260 260 390 391 392 393 394 395 394 394 398 393 393 401 402 401 401 405 392 392 408 409 410 409 409 413 408 408 416 417 416 416 420 391 391 423 424 425 426 425 425 429 424 424 432 433 432 432 436 423 423 439 440 441 440 440 444 439 439 447 448 447 447 451 451 390 390 455 456 457 458 459 458 458 462 457 457 465 466 465 465 469 456 456 472 473 474 473 473 477 472 472 480 481 480 480 484 455 455 487 488 489 490 489 489 493 488 488 496 497 496 496 500 487 487 503 504 505 504 504 508 503 503 511 512 511 511 515 515 0 0 519 520 521 522 523 524 525 526 525 525 529 524 524 532 533 532 532 536 523 523 539 540 541 540 540 544 539 539 547 548 547 547 551 522 522 554 555 556 557 556 556 560 555 555 563 564 563 563 567 554 554 570 571 572 571 571 575 570 570 578 579 578 578 582 521 521 585 586 587 588 589 588 588 592 587 587 595 596 595 595 599 586 586 602 603 604 603 603 607 602 602 610 611 610 610 614 585 585 617 618 619 620 619 619 623 618 618 626 627 626 626 630 617 617 633 634 635 634 634 638 633 633 641 642 641 641 645 645 520 520 649 650 651 652 653 654 653 653 657 652 652 660 661 660 660 664 651 651 667 668 669 668 668 672 667 667 675 676 675 675 679 650 650 682 683 684 685 684 684 688 683 683 691 692 691 691 695 682 682 698 699 700 699 699 703 698 698 706 707 706 706 710 710 649 649 714 715 716 717 718 717 717 721 716 716 724 725 724 724 728 715 715 731 732 733 732 732 736 731 731 739 740 739 739 743 714 714 746 747 748 749 748 748 752 747 747 755 756 755 755 759 746 746 762 763 764 763 763 767 762 762 770 771 770 770 774 774 519 519 778 779 780 781 782 783 784 783 783 787 782 782 790 791 790 790 794 781 781 797 798 799 798 798 802 797 797 805 806 805 805 809 780 780 812 813 814 815 814 814 818 813 813 821 822 821 821 825 812 812 828 829 830 829 829 833 828 828 836 837 836 836 840 840 779 779 844 845 846 847 848 847 847 851 846 846 854 855 854 854 858 845 845 861 862 863 862 862 866 861 861 869 870 869 869 873 844 844 876 877 878 879 878 878 882 877 877 885 886 885 885 889 876 876 892 893 894 893 893 897 892 892 900 901 900 900 904 904 778 778 908 909 910 911 912 913 912 912 916 911 911 919 920 919 919 923 910 910 926 927 928 927 927 931 926 926 934 935 934 934 938 909 909 941 942 943 944 943 943 947 942 942 950 951 950 950 954 941 941 957 958 959 958 958 962 957 957 965 966 965 965 969 969 908 908 973 974 975 976 977 976 976 980 975 975 983 984 983 983 987 974 974 990 991 992 991 991 995 990 990 998 999 998 998 1002 973 973 1005 1006 1007 1008 1007 1007 1011 1006 1006 1014 1015 1014 1014 1018 1005 1005 1021 1022 1023 1022 1022 1026 1021 1021 1029 1030 1029 1029 1033 1033
"""
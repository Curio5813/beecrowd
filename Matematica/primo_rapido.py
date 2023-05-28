import multiprocessing
from random import randint
from datetime import datetime

n = 200
inicio = datetime.now()


def primo_rapido_25():
    for i in range(n):
        x = randint(2, 2 ** 25)
        for k in range(2, x + 1):
            if x == 2:
                print('Prime')
                break
            elif x == 3:
                print('Prime')
                break
            elif x % 2 == 0:
                print('Not Prime')
                break
            elif x % k == 0 and k != x:
                print('Not Prime')
                break
            elif x % k == 0 and k == x:
                print('Prime')
                break


"""
def primo_rapido_25():
    for i in range(n):
        x = randint(2 ** 20, 2 ** 25)
        for k in range(2, x + 1):
            if x == 2:
                print('Prime')
                break
            elif x == 3:
                print('Prime')
                break
            elif x % 2 == 0:
                print('Not Prime')
                break
            elif x % k == 0 and k != x:
                print('Not Prime')
                break
            elif x % k == 0 and k == x:
                print('Prime')
                break



def primo_rapido_28():
    for i in range(n):
        with lock:
            x = randint(2 ** 25, 2 ** 28)
            for k in range(2, x + 1):
                if x == 2:
                    print('Prime')
                    break
                elif x == 3:
                    print('Prime')
                    break
                elif x % 2 == 0:
                    print('Not Prime')
                    break
                elif x % k == 0 and k != x:
                    print('Not Prime')
                    break


def primo_rapido_31():
    for i in range(n):
        with lock:
            x = randint(2 ** 28, 2 ** 31)
            for k in range(2, x + 1):
                if x == 2:
                    print('Prime')
                    break
                elif x == 3:
                    print('Prime')
                    break
                elif x % 2 == 0:
                    print('Not Prime')
                    break
                elif x % k == 0 and k != x:
                    print('Not Prime')
                    break
"""


def main():
    pc1 = multiprocessing.Process(target=primo_rapido_25())
    # pc2 = multiprocessing.Process(target=primo_rapido_25())
    # pc3 = multiprocessing.Process(target=primo_rapido_28(), args=lock)
    # pc4 = multiprocessing.Process(target=primo_rapido_31(), args=lock)

    pc1.start()
    # pc2.start()
    # pc3.start()
    # pc4.start()

    pc1.join()
    # pc2.join()
    # pc3.join()
    # pc4.join()


cont = 0
if __name__ == '__main__':
    cont += 1
    if cont < n:
        primo_rapido_25()
        # primo_rapido_25()
        # primo_rapido_28()
        # primo_rapido_31()

tempo = datetime.now() - inicio
print(f"Terminou em {tempo.total_seconds():.2f} segundos.")

# Terminou em 21.08 segs

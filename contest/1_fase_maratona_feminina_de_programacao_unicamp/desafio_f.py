def desafio_f():
    t1, t2 = 0, 0
    n = int(input())
    for i in range(n):
        times = input().split(" ")
        if int(times[1]) == 1:
            t1 += int(times[2][1])
        if int(times[1]) == 2:
            t2 += int(times[2][1])
    print(f"{t1} x {t2}")


desafio_f()

def fibonacciSequencie():
    """
    This function return tem first 15th terms of the Fibonnaci
    Sequencie.
    :return:
    """
    a, b, p = 0, 0, 1
    for i in range(0, 15):
        a, b = b, p
        p = a + b
        print(a)


fibonacciSequencie()

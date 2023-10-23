def honeycomb_walk():
    """
    A bee larva living in a hexagonal cell of a large honeycomb decides
    to creep for a walk. In each “step” the larva may move into any of
    the six adjacent cells and after n steps, it is to end up in its
    original cell. this function compute, for a given n, the number of
    different such larva walks. A input the first line contains an integer
    giving the number of test cases to follow. Each case consists of one
    line containing an integer n, where 1 ≤ n ≤ 14. the output for each
    test case, output one line containing the number of walks. Under the
    assumption 1 ≤ n ≤ 14, the answer will be less than 2³¹.
    :return:
    """
    comb = [0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600]
    n = int(input())
    for i in range(n):
        walks = int(input())
        combs = comb[walks - 1]
        print(combs)


honeycomb_walk()

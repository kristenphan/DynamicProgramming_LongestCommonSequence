# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    # create a 2D array to store the result of the longest common sequence (lcs)
    T = [[float("inf")]*(len(second_sequence)+1) for _ in range (len(first_sequence)+1)]

    # iterate through the passed in sequences and fill in the result array T
    # instances where one of the passed in sequence is empty (ie. length == 0)
    # in that case, T == 0 as there is no matching element in the two sequences
    for i in range(len(first_sequence)+1):
        T[i][0] = 0
    for j in range(len(second_sequence)+1):
        T[0][j] = 0

    # iterate through the passed in sequences and fill in the result array T
    for i in range(1, len(first_sequence)+1):
        for j in range(1, len(second_sequence)+1):
            if first_sequence[i-1] == second_sequence[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i][j-1], T[i-1][j])

    return T[len(first_sequence)][len(second_sequence)]



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    #a = (2, 7, 8)
    #b= (5, 2, 8, 7, 8)
    print(lcs2(a, b))

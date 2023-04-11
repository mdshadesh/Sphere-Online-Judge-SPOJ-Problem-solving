t = int(input())

for i in range(t):
    l, c = map(int, input().split())

    for j in range(l):
        for k in range(c):
            if j == 0 or j == l - 1 or k == 0 or k == c - 1:
                print('*', end='')
            else:
                print('.', end='')
        print()

    if i < t - 1:
        print()

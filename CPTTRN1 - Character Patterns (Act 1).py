t = int(input())

for i in range(t):
    l, c = map(int, input().split())

    for j in range(l):
        for k in range(c):
            if (j + k) % 2 == 0:
                print('*', end='')
            else:
                print('.', end='')
        print()

    if i < t - 1:
        print()

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    result = []

    for i in range(1, n):
        if i % x == 0 and i % y != 0:
            result.append(i)

    print(" ".join(map(str, result)))

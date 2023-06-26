a, b = map(int, input().split())

sum_of_squares = sum([x*x for x in range(a, b+1)])

print(sum_of_squares)

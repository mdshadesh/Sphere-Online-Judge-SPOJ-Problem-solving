import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # Compute the distance between the centers of the circles
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Check if one circle is inside the other
    if distance + min(r1, r2) < max(r1, r2):
        print("I")  # One circle is inside the other
    elif distance <= abs(r1 - r2):
        print("E")  # One circle is internally tangent to the other
    else:
        print("O")  # Neither of the above cases, circles are not inside or tangent to each other

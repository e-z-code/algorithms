import sys


# 2. A FUNCTION TO GET DIRECTION

def get_dir(x, y, A, B, C):

    result = A * x + B * y + C
    if result < 0:
        return -1
    elif result > 0:
        return 1
    else:
        return 0


# 1. TO GET THE INPUT

point_cnt = int(sys.stdin.readline())

red_points = set()
for point in range(point_cnt):
    x, y = map(int, sys.stdin.readline().split())
    red_points.add((x, y))
blue_points = set()
for point in range(point_cnt):
    x, y = map(int, sys.stdin.readline().split())
    blue_points.add((x, y))


# 3. TO SOLVE THE PROBLEM

# Centroid should also be symmetric.
# Thus, we can get axis of symmetry L : Ax + By + C = 0

red_x, red_y = 0, 0
for x, y in red_points:
    red_x += x
    red_y += y
blue_x, blue_y = 0, 0
for x, y in blue_points:
    blue_x += x
    blue_y += y

# To check if points are clearly separated and symmetric points exist

ans = "possible"

A = 2 * point_cnt * (blue_x - red_x)
B = -2 * point_cnt * (red_y - blue_y)
C = pow(red_x, 2) - pow(blue_x, 2) + pow(red_y, 2) - pow(blue_y, 2)

if A == 0 and B == 0:
    ans = "impossible"
else:

    right_direction = None
    for red_x, red_y in red_points:

        direction = get_dir(red_x, red_y, A, B, C)
        if right_direction is None:
            right_direction = direction
        else:
            if right_direction != direction:
                ans = "impossible"
                break

        blue_x = red_x - 2 * A * (A * red_x + B * red_y + C) // (A * A + B * B)
        blue_y = red_y - 2 * B * (A * red_x + B * red_y + C) // (A * A + B * B)
        if (blue_x, blue_y) not in blue_points:
            ans = "impossible"
            break

print(ans)
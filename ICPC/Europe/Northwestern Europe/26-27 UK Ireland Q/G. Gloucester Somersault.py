import sys
INF = float('inf')

def get_dist(p1, p2):

    x1, y1 = p1
    x2, y2 = p2

    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)


# 2. CCW FUNCTION

def ccw(p1, p2, p3):

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


# 1. TO GET THE INPUT

point_cnt, goal = map(int, sys.stdin.readline().split())

start_x = INF

points = []
for point in range(point_cnt):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
    if y == 0 and x < start_x:
        start_x = x
points.sort()


# 3. MONOTONE CHAIN

upper_hull = []

for point in points:
    while len(upper_hull) > 1 and ccw(upper_hull[-2], upper_hull[-1], point) >= 0:
        upper_hull.pop()
    upper_hull.append(point)

lower_hull = []

for point in points:
    while len(lower_hull) > 1 and ccw(lower_hull[-2], lower_hull[-1], point) <= 0:
        lower_hull.pop()
    lower_hull.append(point)

convex_hull = upper_hull + lower_hull[1:-1][::-1]


# 4. TO SOLVE THE PROBLEM

length = 0
for idx in range(len(convex_hull)):
    length += get_dist(convex_hull[idx-1], convex_hull[idx])

rotate_cnt = (goal - start_x) // length + 1
for x, y in points:
    if y == 0 and x + (rotate_cnt - 1) * length > goal:
        rotate_cnt -= 1
        break

print(int(rotate_cnt))
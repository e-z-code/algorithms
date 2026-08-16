import sys
from math import sqrt


# 2. A FUNCTION TO GET INTERSECTIONS

def get_dist_squared(pointX, pointY):

    x1, y1 = pointX
    x2, y2 = pointY

    return pow(x1 - x2, 2) + pow(y1 - y2, 2)

def get_dist(pointX, pointY):

    return sqrt(get_dist_squared(pointX, pointY))

def point_in_circle(point, circle):

    x, y = point
    center_x, center_y, r = circle

    if pow(center_x - x, 2) + pow(center_y - y, 2) <= pow(r, 2):
        return True
    else:
        return False

def get_candidates(circleX, circleY):

    if circleX[2] < circleY[2]:
        circleX, circleY = circleY, circleX
    x1, y1, r1 = circleX
    x2, y2, r2 = circleY

    center_dist_squared = get_dist_squared((x1, y1), (x2, y2))
    if center_dist_squared <= pow(r1 - r2, 2):
        return max(0, get_dist(point, (x2, y2)) - r2)
    else:

        # Intersections
        
        dx, dy = x2 - x1, y2 - y1
        d = sqrt(pow(dx, 2) + pow(dy, 2))
        unit_dx, unit_dy = dx / d, dy / d

        alpha = (pow(r1, 2) - pow(r2, 2) + pow(d, 2)) / (2 * d)
        center_x = x1 + alpha * unit_dx
        center_y = y1 + alpha * unit_dy

        beta = sqrt(pow(r1, 2) - pow(alpha, 2))
        candidateA = (center_x - beta * unit_dy, center_y + beta * unit_dx)
        candidateB = (center_x + beta * unit_dy, center_y - beta * unit_dx)
        result = min(get_dist(candidateA, point), get_dist(candidateB, point))
        
        # Shortest points

        point_in_circleX = point_in_circle(point, circleX)
        point_in_circleY = point_in_circle(point, circleY)

        if point_in_circleX and point_in_circleY:
            result = 0
        else:

            if not point_in_circle(point, circleX):

                dx, dy = x1 - point_x, y1 - point_y
                d = sqrt(pow(dx, 2) + pow(dy, 2))
                unit_dx, unit_dy = dx / d, dy / d

                candidateC = (x1 - r1 * unit_dx, y1 - r1 * unit_dy)
                if point_in_circle(candidateC, circleY):
                    result = min(result, get_dist(candidateC, point))

            if not point_in_circle(point, circleY):

                dx, dy = x2 - point_x, y2 - point_y
                d = sqrt(pow(dx, 2) + pow(dy, 2))
                unit_dx, unit_dy = dx / d, dy / d

                candidateD = (x2 - r2 * unit_dx, y2 - r2 * unit_dy)
                if point_in_circle(candidateD, circleX):
                    result = min(result, get_dist(candidateD, point))

        return result


# 1. TO GET THE INPUT

circle_cnt = int(sys.stdin.readline())
point_x, point_y = map(int, sys.stdin.readline().split())
point = (point_x, point_y)

circles = []
for circle in range(circle_cnt):
    center_x, center_y, radius = map(int, sys.stdin.readline().split())
    circles.append((center_x, center_y, radius))


# 3. TO SOLVE THE PROBLEM

ans = 0

for i in range(circle_cnt):
    for j in range(i, circle_cnt):
        ans = max(ans, get_candidates(circles[i], circles[j]))

print(ans)
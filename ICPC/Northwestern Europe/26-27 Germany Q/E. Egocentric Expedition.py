import sys
from decimal import Decimal
root2 = Decimal('2') ** Decimal('0.5')


# 1. A FUNCTION TO GET DISTANCE

def get_dist(pointA, pointB):

    xA, yA = pointA
    xB, yB = pointB

    return ((xA - xB) * (xA - xB) + (yA - yB) * (yA - yB)) ** Decimal('0.5')


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

test_cnt = int(sys.stdin.readline())

for test in range(test_cnt):

    print("?", 1, 0)
    sys.stdout.flush()
    dist_to_A = Decimal(sys.stdin.readline().strip())
    pointA = (dist_to_A, 0)

    print("?", 1, 1)
    sys.stdout.flush()
    dist_to_B = Decimal(sys.stdin.readline().strip())
    pointB = (dist_to_B / root2, dist_to_B / root2)

    short_length = dist_to_A * dist_to_B / root2 / get_dist(pointA, pointB)
    ans = 4 * short_length * short_length
    if int(ans - Decimal('0.5')) == int(ans):
        ans = int(ans) + 1
    else:
        ans = int(ans)
    print("!", ans)
    sys.stdout.flush()
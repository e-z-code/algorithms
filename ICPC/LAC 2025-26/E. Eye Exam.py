import sys
INF = float('inf')


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

check_count = int(sys.stdin.readline())

valid = True
min_val = -INF
max_val = INF

for check in range(check_count):

    valA, valB, result = sys.stdin.readline().strip().split()
    valA = int(valA)
    valB = int(valB)

    if result == "E":

        if (valA + valB) % 2 == 0:
            boundary = (valA + valB) // 2
            if min_val <= boundary <= max_val:
                min_val = boundary
                max_val = boundary
            else:
                valid = False
        else:
            valid = False

    elif result == "A":

        if (valA + valB) % 2 == 0:
            boundary = (valA + valB) // 2 - 1
        else:
            boundary = (valA + valB) // 2

        if min_val <= boundary:
            max_val = min(max_val, boundary)
        else:
            valid = False

    elif result == "B":

        boundary = (valA + valB) // 2 + 1

        if boundary <= max_val:
            min_val = max(min_val, boundary)
        else:
            valid = False

if valid:
    print(min_val, max_val)
else:
    print("*")
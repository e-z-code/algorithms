import sys

def plus_one(num):
    return num + 1


# 1. TO GET THE INPUT

plate_count, day_count = map(int, sys.stdin.readline().split())
used_count = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

plates = [0 for plate in range(plate_count)]

for today_used_count in used_count:
    plates[-today_used_count:] = sorted(list(map(plus_one, plates[-today_used_count:])), reverse=True)

print(max(plates))
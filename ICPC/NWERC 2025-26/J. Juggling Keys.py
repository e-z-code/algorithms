import sys


# 1. TO GET THE INPUT

people_count, key_count, trip_count = map(int, sys.stdin.readline().split())

trips = []
for trip in range(trip_count):
    person, start_time, end_time = map(int, sys.stdin.readline().split())
    trips.append((start_time, end_time))


# 2. TO SOLVE THE PROBLEM

changes = []
for idx in range(trip_count):
    changes.append((trips[idx][0], -1, idx))
    changes.append((trips[idx][1], 1, idx))
changes.sort()

# To find trips that need a key

answer = [0 for idx in range(trip_count)]

imos = []
now_people = people_count
for time, change, idx in changes:
    if change == -1:
        now_people -= 1
    else:
        if now_people == 0:
            answer[idx] = 1
            imos.append((trips[idx][0], 1))
            imos.append((trips[idx][1], -1))
        now_people += 1

# To check impossibility

imos.sort()

max_key = 0
now_key = 0
for time, delta in imos:
    now_key += delta
    max_key = max(max_key, now_key)

if max_key <= key_count:
    print("".join(map(str, answer)))
else:
    print("impossible")
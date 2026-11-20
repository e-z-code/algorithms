import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())

ans = "yes"
storage = {}
for schedule in range(length):
    order, item = sys.stdin.readline().strip().split()
    if order == "pickup":
        if item in storage:
            ans = ("no")
            break
        else:
            storage[item] = 1
    else:
        if item in storage:
            if storage[item] == 0:
                ans = "no"
                break
            else:
                storage[item] -= 1
        else:
            ans = "no"
            break

for item in storage:
    if storage[item] != 0:
        ans = "no"
        break

print(ans)
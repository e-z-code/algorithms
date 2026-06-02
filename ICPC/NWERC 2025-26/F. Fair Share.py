import sys


# 1. TO GET THE INPUT

people_count = int(sys.stdin.readline())

shares = []
debts = []
for person in range(people_count):
    share, debt = map(int, sys.stdin.readline().split())
    shares.append(share)
    debts.append(debt)


# 2. TO SOLVE THE PROBLEM

total_share = sum(shares)
total_debt = sum(debts)

ans = "impossible"
for person in range(people_count):
    if total_debt - (total_share - shares[person]) <= debts[person]:
        ans = person + 1
        break
print(ans)